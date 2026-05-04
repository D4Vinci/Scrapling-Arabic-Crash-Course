from scrapling.spiders import Spider, Request, Response
from scrapling.fetchers import FetcherSession, AsyncStealthySession


class ExampleSpider(Spider):
    name = "test_spider"
    start_urls = ["https://quotes.toscrape.com/"]
    allowed_domains = {"toscrape.com"}
    concurrent_requests = 8
    concurrent_requests_per_domain = 4
    max_blocked_retries = 3
    
    robots_txt_obey = False
    development_mode = False
    download_delay = 0

    def configure_sessions(self, manager):
        manager.add("requests", FetcherSession(), default=True)
        manager.add("stealth", AsyncStealthySession(headless=False, max_pages=10), lazy=True)

    async def is_blocked(self, response: Response) -> bool:
        if response.status in {403, 429, 503}:
            return True

        body = response.body.decode("utf-8", errors="ignore")
        if "access denied" in body.lower() or "rate limit" in body.lower():
            return True

        return False

    async def retry_blocked_request(self, request: Request, response: Response) -> Request:
        request.sid = "stealth"
        self.logger.info(f"Retrying blocked request: {request.url}")
        return request

    async def parse(self, response: Response):
        for author in response.css('a[href*="/author/"]::attr(href)').getall():
            yield Request(response.urljoin(author), sid="stealth", disable_resources=True, callback=self.parse_author, priority=10, meta={'test': 'value'})  # higher priority values are processed first

    async def parse_author(self, response: Response):
        print(response.meta.get('test'))
        yield {
            '.author-title': response.css('.author-title::text').get(),
            "birthday": response.css('.author-born-date::text').get(),
            "url": response.url,
        }


if __name__ == "__main__":
    result = ExampleSpider().start(use_uvloop=True)
    stats = result.stats
