import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        hrefs = response.css(
            '#numerical-index'
        ).css('tbody').css('tr').css('a::attr(href)').getall()
        for href in hrefs:
            yield response.follow(href, callback=self.parse_pep)

    def parse_pep(self, pep):
        number, name = pep.css('h1.page-title::text').get().split(' – ')
        yield PepParseItem(
            status=pep.css('abbr::text').getall()[0],
            name=name,
            number=number.replace('PEP ', ''),
        )
