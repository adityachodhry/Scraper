# import requests
# import json
# import datetime
# from datetime import timedelta, timezone

# hotel_id = '5e45600b2b0a5f10a4dede2a'
# extracted_data = []
# def start_requests():
#     start_date = datetime.datetime.now(timezone.utc)
#     num_days = 10

#     for k in range(num_days):
#         checkin = (start_date + timedelta(days=k)).strftime("%Y-%m-%d")
#         checkout = (start_date + timedelta(days=k + 1)).strftime("%Y-%m-%d")

#         # API endpoint
#         endpoint = f"https://hotel.happyeasygo.com/api/web/room_type/{hotel_id}/searchRoom"

#         # Request headers
#         headers = {
#             'Content-Type': 'application/json',
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
#             'Accept': '*/*',
#             'Accept-Encoding': 'gzip, deflate, br'
#         }

#         # Request body with dynamic check-in and check-out dates
#         body = {
#             "cityName": "Bhopal",
#             "guests": [{"id": 1, "adult": 2, "child": 0, "age": []}],
#             "hotelCode": hotel_id,
#             "checkIn": checkin,
#             "checkOut": checkout
#         }

#         # Make the POST request
#         response = requests.post(endpoint, headers=headers, json=body)

#         # Check if the request was successful (status code 200)
#         if response.status_code == 200:
#             # Parse the JSON response
#             response_content = response.json()

#             # Save the complete API response to a new JSON file
#             with open('Go_API_data.json', 'w') as json_file:
#                 json.dump(response_content, json_file, indent=2)

            
#             hotel_info = response_content.get('data', {}).get('roomInfo', [])

#             for hotel in hotel_info:
#                 hotel_cards = hotel.get('ratePlansInfo', [])

#                 for card in hotel_cards:
#                     # Define meal plan based on room_plan
#                     room_plan = card.get('ratePlanName')
#                     if 'Breakfast & Lunch And Dinner' in room_plan:
#                         meal_plan = 'AP'
#                     elif 'Breakfast & Lunch Or Dinner' in room_plan:
#                         meal_plan = 'MAP'
#                     elif 'Breakfast' in room_plan:
#                         meal_plan = 'CP'
#                     else:
#                         meal_plan = 'EP'

#                     # Prepare info dictionary
#                     info = {
#                         'hotel_Id': body.get('hotelCode'),
#                         'checkin' : checkin,
#                         'checkout': checkout,
#                         'room_Name': hotel.get('roomTypeName'),
#                         # 'room_Plan': room_plan,
#                         'meal_Plan': meal_plan,
#                         'room_Price': card.get('currentPrice'),
#                     }
#                     extracted_data.append(info)

#             # Save the extracted data to a new JSON file
            
        
#         else:
#             print(f"Error: {response.status_code}, {response.text}")
#     with open('Hotel_Go_API_Data.json', 'w') as json_file:
#                 json.dump(extracted_data, json_file, indent=2)
# # Call the function to start the requests
# start_requests()
