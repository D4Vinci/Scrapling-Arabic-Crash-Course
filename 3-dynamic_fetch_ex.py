import asyncio
from scrapling.fetchers import DynamicFetcher, DynamicSession, AsyncDynamicSession

# page = DynamicFetcher.fetch('https://quotes.toscrape.com/js/', headless=False)
# page = await DynamicFetcher.async_fetch('https://quotes.toscrape.com/js/')
# print(len(page.css(".quote")))

# DynamicFetcher.fetch('https://quotes.toscrape.com/js/', real_chrome=True)
# DynamicFetcher.fetch('https://example.com', cdp_url='ws://localhost:9222')

# page = DynamicFetcher.fetch('https://quotes.toscrape.com/js-delayed/', wait_selector=".quote", wait_selector_state='visible', headless=False)
# page = DynamicFetcher.fetch('https://example.com', disable_resources=True)
# page = DynamicFetcher.fetch('https://example.com', network_idle=True)
# page = DynamicFetcher.fetch('https://example.com', timeout=30000)
# page = DynamicFetcher.fetch('https://example.com', proxy='http://username:password@host:port')
# page = DynamicFetcher.fetch(
#     'https://example.com',
#     google_search=True,
#     useragent='Mozilla/5.0...',
#     locale='en-US',
# )


# from playwright.sync_api import Page

# def capture_websockets(page: Page):
#     page.on("websocket", lambda ws: print(f"WebSocket opened: {ws.url}"))

# def scroll_page(page: Page):
#     page.mouse.wheel(10, 0)
#     page.mouse.move(100, 400)
#     page.mouse.up()

# page = DynamicFetcher.fetch('https://example.com', page_action=scroll_page, page_setup=capture_websockets)



# with DynamicSession(
#     headless=True,
#     disable_resources=True,
#     real_chrome=True
# ) as session:
#     page1 = session.fetch('https://quotes.toscrape.com/js/')
#     page2 = session.fetch('https://books.toscrape.com/')
#     page3 = session.fetch('https://www.scrapethissite.com/pages/ajax-javascript/')



# async def scrape_multiple_sites():
#     async with AsyncDynamicSession(
#         network_idle=True,
#         timeout=30000,
#         max_pages=3,
#         headless=False
#     ) as session:
#         pages = await asyncio.gather(
#             session.fetch('https://quotes.toscrape.com/js/'),
#             session.fetch('https://books.toscrape.com/'),
#             session.fetch('https://www.scrapethissite.com/pages/ajax-javascript/')
#         )
#         return pages

# if __name__ == "__main__":
#     pages = asyncio.run(scrape_multiple_sites())
#     for p in pages:
#         print(p.status, p.url, len(p.body))



# with DynamicSession(capture_xhr=r"https://api\.example\.com/.*", headless=True) as session:
#     page = session.fetch('https://example.com')

#     for xhr in page.captured_xhr:
#         print(xhr.url, xhr.status)
#         print(xhr.body)


# from scrapling.fetchers import DynamicSession, ProxyRotator

# rotator = ProxyRotator([
#     "http://proxy1:8080",
#     "http://proxy2:8080",
#     "http://proxy3:8080",
# ])


# with DynamicSession(proxy_rotator=rotator, headless=True) as session:
#     page1 = session.fetch('https://example1.com')
#     page2 = session.fetch('https://example2.com')

#     page3 = session.fetch('https://example3.com', proxy='http://specific-proxy:8080')

