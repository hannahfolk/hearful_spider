import scrapy


class GoProSpider(scrapy.Spider):
    """ This spider scrapes the GoPro Fusion Waterproof Digital Spherical Amazon page for all reviews"""
    name = "gopro"
    start_urls = [
        # Can I directly link to all reviews or do I need to somehow switch urls from the original given url in the assignment?
        "https://www.amazon.com/GoPro-Fusion-Waterproof-Digital-Spherical/product-reviews/B0792MJLNM/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
    ]

    def parse(self, response):
        for review in response.css('div.review'):
            yield {
                "unique_review_id": review.css("div::attr(id)").get(),
                "review_title": review.css("a.review-title span::text").get(),
                "review_date": review.css("span.review-date::text").get(),
                "review_star_rating": review.css("i.review-rating span::text").get(),
                "review_text": review.css("span.review-text span::text").getall()
            }

        next_page = response.css("li.a-last a::attr(href)").get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
