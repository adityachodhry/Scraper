# import scrapy
# import json
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from datetime import datetime, timezone, timedelta


# class CTRankingsSpider(scrapy.Spider):
#     name = "ctrankings"
#     start_urls = [f"https://www.cleartrip.com/hotels/results?city=Bhopal&chk_in=08%2F01%2F2024&chk_out=09%2F01%2F2024"]

#     def __init__(self):
#         options = webdriver.ChromeOptions()
#         options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
#         self.driver = webdriver.Chrome(options=options)

#     def __init__(self):
#         self.driver = webdriver.Chrome()

#     def parse(self, response):
#         self.driver.get(response.url)

#         # Wait for the content to load
#         WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.sc-kAyceB.ciDZAa')))


#         # Scroll down to load more content
#         for _ in range(35):
#             self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
#             WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, 'div.sc-kAyceB.ciDZAa')))
#             time.sleep(1)  # Additional time to ensure content loads

#         # Extract hotel information
#         rank = 1
#         hotel_list = []
#         hotel_elements = self.driver.find_elements(By.CSS_SELECTOR, 'div.hotel-box')

#         for hotel_element in hotel_elements:
#             hotel = {}

#             hotel['rank'] = rank

#             try:
#                 hotel['name'] = hotel_element.find_element(By.CSS_SELECTOR, 'div.sc-feUZmu.dZmZVk').text
#             except Exception as e:
#                 self.log(f"Error extracting name: {e}")
#                 hotel['name'] = '-'

#             try:
#                 user_rating_element = hotel_element.find_element(By.CSS_SELECTOR, 'div.sc-aXZVg.bGZzaE.p.sc-gEvEer.lmJiPO.ml-1')
#                 hotel['userRating'] = float(user_rating_element.text)
#             except:
#                 hotel['userRating'] = '-'

#             try:
#                 number_of_ratings_element = hotel_element.find_element(By.CSS_SELECTOR, 'div.sc-kAyceB.loSoiz.mt-1 div.sc-feUZmu.kfqyCH')
#                 hotel['numberOfRatings'] = int(number_of_ratings_element.text)
#             except:
#                 hotel['numberOfRatings'] = '-'

#             try:
#                 discounted_price = hotel_element.find_element(By.CSS_SELECTOR, 'div.sc-aXZVg.ljlsKL.p.sc-gEvEer.fnSGpU').text
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

#         with open('Adita_Data.json', 'w', encoding='utf-8') as json_file:
#             json.dump(final_data, json_file, ensure_ascii=False, indent=4)

#         self.log(f'Saved {len(hotel_list)} Adita_Data.json')

#     def closed(self, reason):
#         self.driver.quit()
