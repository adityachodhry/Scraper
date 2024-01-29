# import scrapy, json, time , datetime
# from datetime import timezone
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

# class MmtrankingsSpider(scrapy.Spider):
#     name = "mmtrankings"
#     start_urls = [
#         "https://www.makemytrip.com/hotels/hotel-listing/?checkin=11072023&city=CTHYDERA&checkout=11082023&roomStayQualifier=2e0e"
#         ]

#     def __init__(self):
#         self.driver = webdriver.Chrome()

#     def parse(self, response):
#         self.driver.get(response.url)

#         for _ in range(35):
#             self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
#             time.sleep(0.5)

#         # self.driver.implicitly_wait(10)

#         # Extract hotel information
#         rank = 1
#         hotel_list = []
#         hotel_elements = self.driver.find_elements(By.CSS_SELECTOR, '.listingRowOuter.hotelTileDt')

#         for hotel_element in hotel_elements:
#             hotel = {}

#             hotel['rank'] = rank

#             try:
#                 hotel['name'] = hotel_element.find_element(By.CSS_SELECTOR, '.wordBreak.appendRight10').text
#             except:
#                 hotel['name'] = '-'

#              # Extract the hotel ID from the id attribute
#             try:
#                 img_gallery = hotel_element.find_element(By.CSS_SELECTOR, '.imgGalleryCont')
#                 hotel['otaPId'] = str(img_gallery.get_attribute('id'))
#             except:
#                 hotel['otaPId'] = '-'
                
#             try :
#                 starCategory = hotel_element.find_element(By.CSS_SELECTOR, '#hlistpg_hotel_star_rating')
#                 hotel['starCategory'] = int(starCategory.get_attribute('data-content'))
#             except :
#                 hotel['starCategory'] = '-'

#             try:
#                 hotel['userRating'] = float(hotel_element.find_element(By.CSS_SELECTOR, '#hlistpg_hotel_user_rating').text)
#             except:
#                 hotel['userRating'] = '-'

#             try:
#                 hotel['numberOfRatings'] = int(hotel_element.find_element(By.CSS_SELECTOR, '.darkGreyText#hlistpg_hotel_reviews_count').text)
#             except:
#                 hotel['numberOfRatings'] = '-'

#             try:
#                 discounted_price = hotel_element.find_element(By.CSS_SELECTOR, '#hlistpg_hotel_shown_price').text
#                 hotel['discountedPrice'] = int(discounted_price.split(' ')[1].replace(",", ""))
#             except:
#                 hotel['discountedPrice'] = '-'
            
#             try:
#                location_element = hotel_element.find_element(By.CSS_SELECTOR, '.blueText')
#                hotel['location'] = location_element.text
#             except:
#                 hotel['location'] = '-'
            
#             try:
#                persuasion_element = hotel_element.find_element(By.CSS_SELECTOR, '.persuasion__item.pc__peithoPerNew span')
#                hotel['persuasionText'] = persuasion_element.text
#             except:
#                  hotel['persuasionText'] = '-'


#             hotel_list.append(hotel)
#             rank = rank + 1

#         # Save the hotel_list to a JSON file
#         final_data = {
#             "timestamp": str(datetime.datetime.now(timezone.utc)),
#             "otaId": 1,
#             "cityCode": "CTHYDERA",
#             "ranking": hotel_list[:100]
#         }


#         with open('Hyderabad_hotels_mmt_071123.json', 'w', encoding='utf-8') as json_file:
#             json.dump(final_data, json_file, ensure_ascii=False, indent=4)

#         self.log(f'Saved {len(hotel_list)} hotels to hotels.json')

#     def closed(self, reason):
#         self.driver.quit()
