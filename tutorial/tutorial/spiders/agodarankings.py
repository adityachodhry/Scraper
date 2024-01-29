# import scrapy,time,json,datetime
# from datetime import timezone 
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys

# class AgodaRankingsSpider(scrapy.Spider):
#     name = "agodarankings"

#     start_urls = ["https://www.agoda.com/search?city=6613&checkIn=2023-11-07&checkOut=2023-11-08"]

#     def __init__(self):
#         self.driver = webdriver.Chrome()

#     def parse(self, response):
#         self.driver.get(response.url)
#         for _ in range(35):
#             self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
#             time.sleep(0.5)

#         self.driver.implicitly_wait(10)
#         rank = 1
#         # Extract hotel information
#         hotel_list = []
#         hotel_elements = self.driver.find_elements(By.CSS_SELECTOR, 'li[data-selenium="hotel-item"]')
#         for hotel_element in hotel_elements:
#             hotel = {}

#             hotel['rank'] = rank
#             try:
#                 hotel['name'] = hotel_element.find_element(By.CSS_SELECTOR, 'h3[data-selenium="hotel-name"]').text
#             except:
#                 hotel['name'] = '-'

#             try :
#                 hotel['otaPId'] = str(hotel_element.get_attribute('data-hotelid'))
#             except :
#                 hotel['otaPId'] = '-'

#             try : 
#                 hotel['starCategory'] = int(((hotel_element.find_element(By.CSS_SELECTOR, 'div[role="img"]')).get_attribute('aria-label'))[:1])
#             except :
#                 hotel['starCategory'] = '-'

#             try:
#                 hotel['userRating'] = float(hotel_element.find_element(By.CSS_SELECTOR, '.ReviewWithDemographic p.kite-js-Typography').text)
#             except:
#                 hotel['userRating'] = '-'

#             try:
#                 # Extract and clean NumberOfRatings
#                 number_of_ratings = hotel_element.find_element(By.CSS_SELECTOR, '.ReviewWithDemographic span:nth-child(2)').text
#                 hotel['numberOfRatings'] = int(number_of_ratings.replace(" reviews", "").replace(",", ""))
#             except:
#                 hotel['numberOfRatings'] = '-'

#             try:
#                 # Extract and clean DiscountedPrice
#                 discounted_price = hotel_element.find_element(By.CSS_SELECTOR, 'div[data-element-name="final-price"] span.PropertyCardPrice__Value').text
#                 hotel['discountedPrice'] = int(discounted_price.replace(",", ""))
#             except:
#                 hotel['discountedPrice'] = '-'

#             hotel_list.append(hotel)
#             rank = rank + 1

#         final_data = {
#                     "timestamp" : str(datetime.datetime.now(timezone.utc)),
#                     "otaId" : 4,
#                     "cityCode" : "CTAMD",
#                     "ranking" : hotel_list[:100]
#                 }
#         with open('Ahmedabad_hotels_agoda_071123.json', 'w', encoding='utf-8') as json_file:
#             json.dump(final_data, json_file, ensure_ascii=False, indent=4)

#         self.log(f'Saved {len(hotel_list)} hotels to hotels.json')
#     def closed(self, reason):
#         self.driver.quit()