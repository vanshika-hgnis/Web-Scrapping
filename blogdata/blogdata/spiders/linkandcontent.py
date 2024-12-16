import scrapy


class LinkandcontentSpider(scrapy.Spider):
    name = "linkandcontent"
    allowed_domains = ["dynodesoft.org"]
    start_urls = ["https://dynodesoft.org/fl/PMSProducts.aspx"]

    def parse(self, response):
        blogs = response.css("div.doctors-detail")
        for blog in blogs:
            link = blog.css("a:has(button.btn-danger)::attr(href)").get()
            if link:
                next_page_url = "https://dynodesoft.org/fl/" + link
                yield response.follow(next_page_url, callback=self.parse_blog_page)

    def parse_blog_page(self, response):
        content = response.css("div.cen_header").get()
        yield {"url": response.url, "content": content}
