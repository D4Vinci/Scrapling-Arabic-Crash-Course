from scrapling import Fetcher

selector = '#hmenus > div:nth-child(1) > ul > li:nth-child(1) > a'
old_url = "https://web.archive.org/web/20100102003420/http://stackoverflow.com/"
new_url = "https://stackoverflow.com/"

Fetcher.configure(adaptive = True, adaptive_domain='stackoverflow.com')

page = Fetcher.get(old_url, timeout=30)
element1 = page.css(selector, auto_save=True)[0]

# Same selector but used in the updated website
page = Fetcher.get(new_url)
element2 = page.css(selector, adaptive=True)[0]

if element1.text == element2.text:
    print('Scrapling found the same element in the old and new designs!')