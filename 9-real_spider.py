# -*- coding: utf-8 -*-
from copy import deepcopy

from scrapling.spiders import Spider, Request


class DisplayCentreSpider(Spider):
    name = 'displaycentre_spider'
    allowed_domains = {'displaycentre.co.uk'}
    start_urls = ['https://displaycentre.co.uk/shop/']
    development_mode = True

    async def parse(self, response):
        categories = response.css('.wd-promo-banner-link::attr(href)').getall()
        pages = response.css('a.page-numbers::attr(href)').getall()
        for url in (categories + pages):
            yield Request(response.urljoin(url))

        for product in response.css('a[href*="/product/"]::attr(href)').getall():
            yield Request(response.urljoin(product), callback=self.parse_product)

    async def parse_product(self, response):
        schema = response.css('[type="application/ld+json"]:contains("Product")::text').get().json()
        main_name = schema['name']
        og_item = dict()
        og_item['category'] = response.css('.yoast-breadcrumb a::text').extract()[1:]
        og_item['image_url'] = schema.get('image') or ''
        og_item['url'] = response.url
        og_item['brand'] = 'The Display Centre'

        for offer in schema['offers']:
            item = deepcopy(og_item)
            item['name'] = main_name
            item['sku'] = schema.get('mpn') or offer.get('mpn') or schema.get('sku')
            item['identifier'] = schema['sku']
            prices = offer.get('priceSpecification') or []
            old_price = None
            if len(prices) > 1:
                price = float(min(prices, key=lambda x: float(x['price']))['price'])
                old_price = float(max(prices, key=lambda x: float(x['price']))['price'])
            else:
                price = float(prices[0]['price'] if prices else offer.get('lowPrice', 0))

            item['price'] = price
            item['instock'] = True if 'InStock' in offer.get('availability', 'InStock') else False
            item['shipping_cost'] = 0 if price > 200 else 11.95
            if old_price:
                item['old_price'] = old_price
            yield item


if __name__ == "__main__":
    result = DisplayCentreSpider().start(use_uvloop=True)
    result.items.to_json("products.json", indent=True)
