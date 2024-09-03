import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        for href in response.css(
                '#numerical-index table tbody tr a::attr(href)'
        ).getall():
            yield response.follow(href, callback=self.parse_pep)

    def parse_pep(self, pep):
        title = pep.css('h1.page-title::text').get()
        number, name = title.split(' – ', 1)
        yield PepParseItem(
            status=pep.css('abbr::text').getall()[0],
            name=name,
            number=number.replace('PEP ', ''),
        )
