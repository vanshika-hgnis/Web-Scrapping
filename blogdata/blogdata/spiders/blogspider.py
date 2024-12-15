import scrapy


class BlogspiderSpider(scrapy.Spider):
    name = "blogspider"
    allowed_domains = ["www.dynodesoft.com"]
    start_urls = ["https://dynodesoft.org/fl/PMSProducts.aspx"]

    def parse(self, response):
        blogs = response.css("div.doctors-detail")
        for blog in blogs:
            yield {
                "title": blog.css("h4::text").get(),
                "detail": blog.css("p.text4::text").get(),
                "links": blog.css("a:has(button)::attr(href)").get(),
            }
