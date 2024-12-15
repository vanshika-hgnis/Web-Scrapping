import scrapy


class LinkextractorSpider(scrapy.Spider):
    name = "linkextractor"
    allowed_domains = ["dynodesoft.org"]
    start_urls = ["https://dynodesoft.org/fl/PMSProducts.aspx"]

    def parse(self, response):
        blogs = response.css("div.doctors-detail")
        for blog in blogs:
            title = blog.css("h4::text").get()
            detail = blog.css("p.text4::text").get()
            link = blog.css("a:has(button.btn-danger)::attr(href)").get()

            # Yield the data (for the main page) and the extracted link for the next spider
            if link:
                next_page_url = "https://dynodesoft.org/fl/" + link
                yield {"title": title, "detail": detail, "link": next_page_url}
