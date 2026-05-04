import re
from scrapling.parser import Selector

with open('html_doc.html') as f:
    html_doc = f.read()


page = Selector(html_doc)

# print(page.get_all_text())

# print(page.css('section'))
# print(page.xpath('//section'))
# print(page.xpath('//section').length == len(page.xpath('//section')))

# print(page.css('section ::text').get())
# for i in page.css('section div ::text').getall():
#     if i.clean():
#         print(i.clean())

section_element = page.find('section')
# print(section_element)
# print(page.find_all('section'))
# print(page.find_all('section', {'id':"products"}))
# print(page.find_all('section', id="products"))
# print(page.find_all('h3', re.compile(r'Product \d')))

# print(page.find_by_text('Products', first_match=False))

# print(page.find_by_regex(r'Product \d', first_match=False))

if section_element:
    print(section_element.tag)
    print(section_element.attrib)
    print(section_element.text)
    print(section_element.get_all_text())
    print(section_element.generate_full_css_selector)
    print(section_element.parent)
    print(section_element.children)
    print(section_element.siblings)
    print(section_element.children.css('h2::text').getall())
