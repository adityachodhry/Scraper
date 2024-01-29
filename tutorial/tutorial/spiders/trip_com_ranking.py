# import scrapy
# import json
# import time
# import datetime
# from datetime import timezone
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

# class trip_rankingsSpider(scrapy.Spider):
#     name = "trip_rankings"
#     start_urls = [
#         f"https://www.trip.com/hotels/list?city=60045&checkin=2024/01/15&checkout=2024/01/16&barCurr=INR&crn=1&adult=2&children=0"]

#     def __init__(self):
#         self.driver = webdriver.Chrome()

#     def parse(self, response):
#         self.driver.get(response.url)

#         try:
#             for _ in range(35):
#                 self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
#                 time.sleep(1)

#             # Extract hotel information
#             rank = 1
#             hotel_list = []
#             hotel_elements = self.driver.find_elements(By.CSS_SELECTOR, 'div.with-decorator')

#             for hotel_element in hotel_elements:
#                 hotel = {}
#                 hotel['rank'] = rank

#                 try:
#                     hotel['name'] = hotel_element.find_element(By.CSS_SELECTOR, 'div.list-card-tagAnd span.name').text
#                 except Exception as e:
#                     self.log(f"Failed to extract hotel name: {str(e)}")
#                     hotel['name'] = '-'

#                 try:
#                     img_gallery = hotel_element.find_element(By.CSS_SELECTOR, 'div.compressmeta')
#                     hotel['otaPId'] = str(img_gallery.get_attribute('id'))
#                 except Exception as e:
#                     self.log(f"Failed to extract OTA product ID: {str(e)}")
#                     hotel['otaPId'] = '-'

#                 try:
#                     starCategory = hotel_element.find_element(By.CSS_SELECTOR, 'div.list-card-tagAnd div.more-star-repeat')
#                     hotel['starCategory'] = int(starCategory.get_attribute('data-content'))
#                 except Exception as e:
#                     self.log(f"Failed to extract star category: {str(e)}")
#                     hotel['starCategory'] = '-'

#                 try:
#                     hotel['userRating'] = float(hotel_element.find_element(By.CSS_SELECTOR, 'section.list-card-comment div.score div.real').text)
#                 except Exception as e:
#                     self.log(f"Failed to extract user rating: {str(e)}")
#                     hotel['userRating'] = '-'

#                 try:
#                     hotel['numberOfRatings'] = int(hotel_element.find_element(By.CSS_SELECTOR, 'section.list-card-comment div.count').text)
#                 except Exception as e:
#                     self.log(f"Failed to extract number of ratings: {str(e)}")
#                     hotel['numberOfRatings'] = '-'

#                 try:
#                     discounted_price = hotel_element.find_element(By.CSS_SELECTOR, 'div.whole div.real labelColor[id*="meta-real-price"]').text
#                     hotel['discountedPrice'] = int(discounted_price.split(' ')[1].replace(",", ""))
#                 except Exception as e:
#                     self.log(f"Failed to extract discounted price: {str(e)}")
#                     hotel['discountedPrice'] = '-'

#                 hotel_list.append(hotel)
#                 rank += 1

#             # Save the hotel_list to a JSON file
#             final_data = {
#                 "timestamp": str(datetime.datetime.now(timezone.utc)),
#                 "otaId": 6,
#                 "ranking": hotel_list[:100]
#             }

#             with open('Trip_Ranking.json', 'w', encoding='utf-8') as json_file:
#                 json.dump(final_data, json_file, ensure_ascii=False, indent=4)

#             self.log(f'Saved {len(hotel_list)} hotels to Trip_Ranking.json')

#         except Exception as e:
#             self.log(f"Error in parsing: {str(e)}")

#     def closed(self, reason):
#         self.driver.quit()
