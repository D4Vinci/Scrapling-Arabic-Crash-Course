import asyncio
from scrapling.fetchers import StealthyFetcher, StealthySession, AsyncStealthySession


# page = StealthyFetcher.fetch('https://nopecha.com/demo/cloudflare', solve_cloudflare=True, headless=False)
# page = await StealthyFetcher.async_fetch('https://nopecha.com/demo/cloudflare', solve_cloudflare=True)

# page = StealthyFetcher.fetch(
#     'https://www.doordash.com/',
#     solve_cloudflare=True,
#     block_webrtc=True,
#     hide_canvas=True,
#     allow_webgl=True,
#     google_search=True,
#     real_chrome=True,
#     headless=False,
# )


# from scrapling.fetchers import StealthySession


# with StealthySession(
#     headless=True,
#     real_chrome=True,
#     block_webrtc=True,
#     solve_cloudflare=True
# ) as session:
#     page1 = session.fetch('https://quotes.toscrape.com/js/')
#     page2 = session.fetch('https://books.toscrape.com/')
#     page3 = session.fetch('https://www.scrapethissite.com/pages/ajax-javascript/')


# async def scrape_multiple_sites():
#     async with AsyncStealthySession(
#         real_chrome=True,
#         block_webrtc=True,
#         solve_cloudflare=True,
#         max_pages=3
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

