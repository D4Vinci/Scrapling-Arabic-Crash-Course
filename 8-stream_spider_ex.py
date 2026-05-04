import logging

import anyio
from scrapling.spiders import Spider, Response

class QuotesSpider(Spider):
    name = "quotes"
    start_urls = ["https://quotes.toscrape.com"]
    logging_level = logging.INFO

    async def parse(self, response: Response):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(""),
                "author": quote.css("small.author::text").get(""),
            }

        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    async def on_start(self, resuming: bool = False):
        self.logger.info("Spider starting up")
        # Load seed URLs from a database, initialize counters, etc.
    
    async def on_close(self):
        self.logger.info("Spider shutting down")
        # Close database connections, flush buffers, etc.
    
    async def on_scraped_item(self, item: dict) -> dict | None:
        # Drop items without author
        if not item.get("author"):
            return None

        # Modify items (e.g., add timestamps)
        item["scraped_at"] = "2026-4-26"
        return item
    

should_pause = False

async def main():
    spider = QuotesSpider(crawldir="crawl_data/my_spider")
    async for item in spider.stream():
        print(item)
        print(f"Items so far: {spider.stats.items_scraped}")
        print(f"Requests made: {spider.stats.requests_count}")
        if should_pause:
            spider.pause()

if __name__ == "__main__":
    anyio.run(main)
