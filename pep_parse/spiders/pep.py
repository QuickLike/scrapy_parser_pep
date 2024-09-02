import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        trs = response.css('#numerical-index').css('tbody').css('tr')
        for tr in trs:
            pep_url = tr.css('a::attr(href)').get()
            yield response.follow(pep_url, callback=self.parse_pep)

    def parse_pep(self, pep):
        number, name = pep.css('h1.page-title::text').get().split(' – ')
        data = {
            'status': pep.css('abbr::text').getall()[0],
            'name': name,
            'number': number.replace('PEP ', ''),
        }
        yield PepParseItem(data)
