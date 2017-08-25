'''
获取所有的名人名言
'''
# run command  scrapy crawl quotes
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    def start_requests(self):
        '''
        必须返回一个可迭代request对象,这里是发起请求最初的地方
        '''
        urls = [
            'http://quotes.toscrape.com/page/1/',
        ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    def parse(self,response):
        for quote in response.css('div.quote'):
            # 生成器循环到这儿 ，输出一个dict
            yield {
                'text' : quote.css('span.text::text').extract_first(),
                'author' : quote.css('small.author::text').extract_first(),
                'tags' : quote.css('div.tags a.tag::text').extract()
            }
        next_page = response.css('li.next a::attr(href)').extract_first()
        # following links  我理解为 追加链接
        if next_page is not None:
            #yield response.follow(next_page,callback=self.parse)  #这里的next_page可以直接使用相对地址
            
            next_page = response.urljoin(next_page)  # 建立绝对路径，这里不用在意你当前请求页面url是什么，它只取域名，不取后面的路径进行 合并
            # 生成器循环到这儿，没有输出，但创建一次request请求
            yield scrapy.Request(next_page,callback = self.parse)
