# import scrapy
# import json
# import os
# import datetime
# from datetime import timezone

# list = []


# class BookingHotelDetailsSpider(scrapy.Spider):
#     name = "booking_hotel_details"
#     allowed_domains = ["www.booking.com"]

#     def start_requests(self):
#         # Initialize a start date
#         start_date = datetime.datetime.now(timezone.utc)

#         # Define the number of days to scrape
#         num_days = 90

#         for k in range(num_days):
#             checkin = (start_date + datetime.timedelta(days=k)
#                        ).strftime("%Y-%m-%d")
#             checkout = (start_date + datetime.timedelta(days=k+1)
#                         ).strftime("%Y-%m-%d")
#             url = f"https://www.booking.com/hotel/in/the-elite-hyderabad.html?&checkin={checkin}&checkout={checkout}&group_adults=2&group_children=0"
#             yield scrapy.Request(url, callback=self.parse, meta={'checkin': checkin, 'checkout': checkout})

#     def parse(self, response):
#         checkin = response.meta['checkin']
#         checkout = response.meta['checkout']


#         if initial_state := response.xpath('//script[contains(., "b_rooms_available_and_soldout:")]/text()').extract_first():
#             start_index = initial_state.find('b_rooms_available_and_soldout:')
#             end_index = initial_state.find('b_photo_pid')

#             if start_index != -1 and end_index != -1:
#                 start_index += len('b_rooms_available_and_soldout:')
#                 data = initial_state[start_index:end_index].strip().rstrip(',')

#                 # Parse the JSON data
#                 parsed_data = json.loads(data)

#                 for element in parsed_data:
#                     for room_option in element['b_blocks']:
#                         if room_option['b_max_persons'] == 2:
#                             for stay_price in room_option['b_stay_prices']:
#                                 if stay_price['b_stays'] == 1:
#                                     room_plan = room_option['b_mealplan_included_name']
#                                     if room_plan == "full_board":
#                                         r_plan = 'AP'
#                                     elif room_plan == "half_board":
#                                         r_plan = 'MAP'
#                                     elif room_plan == "breakfast":
#                                         r_plan = 'CP'
#                                     else:
#                                         r_plan = 'EP'

                                    


#                                     hotel_name = response.css(
#                                         '.pp-header__title::text').get(default='').strip()
#                                     hotel_ratings = response.css(
#                                         '.abf093bdfe f45d8e4c32 d935416c47').get(default='').strip()
                                  

#                                     rates = {
#                                         'OTA_PId': int((str(element['b_blocks'][0]['b_block_id'])).split("_")[1]),
#                                         'Room_ID': int(element['b_id']),
#                                         'Hotel_Name': hotel_name,
#                                         'Hotel_Ratings': hotel_ratings,
#                                         'Check_In': datetime.datetime.strptime(checkin, "%Y-%m-%d").isoformat(),
#                                         'Check_Out': datetime.datetime.strptime(checkout, "%Y-%m-%d").isoformat(),
#                                         'Room_Name': element['b_name'],
#                                         'Room_Plan': r_plan,
#                                         'Price': int(stay_price['b_price'].replace("\xa0", " ").split(' ')[1].replace(",", ""))

#                                     }

#                                     list.append(rates)

#                     # Print the extracted information for all data elements
#                     final_data = {
#                         "hId": 10018,
#                         "otaId": 3,
#                         "rates": list
#                     }
                    
#                     with open('The_Elite_Hotel_Booking_0811.json', 'w') as json_file:
#                         json.dump(final_data, json_file, indent=4)
