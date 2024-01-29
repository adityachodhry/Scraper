# import requests
# from bs4 import BeautifulSoup
# import json
# import datetime
# results = []  # Reset results list for each iteration

# today = datetime.datetime.now()

# # List to store data for all days
# final_data = []

# for day in range(10):
#     # Calculate check-in and check-out dates for the current iteration
#     check_in_date = (today + datetime.timedelta(days=day)).strftime("%Y-%m-%d")
#     check_out_date = (today + datetime.timedelta(days=day + 1)).strftime("%Y-%m-%d")

#     endpoint = "https://www.cleartrip.com/hotels/details/lemon-tree-hotel-indore-804712?c=22012024|23012024&city=Indore&state=Madhya%20Pradesh&country=IN&r=2,0"


#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
#     }

#     response = requests.get(endpoint, headers=headers)

#     # Check if the request was successful (status code 200)
#     if response.status_code == 200:
#         # Parse the HTML content with BeautifulSoup
#         soup = BeautifulSoup(response.text, 'html.parser')

#         # Find the script with ID "__NEXT_DATA__"
#         next_data_script = soup.find('script', {'id': '__NEXT_DATA__'})

#         # Check if the script was found
#         if next_data_script:
#             # Extract the script content
#             script_content = next_data_script.contents[0] if next_data_script.contents else None

#             if script_content:
#                 # Save the script content to a JSON file
#                 script_data = json.loads(script_content)


#                 slots_data = script_data["props"]["pageProps"]["initialState"]["details"]["data"]["slotsData"]
#                 for slot in slots_data:
#                     stack_type = slot['slotData']['type']

#                     if stack_type == "STACK":
#                         stack_data = slot['slotData']['data']['slots']
#                         for stack in stack_data:
#                             slot_type = stack['slotData']['type']
#                             if slot_type == "ROOM_TYPE_WITH_INCLUSION_DETAILS":
#                                 # Check if 'data' key is nested further
#                                 room_type_data = stack.get('slotData', {}).get('data', {})
#                                 room_variants = room_type_data['roomVariants']

#                                 for variant in room_variants:
#                                     bkgDetails = {}

#                                     roomDetails = variant['data']['primaryCTA']['ravenTracking']['eventData']
#                                     id = bkgDetails['roomID'] = room_type_data['id']
#                                     bkgDetails['checkin'] = check_in_date
#                                     bkgDetails['checkout'] = check_out_date
#                                     bkgDetails['roomName'] = roomDetails['h_room_type']

#                                     meal = variant['data']['heading']
#                                     # bkgDetails['meal'] = meal
#                                     if meal == "Room with Breakfast, Lunch & Dinner":
#                                         bkgDetails['roomPlan'] = 'AP'
#                                     elif meal == "Room with Breakfast & Lunch/Dinner" or meal == "Room With Breakfast & Lunch":
#                                         bkgDetails['roomPlan'] = 'MAP'
#                                     elif meal == "Room with Breakfast":
#                                         bkgDetails['roomPlan'] = 'CP'
#                                     elif meal == "Room Only":
#                                         bkgDetails['roomPlan'] = 'EP'
#                                     else:
#                                         bkgDetails['roomPlan'] = 'NA'

#                                     bkgDetails['price'] = roomDetails['h_amount_per_night'] - roomDetails[
#                                         'h_taxes']

#                                     results.append(bkgDetails)
#                 final_data = ({
#                 "otaId": 1,
#                 "timestamp": datetime.datetime.now().strftime("%Y-%m-%d"),
#                 "rates": results
#             })           # Append the results for the current day to the overall list
                    
        
#     else:
#         print(f"Error: {response.status_code}")
#         print(response.text)

# # Save the entire list to a JSON file
# with open('Cleartrip_Room_Info.json', 'w', encoding='utf-8') as json_file:
#     json.dump(final_data, json_file, indent=2)       

