# import time
# import requests
# import random
# import json
# from datetime import datetime
# # from pymongo import MongoClient
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# # List of accounts with Property Code, Username, and Password
# accounts = [
#     {'username': 'mirage@hotelmirage.in', 'password': 'djubo123'}
# ]

# # Create an empty list to store results
# results = []

# # Initialize the WebDriver (Chrome)
# driver = webdriver.Chrome()

# # # MongoDB connection
# # client = MongoClient('mongodb://localhost:27017/')
# # db = client['BI']  # DataBase Name
# # collection = db['Djubo']  # Collection Name

# try:
#     for account in accounts:
#         username = account['username']
#         password = account['password']

#         try:
#             url = 'https://apps.djubo.com/sign-in/'

#             # Go to the login page
#             driver.get(url)

#             # Input credentials and submit the form
#             driver.find_element(By.NAME, 'email_address').send_keys(username)
#             driver.find_element(By.NAME, 'password').send_keys(password)

#             # Wait for the login process to complete
#             time.sleep(random.randint(6, 8))

#             # Click on the button (assuming this is what btnER does)
#             driver.find_elements(By.CLASS_NAME, 'submitBtn')[0].click()

#             # Wait for the button click to take effect
#             time.sleep(4)

#             # Get the cookies
#             cookies = driver.get_cookies()

#             # Find the SSID cookie
#             authorization = next(
#                 (cookie['value'] for cookie in cookies if cookie['name'] == 'auth_token_7'), None)

#             # Check if SSID cookie is found before proceeding
#             if not authorization:
#                 print(f"SSID cookie not found for account {username}. Skipping.")
#             else:
#                 print(f'SSID for account {username}  {authorization}')

#                 headers = {
#                     'Cookie': f'auth_token_7={authorization}',
#                     'Content-Type': 'application/json'
#                 }
#                 property_endpoint = "https://apps.djubo.com/core-data/properties"
#                 property_response = requests.get(property_endpoint, headers=headers)
#                 property_response_content = property_response.json()
#                 for property in property_response_content :
#                     hotel_id = property.get("id")
#                     print(hotel_id)

#                 page_number = 1
#                 while True:
#                     # Set up the endpoint and headers for the POST request
#                     endpoint = f"https://apps.djubo.com/analytics-api-data/accounts/0/properties/{hotel_id}/folios-list?page={page_number}&search=&type=2&via=folioSearch"

#                     response = requests.get(endpoint, headers=headers)

#                     # Print the response status code and content
#                     print(f"Status Code for account {username} (Page {page_number}): {response.status_code}")

#                     response_content = response.json()

#                     if not response_content:
#                         print(f"No more data for account {username}. Exiting loop.")
#                         break

#                     for data in response_content:
#                         bkgDetails = {}

#                         bkgDetails['hotelName'] = data['general_details']['property_name']
#                         bkgDetails['res'] = str(data['general_details']['guest_id'])

#                         booking_date = datetime.strptime(data['general_details']['created_on'], '%m/%d/%Y')
#                         bkgDetails['bookingDate'] = booking_date.strftime("%Y-%m-%d")

#                         bkgDetails['guestName'] = data['general_details']['guest_name']

#                         arrival_date = datetime.strptime(data['general_details']['arrival_date'], '%m/%d/%Y')
#                         departure_date = datetime.strptime(data['general_details']['departure_date'], '%m/%d/%Y')

#                         # Format dates as strings in your desired format
#                         bkgDetails['arrivalDate'] = arrival_date.strftime("%Y-%m-%d")
#                         bkgDetails['deptDate'] = departure_date.strftime("%Y-%m-%d")

#                         room_type_full = data['general_details']['room_categories']
#                         room_type_parts = room_type_full.split(' X ')
#                         room_type = room_type_parts[0] if room_type_parts else room_type_full

#                         bkgDetails['room'] = room_type

#                         if data['general_details']['agency_class'] == "OTA":
#                             bkgDetails['source'] = data['general_details']['agency_name']

#                         adults = data['general_details']['total_adults']
#                         children = data['general_details']['total_children']
#                         lead_time = arrival_date - booking_date

#                         bkgDetails['pax'] = f"{adults}\{children}"

#                         bkgDetails['noOfNights'] = data['room_details']['total_room_nights']
#                         bkgDetails['totalCharges'] = round(data['payment_summary_details']['total_amount'], 2)

#                         bkgDetails['lead'] = lead_time.days
#                         bkgDetails['hotelCode'] = str(hotel_id)

#                         if data['general_details']['status'] == 'Confirmed':
#                             bkgDetails['isActive'] = "true"
#                         else:
#                             continue

#                         results.append(bkgDetails)
                        
#                     page_number += 1  # Move to the next page
                
#                 # if results:
#                 #     collection.insert_many(results)
#                 #     print(f"Inserted data into MongoDB for account {username}")

#                 with open('results_djubonew.json', 'w') as json_file:
#                     json.dump(results, json_file, indent=2)

#         except Exception as e:
#             print(f"An error occurred for account {username}  {str(e)}")
#             print(data)
#             with open('results_djubonew.json', 'w') as json_file:
#                     json.dump(results, json_file, indent=2)

# finally:
#     # Close the browser in the finally block to ensure it happens even if there's an exception
#     if 'driver' in locals():
#         driver.quit()