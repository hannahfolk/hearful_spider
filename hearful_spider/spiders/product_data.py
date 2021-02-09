import scrapy


class ProductDataSpider(scrapy.Spider):
    """ This spider scrapes the GoPro Fusion Waterproof Digital Spherical Amazon page for pertinent product information. """
    name = "product_data"
    custom_settings = {
        "COLLECTION_NAME": "products",
    }
    start_urls = [
        "https://www.amazon.com/GoPro-Fusion-Waterproof-Digital-Spherical/dp/B0792MJLNM/ref=sr_1_3?crid=D3C7EDM435E7&keywords=gopro+fusion&qid=1550442454&s=electronics&sprefix=GoPro+Fu%2Celectronics%2C1332&sr=1-3",
        # "https://www.amazon.com/gp/product/B085DVTYHN?pf_rd_r=VW0NY16VCN84DZXZ0285&pf_rd_p=5ae2c7f8-e0c6-4f35-9071-dc3240e894a8&pd_rd_r=f3ce7385-fdb9-4260-8efb-5befe820f0cd&pd_rd_w=A7vOx&pd_rd_wg=YUNGh&ref_=pd_gw_unk"
    ]

    def parse(self, response):
        msrp = response.css("span#priceblock_ourprice::text").get()

        specs = []
        for spec in response.css("div#feature-bullets ul li span.a-list-item::text").getall():
            if spec.strip() != "":
                specs.append(spec.strip())

        if msrp is None:
            msrp = response.css(
                "div#price span.priceBlockStrikePriceString::text").get()
            sale_price = response.css(
                "div#price span#priceblock_pospromoprice::text").get()
            yield {
                "product_name": response.css("span#productTitle::text").get().strip(),
                "brand": response.css("div#productOverview_feature_div td.a-span9 span.a-size-base::text").get(),
                "source": "Amazon",
                "list_price": msrp,
                "sale_price": sale_price,
                "description": specs,
                "star_rating": response.css("span.a-icon-alt::text").get(),
                "total_num_reviews": response.css("span#acrCustomerReviewText::text").get(),
            }
        else:
            yield {
                "product_name": response.css("span#productTitle::text").get().strip(),
                "brand": response.css("div#productOverview_feature_div td.a-span9 span.a-size-base::text").get(),
                "source": "Amazon",
                "list_price": msrp,
                "description": specs,
                "star_rating": response.css("span.a-icon-alt::text").get(),
                "total_num_reviews": response.css("span#acrCustomerReviewText::text").get(),
            }
