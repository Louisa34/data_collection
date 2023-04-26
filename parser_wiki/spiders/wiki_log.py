import scrapy
from scrapy import FormRequest
from scrapy.http import HtmlResponse
import json
import re
#from logging import log
#from scrapy.http import Request

class WikiLogSpider(scrapy.Spider):
    name = "wiki_log"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/"]
    wiki_login_link = "https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Main+Page"
    wiki_login = 'Siera Ja'
    wiki_pwd = 'qwerasdf_1'

    def parse(self, response: HtmlResponse):
        csrf_token = self.fetch_csrf_token(response.text)
        print('next_saveing')
        with open("response_1.txt", "w", encoding="utf-8") as self.f:
            self.f.write(response.text)
        
        yield FormRequest(
            self.wiki_login_link,
            method='POST',
            callback=self.after_login,
            formdata={'wpName1': self.wiki_login, 'wpPassword1': self.wiki_pwd, 'authAction':'login'},
            headers={'csrfToken': csrf_token}
        )

    def after_login(self, response):
        greeting = response.xpath("//h1[@class='firstHeading mw-first-heading']/text()").get()
        print(greeting)

    def fetch_csrf_token(self, text):  
        """ Get csrf-token for auth """
        matched = re.search(r'\"csrfToken\":\"\w+', text).group()
        return matched.split(':').pop().replace(r'"', '')
    








'''

["https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Main+Page"]

    def parse(self, response):
        #csrf_token = 'Rq7Mdb2ij8tByCPEJQIW6Xei+4Aaw0Yo4c5zTlCQPoif9jRFUhEdY5aCVeHjRgXd9x1cWd+hj8/m1pPzp7x8pQ=='
        yield FormRequest(
            "https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Main+Page",
            #formxpath="//div[@id='userloginForm']/form",
            #formid='login-form',
            method='POST',
            formdata={
            #'csrf_token':csrf_token, 
            #'wpLoginToken':'bdb9b0dde3fa388dd09c9918b5ff399c64401bd2',                    
            'username':'Siera Ja',
            'password':'qwerasdf_1',
            #'Token': '7457be6d6f42a5ef8e277af8323b4043643e934c', 
            #'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39',
            #'cookie':'GeoIP=GB:ENG:London:51.52:-0.09:v4; ruwikimwuser-sessionId=47bbb278f1016f2846b2; ruwikiss0-UserName=Siera%20Ja; ruwikiUserName=Siera%20Ja; WMF-Last-Access=18-Apr-2023; WMF-Last-Access-Global=18-Apr-2023; WMF-DP=670; ruwikiwmE-sessionTickLastTickTime=1681823702301; ruwikiwmE-sessionTickTickCount=13; ss0-ruwikiSession=ksjuebu02lum143mh5qn9cqcenc5n18n; ruwikiSession=ksjuebu02lum143mh5qn9cqcenc5n18n; ruwikiss0-UserID=3385240; ruwikiUserID=3385240; centralauth_ss0-User=Siera%20Ja; centralauth_User=Siera%20Ja; loginnotify_prevlogins=2023-fmonb7-iea8lvvu0w2y9gksk9ba54pinr5y0h2; cpPosIndex=1%401681823745%237501a4cf90dd8e5eca4a5bd23684ee81; UseDC=master; UseCDNCache=false; ss0-centralauth_Session=e9f26481e1243468a006be43b61ce658; centralauth_Session=e9f26481e1243468a006be43b61ce658'
            },
            callback=self.after_login
        )

    def after_login(self, response):
        greeting = response.xpath("//h1[@class='firstHeading mw-first-heading']/text()").get()
        print(greeting)
        # check login succeed before going on
        #if "authentication failed" in response.text:
        #    self.log("Login failed", level=log.ERROR)
        #else:
           # return Request(url="https://ru.wikipedia.org/w/index.php?title=%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%8F%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0&namespace=-1&source=specialconfirmemail",
                #callback=self.parse_viki)
                      

    def parse_viki(self,response):
        greeting = response.xpath("//h1[@class='firstHeading mw-first-heading']/text()").get()
        #scroller_item = response.xpath("//div[@class='gb-main-scroller__item']")
        print(greeting)
        #print(f'Scrapy crawled {len(scroller_item)} scroller items')
'''