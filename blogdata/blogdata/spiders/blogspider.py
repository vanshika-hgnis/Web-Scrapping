import scrapy


class BlogspiderSpider(scrapy.Spider):
    name = "blogspider"
    allowed_domains = ["dynodesoft.com"]
    start_urls = ["https://dynodesoft.org/fl/PMSProducts.aspx"]

    def parse(self, response):
        # Extracting all blog links on the main page (https://dynodesoft.org/fl/PMSProducts.aspx)
        blogs = response.css("div.doctors-detail")
        for blog in blogs:
            # Extracting the title, detail, and link from each blog entry on the start page
            title = blog.css("h4::text").get()
            detail = blog.css("p.text4::text").get()
            link = blog.css("a:has(button.btn-danger)::attr(href)").get()

            # Yield the data (for the main page)
            yield {"title": title, "detail": detail, "link": link}

            # Follow the link to the individual blog page if a link is found
            if link:
                next_page_url = "https://dynodesoft.org/fl/" + link
                self.logger.info(
                    f"Following link: {next_page_url}"
                )  # Log the link being followed
                yield response.follow(
                    next_page_url,
                    callback=self.parse_blog_page,
                    cb_kwargs={"title": title, "detail": detail, "link": link},
                )

    def parse_blog_page(self, response, title, detail, link):
        # Extract content from the individual blog page (from div.cen_header)
        content = response.css("div.cen_header").get()

        # Log if content is not found for a particular blog
        if not content:
            self.logger.warning(
                f"Content not found for {response.url}"
            )  # Log missing content

        # Yield the result combining the main page data and individual content
        yield {
            "title": title,
            "detail": detail,
            "link": link,
            "url": response.url,  # URL of the individual blog page
            "content": (
                content if content else "Content not found"
            ),  # Handle missing content gracefully
        }
