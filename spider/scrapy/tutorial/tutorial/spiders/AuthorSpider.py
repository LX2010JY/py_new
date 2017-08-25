'''
获取名人名言的 作者信息
'''
import scrapy

class AuthorSpider(scrapy.Spider):
    name = 'author'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self,response):
        #获取作者信息的链接地址，并创建request
        for href in response.css('.author + a::attr(href)'): # 这里的 + 号 代表后一个兄弟元素 ？ I guess
            yield response.follow(href,callback=self.parse_author)
        # 获取下一页
        for a in response.css('li.next a'):
            yield response.follow(a,callback=self.parse)
    # 处理教师页面
    def parse_author(self,response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()
        yield {
            'name' : extract_with_css('h3.author-title::text'),
            'birthdate' : extract_with_css('.author-born-date::text'),
            'bio' : extract_with_css('.author-description::text')
        }
        
        

