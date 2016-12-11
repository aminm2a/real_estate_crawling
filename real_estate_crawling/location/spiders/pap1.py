from __future__ import unicode_literals
# -*- coding: utf-8 -*-
from scrapy.http.request import Request
from location.models import Offer, Source, OfferCategory
import scrapy
import re

class pap1Spider(scrapy.Spider):
    name = "pap1"
    max_price = 800
    start_urls = (
        'http://www.pap.fr/annonce/locations-appartement-paris-75-g439-jusqu-a-{0}-euros-a-partir-de-20-m2'.format(max_price),
    )
    offer_category_id = OfferCategory.objects.filter(name='location')[0].id
    source_id = Source.objects.filter(name='pap')[0].id

    def parse_next_page(self,response):
        try:
            for elmt in response.xpath('.//div[@class="box search-results-item"]'):
                html_id = elmt.xpath('.//a[@data-annonce]/@data-annonce').extract()[0].replace('false','False').replace('true','True')
                offer = Offer.objects.filter(html_id=html_id).distinct()
                if Offer.objects.filter(html_id=html_id).count() == 0:
                    offer = Offer()
                else:
                    offer = offer[0]

                offer.offer_category_id = self.offer_category_id
                offer.source_id = self.source_id
                offer.url = 'http://www.pap.fr' + elmt.xpath(".//div[@class='float-right']/a/@href").extract()[0]
                offer.title = elmt.xpath('.//span[@class="h1"]/text()').extract()[0]
                offer.price = elmt.xpath('.//span[@class="price"]/strong/text()').extract()[0][:-2]
                offer.address = elmt.xpath('.//p[@class="item-description"]/strong/text()').extract()[0]
                yield Request(offer.url, callback=self.parse_one_annonce, meta={'object':offer})

        except UnboundLocalError:
            print "Crawling ended. Exiting..."
            exit()
        n = re.match('.*-(\d+)$',response.url)
        if n:
            page_suiv = response.url[:-len(n.groups()[0])] + str(int(n.groups()[0]) + 1)
        else:
            page_suiv = response.url + '-2'

        yield Request(page_suiv,
                              callback=self.parse_next_page)


    def parse_one_annonce(self, response):
        obj = response.meta['object']
        obj.surface = response.xpath('//p[@class="item-description"]/text()').extract()[0]
        obj.description = response.xpath('//*[contains(text(),"Surface")]/strong/text()').extract()[0][:-3]
        obj.save()
