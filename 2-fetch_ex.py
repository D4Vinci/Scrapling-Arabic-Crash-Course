from scrapling.fetchers import Fetcher, AsyncFetcher, FetcherSession, ProxyRotator

page = Fetcher.get('https://scrapling.requestcatcher.com/get', impersonate="chrome", stealthy_headers=True)
page = Fetcher.post('https://scrapling.requestcatcher.com/post', data={'key': 'value'})
page = Fetcher.put('https://scrapling.requestcatcher.com/put', data={'key': 'value'})
page = Fetcher.delete('https://scrapling.requestcatcher.com/delete')

# page = await AsyncFetcher.get('https://scrapling.requestcatcher.com/get', impersonate="chrome", stealthy_headers=True)

# page = Fetcher.get('https://example.com/search', params={'q': 'query'}, proxy='http://username:password@localhost:8030')
# page = Fetcher.get('https://example.com', http3=True)
# page = Fetcher.get('https://example.com', headers={'User-Agent': 'Custom/1.0'})
# page = Fetcher.get("https://example.com/login", auth=("my_user", "password123"))


page.status          # HTTP status code
page.reason          # Status message
page.cookies         # Response cookies as a dictionary
page.headers         # Response headers
page.request_headers # Request headers
page.history         # Response history of redirections, if any
page.body            # Raw response body as bytes
page.encoding        # Response encoding
page.meta            # Response metadata dictionary (e.g., proxy used). Mainly helpful with the spiders system.
page.captured_xhr    # List of captured XHR/fetch responses (when capture_xhr is enabled on a browser session)


page = Fetcher.get('https://raw.githubusercontent.com/D4Vinci/Scrapling/main/docs/assets/main_cover.png')
with open(file='main_cover.png', mode='wb') as f:
   f.write(page.body)


###

with FetcherSession(impersonate='chrome', http3=True, stealthy_headers=True, timeout=30, retries=3) as session:
    page1 = session.get('https://scrapling.requestcatcher.com/get')
    page2 = session.post('https://scrapling.requestcatcher.com/post', data={'key': 'value'})
    page3 = session.get('https://api.github.com/events')


# async with FetcherSession(impersonate='firefox', http3=True) as session:
#     response = await session.get('https://example.com')
#     response = await session.post('https://scrapling.requestcatcher.com/post', json={'data': 'value'})
#     response = await session.put('https://scrapling.requestcatcher.com/put', data={'update': 'info'})
#     response = await session.delete('https://scrapling.requestcatcher.com/delete')



###

from scrapling.fetchers import FetcherSession, ProxyRotator

rotator = ProxyRotator([
    'http://proxy1:8080',
    'http://proxy2:8080',
    'http://proxy3:8080',
])

with FetcherSession(proxy_rotator=rotator, impersonate='chrome') as session:
    # Each request automatically uses the next proxy in rotation
    page1 = session.get('https://example.com/page1')
    page2 = session.get('https://example.com/page2')

    # You can check which proxy was used via the response metadata
    print(page1.meta['proxy'])