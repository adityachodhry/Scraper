# import scrapy
# import json
# import os
# import datetime
# from datetime import timezone

# my_list = []
# hotel_id = '5e45600b2b0a5f10a4dede2a'

# class HappyEasyGoHotelDetailsSpider(scrapy.Spider):
#     name = "Go_hotel_details"
#     allowed_domains = ["www.happyeasygo.com"]

#     def start_requests(self):
#         # Initialize a start date
#         start_date = datetime.datetime.now(timezone.utc)

#         # Define the number of days to scrape
#         num_days = 90

#         for k in range(num_days):
#             # checkin = (start_date + datetime.timedelta(days=k)).strftime("%Y-%m-%d")
#             # checkout = (start_date + datetime.timedelta(days=k+1)).strftime("%Y-%m-%d")
#             # url = f"https://hotel.happyeasygo.com/hotels/bhopal/hotel_{hotel_id}/{checkin}_{checkout}/2-0"

#             url = "https://hotel.happyeasygo.com/hotels/bhopal/hotel_5e45600b2b0a5f10a4dede2a/2024-01-16_2024-01-17/2-0?source_from=happyeasygo"
#             yield scrapy.Request(url, callback=self.parse)
#             # yield scrapy.Request(url, callback=self.parse, meta={'checkin': checkin, 'checkout': checkout})


#     def parse(self, response):
#         # checkin = response.meta['checkin']
#         # checkout = response.meta['checkout']

#         # Sample code (modify as per the actual HTML structure):
#         hotel_name = response.css('div.hotel h1.hotel-name::text').get()
#         print(hotel_name)

#         # hotel_ratings = response.css('.hotel-ratings::text').get(default='').strip()
#         # print(hotel_ratings)

#         # hotel_review = response.css('div.num span.review-number::text').get(default='').strip()
#         # print(hotel_review)

#         # for room_option in response.css('div.rateplan-item-container'):
#         #     # Extract room details
#         #     room_name = room_option.css('div.room-title.flex::text').get(default='').strip()
#         #     print(room_name)

#         #     price = room_option.css('div.current::text').get(default='').strip()
#         #     print(price)

#         #     room_plan = room_option.css('div.rateplan-meals::text').get(default='').strip()

#         #     if "Free" in room_plan and "Lunch" in room_plan and "Dinner" in room_plan:
#         #         mealPlan = "AP"
#         #     elif "Free" in room_plan and ("Lunch" in room_plan or "Dinner" in room_plan):
#         #         mealPlan = "MAP"
#         #     elif "Free Breakfast" in room_plan:
#         #         mealPlan = "CP"
#         #     else:
#         #         mealPlan = "EP"

#         #     print(mealPlan)

#         #     rates = {
#         #         'Hotel_Name': hotel_name,
#         #         'Hotel_Ratings': hotel_ratings,
#         #         'Hotel_Review': hotel_review,
#         #         'Check_In': datetime.datetime.strptime(checkin, "%Y-%m-%d").isoformat(),
#         #         'Check_Out': datetime.datetime.strptime(checkout, "%Y-%m-%d").isoformat(),
#         #         'Room_Name': room_name,
#         #         'Room_Plan': mealPlan,
#         #         'Price': price
#         #     }

#         #     my_list.append(rates)

#         # # Save the data to a JSON file
#         # final_data = {
#         #     "hId": 10018,
#         #     "otaId": 7,
#         #     "rates": my_list
#         # }

#         # with open('HappyEasyGo_Hotel_Booking.json', 'w') as json_file:
#         #     json.dump(final_data, json_file, indent=4)
