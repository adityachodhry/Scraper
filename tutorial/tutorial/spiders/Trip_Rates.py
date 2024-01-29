# import requests
# import json
# import datetime
# from datetime import timedelta, timezone

# extracted_data = []

# start_date = datetime.datetime.now(timezone.utc)
# num_days = 1

# for k in range(num_days):
#     checkin = datetime.datetime.now(timezone.utc).strftime("%Y%m%d")
#     checkout = (datetime.datetime.now(timezone.utc) + timedelta(days=1)).strftime("%Y%m%d")
    
#     print(checkin)
#     print(checkout)

#     endpoint = "https://www.trip.com/restapi/soa2/28820/getHotelRoomList"

#     headers = {
#         'Content-Type': 'application/json',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
#         'Accept': '*/*',
#         'Accept-Encoding': 'gzip, deflate, br'
#     }

#     body = {
#         "search": {
#             "hotelId": 95448948,
#             "roomId": 0,
#             "checkIn": checkin,
#             "checkOut": checkout,
#             "roomQuantity": 1,
#             "adult": 2,
#             "childInfoItems": [],
#             "priceType": 0,
#             "hotelUniqueKey": "",
#             "mustShowRoomList": [],
#             "location": {
#                 "geo": {
#                     "cityID": 60045
#                 }
#             },
#             "filters": [],
#             "meta": {
#                 "fgt": -1,
#                 "roomkey": "",
#                 "minCurr": "",
#                 "minPrice": ""
#             },
#             "hasAidInUrl": False,
#             "cancelPolicyType": 0,
#             "fixSubhotel": 0,
#             "isFirstEnterDetailPage": "F",
#             "listTraceId": ""
#         },
#         "head": {
#             "platform": "PC",
#             "cver": "0",
#             "cid": "1704",
#             "bu": "IBU",
#             "group": "trip",
#             "aid": "",
#             "sid": "",
#             "ouid": "",
#             "locale": "en-US",
#             "timezone": "5.5",
#             "currency": "INR",
#             "pageId": "123",
#             "vid": "",
#             "guid": "",
#             "isSSR": False,
#             "frontVersion": "1.1.0"
#         },
#         "hotelExtension": {
#             "fingerprint": "",
#             "token": ""
#         }
#     }

#     response = requests.post(endpoint, headers=headers, json=body)

#     if response.status_code == 200:
#         response_content = response.json()


#     if 'data' in response_content:
#         room_names = response_content['data'].get('physicRoomMap', {})
#         hotel_info = response_content['data'].get('saleRoomMap', {})

#         for room_id, room in room_names.items():
#             id = room.get("id")
#             name = room.get("name")

#             # Iterate through saleRoomMap to find matching room details
#             for sale_room_id, sale_room_info in hotel_info.items():
#                 physical_room_id = sale_room_info.get('physicalRoomId')

#                 meal_info = sale_room_info.get('mealInfo', {})
#                 hover_info = meal_info.get('hover')
#                 meal_description = hover_info[0] if hover_info else None

#                 # Print statements based on meal conditions
#                 if "Includes breakfast and dinner for 1 guest" in meal_description or "Includes breakfast and dinner for 2 guest" in meal_description or "Includes breakfast and dinner for 3 guest" in meal_description:
#                     meal_category = "MAP"
#                 elif "Includes breakfast for 1 guest" in meal_description or "Includes breakfast for 2 guests" in meal_description or "Includes breakfast for 3 guests" in meal_description:
#                     meal_category = "CP"
#                 elif "Meals not included" in meal_description:
#                     meal_category = "EP"
#                 else:
#                     meal_category = "_"

#                 if isinstance(meal_description, list):
#                     meal_description = meal_description[0] if meal_description else None


#                 # Check if the physicalRoomId matches with id
#                 if physical_room_id == id:
#                     # Extract price information
#                     price_info = sale_room_info.get('priceInfo', {})
#                     rate = price_info.get("price")

#                     # Add extracted data to the list
#                     room_data = {
#                         'roomID': id,
#                         "checkIn": checkin,
#                         "checkOut": checkout,
#                         'roomName': name,
#                         'meal': meal_description,
#                         'roomPlan': meal_category,
#                         'price': rate
#                     }
#                     extracted_data.append(room_data)


# # Save the extracted data to a new JSON file
# with open('Trip_Rates_data.json', 'w') as json_file:
#     json.dump(extracted_data, json_file, indent=2)
