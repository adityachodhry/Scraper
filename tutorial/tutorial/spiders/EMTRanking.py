# import scrapy
# import json
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from datetime import datetime, timezone

# city_name = 'Bhopal'


# class MmtrankingsSpider(scrapy.Spider):
#     name = "emtrankings"
#     start_urls = [f"https://www.easemytrip.com/hotels/hotels-in-{city_name}/?city={city_name}&cin=05/01/2024&cOut=06/01/2024&Hotel=NA&Rooms=1&pax=2"]

#     def __init__(self):
#         self.driver = webdriver.Chrome()

#     def parse(self, response):
#         self.driver.get(response.url)

#         # Wait for the content to load (adjust the timeout as needed)
#         WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.result-item.mrel')))

#         # Scroll down to load more content (if necessary)
#         for _ in range(35):
#             self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
#             time.sleep(0.5)

#         # Extract hotel information
#         rank = 1
#         hotel_list = []
#         hotel_elements = self.driver.find_elements(By.CSS_SELECTOR, '.result-item.mrel')

#         for hotel_element in hotel_elements:
#             hotel = {}

#             hotel['rank'] = rank

#             try:
#                 hotel['name'] = hotel_element.find_element(By.CSS_SELECTOR, '.htl_ttl').text
#             except Exception as e:
#                 self.log(f"Error extracting name: {e}")
#                 hotel['name'] = '-'

#             try :
#                 star_category_element = hotel_element.find_element(By.CSS_SELECTOR, '.star-rating span.starImg')
#                 star_icons = star_category_element.find_elements(By.TAG_NAME, 'img')
#                 hotel['starCategory'] = len(star_icons)
#             except :
#                 hotel['starCategory'] = '-'

#             try:
#                 user_rating_element = hotel_element.find_element(By.CSS_SELECTOR, '.review-bg-g.ng-binding.ng-scope')
#                 hotel['userRating'] = float(user_rating_element.text)
#             except:
#                 hotel['userRating'] = '-'
            
#             try:
#                 number_of_ratings_element = hotel_element.find_element(By.CSS_SELECTOR, '.Review-Section-count.ng-scope span.ng-binding')
#                 hotel['numberOfRatings'] = int(number_of_ratings_element.text)
#             except:
#                 hotel['numberOfRatings'] = '-'

#             try:
#                 discounted_price = hotel_element.find_element(By.CSS_SELECTOR, '.act_price span.ng-binding').text
#                 hotel['discountedPrice'] = int(discounted_price)
#             except:
#                 hotel['discountedPrice'] = '-'



#             hotel_list.append(hotel)
#             rank += 1

#         # Save the hotel_list to a JSON file
#         final_data = {
#             "timestamp": str(datetime.now(timezone.utc)),
#             "otaId": 5,
#             "ranking": hotel_list[:100]
#         }

#         with open('Ease_My_Trip_Ranking.json', 'w', encoding='utf-8') as json_file:
#             json.dump(final_data, json_file, ensure_ascii=False, indent=4)

#         self.log(f'Saved {len(hotel_list)} hotels to Ease_My_Trip_Ranking.json')

#     def closed(self, reason):
#         self.driver.quit()