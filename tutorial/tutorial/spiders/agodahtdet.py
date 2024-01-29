# import scrapy,json,datetime
# from datetime import timezone

# list = []

# class AgodaHtDetSpider(scrapy.Spider):
#     name = "agodahtdet"
#     allowed_domains = ["www.agoda.com"]

#     def start_requests(self):
#         start_date = datetime.datetime.now(timezone.utc)
#         num_days = 90

#         for k in range(num_days):
#             checkin = (start_date + datetime.timedelta(days=k)).strftime("%Y-%m-%d")
#             checkout = (start_date + datetime.timedelta(days=k+1)).strftime("%Y-%m-%d")
#             url = f'https://www.agoda.com/api/cronos/property/BelowFoldParams/GetSecondaryData?checkIn={checkin}&checkOut={checkout}&rooms=1&adults=2&childs=0&los=1&hotel_id=7010854'
#             yield scrapy.Request(url, callback=self.parse, meta={'checkin': checkin, 'checkout': checkout})

#     def parse(self, response):
#         json_data = json.loads(response.text)

#         # with open('agoda_response.jso n', 'w') as json_file:
#         #     json.dump(json_data, json_file, indent=4)

#         hotelid = json_data['hotelId']
#         checkInDate = response.meta['checkin']
#         checkOutDate = response.meta['checkout']
#         hotels = json_data['roomGridData']
#         roomData = hotels['masterRooms']

#         for roomType in roomData:
#             rooms = roomType['rooms']
#             roomID = roomType['id']
#             roomName = roomType['name']
#             for room in rooms:

#                 benefits = []
#                 features = room['features']
#                 displayPrice = room['pricing']['displayPrice']
#                 for feature in features :
#                     try :
#                         if feature['benefits']:
#                             for benefit in feature['benefits']:
#                                 benefits.append(benefit['description'])
#                                 mealPlan = "null"
#                                 if "Breakfast" in benefits:
#                                     if "Lunch included" in benefits or "Dinner included" in benefits:
#                                         mealPlan = "MAP"
#                                     else:
#                                         mealPlan = "CP"
#                                 elif "Lunch included" in benefits and "Breakfast" in benefits:
#                                     mealPlan = "MAP"
#                                 elif "Lunch included" in benefits and "Breakfast" in benefits and "Dinner included" in benefits:
#                                     mealPlan = "AP"
#                                 else:
#                                     mealPlan = "EP"
#                     except:
#                         pass
#                 rates = {
#                     'roomID': roomID,
#                     'checkInDate': checkInDate,
#                     'checkOutDate': checkOutDate,
#                     'roomType' : roomName,
#                     'roomPlan' : mealPlan,
#                     'price' : float(format(displayPrice*83.26, ".2f")),
#                 }
#                 list.append(rates)

#         final_data = {
#             "hId" : 10022,
#             "otaId" : 4,
#             'OtaPId' : str(hotelid),
#             "rates" : list
#         }
#         with open('White_Castle_agoda_rates_0811.json', 'w') as json_file:
#             json.dump(final_data, json_file, indent=4)
