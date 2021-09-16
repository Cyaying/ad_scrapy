import scrapy
from ad_scrapy.items import AdScrapyItem


class CrawlArticleSpider(scrapy.Spider):
    name = 'crawl_article'
    start_urls = ['https://www.adc.org.cn/index.php?m=article&f=browse&t=mhtml&categoryID=15']
    model_urls = []
    detail_url = ''

    def parse(self, response):
        """
        function: 解析各板块的内容
        """
        li_list = response.xpath('//*[@id="block6"]/div[2]/ul/li')
        a_list = [0, 6, 8, 9, 1, 4]
        for idx in a_list:
            model_url = 'https://www.adc.org.cn' + li_list[idx].xpath('./a/@href').extract_first()
            self.model_urls.append(model_url)
        for idx, url in enumerate(self.model_urls):
            yield scrapy.Request(url=url, callback=self.parse_model)

    def parse_model(self, response):
        """
        function: 解析各板块详情页的内容
        """
        div_list = response.xpath('//*[@id="articles"]/div')
        category = response.xpath('/html/body/div[2]/div[2]/div/ul/li[2]/a/text()').extract_first()
        for div in div_list:
            title = div.xpath('./div[@class="item-heading"]/h4/a/text()').extract_first()
            abstract = div.xpath('./div[@class="item-content"]/div/text()').extract_first()
            self.detail_url = 'https://www.adc.org.cn' + div.xpath('./div[@class="item-heading"]/h4/a/@href').extract_first()
            move = dict.fromkeys((ord(c) for c in u"\xa0\n\t' '"))
            abstract = abstract.translate(move)
            item = AdScrapyItem()
            item['category'] = category
            item['title'] = title
            item['abstract'] = abstract
            item['url'] = self.detail_url
            yield scrapy.Request(url=self.detail_url, callback=self.parse_detail, meta={'item': item})

    def parse_detail(self, response):
        """
        function: 解析文章详情页内容
        """
        views = response.xpath('//*[@id="article"]/header/dl/dd[3]/span').extract_first()
        if views == None:
            views = '0'
        else:
            views = views.split('</i>')[-1]
            views = "".join(list(filter(str.isdigit, views)))
        item = response.meta['item']
        item['nickname'] = "AD秘书处"
        item['views'] = views
        print('******** ', item['url'], '... ********')
        yield item
