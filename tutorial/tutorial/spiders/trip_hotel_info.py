# import scrapy
# import json
# import os
# import datetime
# from datetime import timezone
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

# data_list = []
# hotel_id = '2237731'

# class BookingHotelDetailsSpider(scrapy.Spider):
#     name = "trip_hotel_data"
#     allowed_domains = ["www.trip.com"]

#     def start_requests(self):
#         # Initialize a start date
#         start_date = datetime.datetime.now(timezone.utc)

#         # Define the number of days to scrape
#         num_days = 30

#         for k in range(num_days):
#             checkin = (start_date + datetime.timedelta(days=k)
#                        ).strftime("%Y-%m-%d")
#             checkout = (start_date + datetime.timedelta(days=k+1)
#                         ).strftime("%Y-%m-%d")
#             url = f"https://www.trip.com/hotels/detail/?&hotelId={hotel_id}&checkIn={checkin}&checkOut={checkout}&adult=2&children=0&&curr=INR"
#             yield scrapy.Request(url, callback=self.parse, meta={'checkin': checkin, 'checkout': checkout})

#     def parse(self, response):
#         checkin = response.meta['checkin']
#         checkout = response.meta['checkout']

#         hotel_name = response.css('div.detail-headline-v8_title h1.detail-headline-v8_name::text').get(default='').strip()
#         print(hotel_name)
#         hotel_ratings = response.css('span.detail-headreview-ab_score_box b.detail-headreview-ab_score_value::text').get(default='').strip()
#         print(hotel_ratings)

#         # Extracting room information
#         room_elements = response.css('div.room-card-item ')

#         for room_element in room_elements:
#             room_name = room_element.css('div.room-head span.room-name::text').get(default='').strip()

#             room_plan = room_element.css('div.sale-card div.meal-item::text').get(default='').strip()

#             room_rates = room_element.css('div.price-box div.price-real::text').get(default='').strip()

#             mealPlan = ""
#             if "Breakfasts" in room_plan and "dinner" in room_plan and "lunch" in room_plan and "included" in room_plan and not ("not" in room_plan):
#                 mealPlan = "AP"
#             elif "Breakfasts" in room_plan and "dinner" in room_plan or "lunch" in room_plan and "included" in room_plan:
#                 mealPlan = "MAP"
#             elif "included 1 Breakfasts" in room_plan and "included 2 Breakfasts" in room_plan:
#                 mealPlan = "CP"
#             else:
#                 mealPlan = "EP"

#             room_info = {
#                 'Hotel_Id': hotel_id,
#                 'Hotel_Name': hotel_name,
#                 'Check_In': datetime.datetime.strptime(checkin, "%Y-%m-%d").isoformat(),
#                 'Check_Out': datetime.datetime.strptime(checkout, "%Y-%m-%d").isoformat(),
#                 'Room_Name': room_name,
#                 'Room_Plan': mealPlan,
#                 'Room_Rates': room_rates,
#                 'Room_Plan_Description': room_plan
#             }

#             data_list.append(room_info)

#         # Move this block outside the parse method to avoid overwriting the file for each room
#         with open('Trip.json', 'w') as json_file:
#             json.dump(data_list, json_file, indent=4)
