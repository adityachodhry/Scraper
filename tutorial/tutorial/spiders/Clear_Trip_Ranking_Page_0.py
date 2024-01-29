# import requests
# import json

# # API endpoint
# endpoint = "https://www.cleartrip.com/hotel/orchestrator/v2/search"

# # Request headers
# headers = {
#     'Content-Type': 'application/json',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
#     'Accept': '*/*',
#     'Accept-Encoding': 'gzip, deflate, br'
# }

# hotel_rankings = []

# # Request body
# body = {
#     "roomAllocations": [
#         {
#             "adults": {
#                 "count": 2,
#                 "metadata": []
#             },
#             "children": {
#                 "count": 0,
#                 "metadata": []
#             }
#         }
#     ],
#     "sortAndFilters": {
#         "sortBy": {
#             "key": "recommended",
#             "metadata": None,
#             "order": "asc"
#         },
#         "amenities": [],
#         "properties": [],
#         "starRating": [
#             "three"
#         ],
#         "localities": [],
#         "inclusions": []
#     },
#     "cityId": "",
#     "city": "Bhopal",
#     "state": "Madhya Pradesh",
#     "country": "IN",
#     "locationSearchName": None,
#     "localityId": None,
#     "locality": None,
#     "metaLandingHotelId": None,
#     "metaLandingSource": None,
#     "unavailableHotels": False,
#     "checkInDate": "09/01/2024",
#     "checkOutDate": "10/01/2024",
#     "seoUrl": "hotels-in-bhopal",
#     "useCaseContext": "DESKTOP_SEO_PAGE",
#     "pageNo": 0,
#     "pageSize": 100
# }

# # Make the POST request
# response = requests.post(endpoint, headers=headers, json=body)

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Parse the JSON response
#     response_content = response.json()

#     # Save the extracted data to a new JSON file
#     with open('Cleartrip_API_data.json', 'w') as json_file:
#         json.dump(response_content, json_file, indent=2)

#         slots_data = response_content['response']['slotsData']

#     for slot in slots_data:
#         if slot['slotData']['type'] == 'HOTEL_CARD_LIST':
#             hotelCards = slot['slotData']['data']['hotelCardList']
#             for card in hotelCards:
#                 ranks = {}
#                 eventData = card['ravenTracking']['eventData']
#                 ranks['rank'] = eventData['h_hotel_rank']
#                 ranks['hotel_id'] = eventData['h_hotel_id']
#                 ranks['hotel_name'] = eventData['h_hotel_name']
#                 ranks['star_category'] = eventData['h_star_category']
#                 ranks['user_rating'] = eventData['h_user_rating']
#                 ranks['total_amount'] = eventData['h_total_amount']


#                 hotel_rankings.append(ranks)
#             else :
#                  pass
# else:
#     print("Error: 'hotels' key not found in the response")

# with open('Cleartrip_Rankin_Data.json', 'w') as json_file:
#         json.dump(hotel_rankings, json_file, indent=2)
# # response.pageData