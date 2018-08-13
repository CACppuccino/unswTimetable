import scrapy

class UnswSpider(scrapy.Spider):
    name = 'unsw'

    def start_requests(self):
        urls = [
            'http://timetable.unsw.edu.au/2018/subjectSearch.html'        
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        ael = response.xpath('///a[@href]')
        shortL = []
        urlL = []
        headURL = 'http://timetable.unsw.edu.au/2018/'
        # get all courses' short name
        for x in range(len(ael)):
            if ael[x].xpath('text()').extract() and len(ael[x].xpath('text()').extract()[0]) == 4:
                shortL.append(ael[x].xpath('text()').extract()[0])
                urlL.append(headURL + ael[x].xpath('@href').extract()[0])
                
