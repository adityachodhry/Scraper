# import scrapy
# import json
# from datetime import datetime, timedelta

# data_list = []

# hotelid = '707622'

# class RoomItem(scrapy.Item):
#     CheckIn = scrapy.Field()
#     CheckOut = scrapy.Field()
#     RoomName = scrapy.Field()
#     Price = scrapy.Field()


# class CtspiderSpider(scrapy.Spider):
#     name = "ctspider"
#     allowed_domains = ["www.cleartrip.com"]
    
#     def start_requests(self):
#         start_date = datetime.now().date()
#         num_days = 5

#         for k in range(num_days):
#             checkin = (start_date + timedelta(days=k)).strftime("%m/%d/%Y")
#             checkout = (start_date + timedelta(days=k+1)).strftime("%m/%d/%Y")
#             url = f"https://www.cleartrip.com/hotels/details/{hotelid}?c={checkin}|{checkout}&country=IN&r=2,0"
#             yield scrapy.Request(url, callback=self.parse, meta={'checkin': checkin, 'checkout': checkout})

#     def parse(self, response):
    

#         # hotelName = response.css('h3.sc-gEvEer hZNzNt div.sc-aXZVg kwRPhS::text').get()
#         # room_name = response.css('h2.sc-gEvEer dAbDZN div.sc-aXZVg cfUwXc::text').get()
#         # room_rates = response.css('h2.sc-gEvEer dAbDZN mr-1 div.sc-aXZVg eat::text').get()
#         try:
#             hotel_name = response.css('div.sc-aXZVg kwRPhS h3.sc-gEvEer hZNzNt::text').get()
#             self.log(f"Hotel Name: {hotel_name}")
#         except Exception as e:
#             self.log(f"Error extracting hotel name: {str(e)}")   

#         # try:
#         #     room_name = response.css('div.sc-aXZVg cfUwXc h2.sc-gEvEer dAbDZN::text').get()
#         #     self.log(f"Room Name: {room_name}")
#         # except Exception as e:
#         #     self.log(f"Error extracting room name: {str(e)}")      

#         # try:
#         #     room_rates = response.css('div.sc-aXZVg eat h2.sc-gEvEer dAbDZN mr-1::text').get()
#         #     self.log(f"Room Rates: {room_rates}")
#         # except Exception as e:
#         #     self.log(f"Error extracting room rates: {str(e)}")
        
        

#         checkin = datetime.strptime(response.meta['checkin'], "%m/%d/%Y")
#         checkout = datetime.strptime(response.meta['checkout'], "%m/%d/%Y")
        
            
#         hotel_info = {
#             "Hotel_Name": hotel_name,
#             "CheckIn": checkin.strftime("%m/%d/%Y"),
#             "CheckOut": checkout.strftime("%m/%d/%Y"),
#         #     "Room_Name": room_name,
#         #     "Room_Rates": room_rates
#         }

#         data_list.append(hotel_info)


#             # Save data to a JSON file
#         with open(f"Clear_Trip_Data.json", "w") as json_file:
#                 json.dump(data_list, json_file, indent=2)