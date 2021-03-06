import scrapy


class ReviewsSpider(scrapy.Spider):
    """ This spider scrapes the GoPro Fusion Waterproof Digital Spherical Amazon page for all reviews. """
    name = "reviews"
    custom_settings = {
        "COLLECTION_NAME": "reviews",
    }
    start_urls = [
        "https://www.amazon.com/GoPro-Fusion-Waterproof-Digital-Spherical/product-reviews/B0792MJLNM/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
    ]

    def parse(self, response):
        for review in response.css('div.review'):
            yield {
                "unique_review_id": review.css("div::attr(id)").get(),
                "review_title": review.css("a.review-title span::text").get(),
                "review_date": review.css("span.review-date::text").get(),
                "review_star_rating": review.css("i.review-rating span::text").get(),
                "review_text": review.css("span.review-text span::text").getall(),
                # below id is copied from mongoDB collection 'products'
                "product_id": "6021fa56f08cd707597d49d8",
            }

        next_page = response.css("li.a-last a::attr(href)").get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
