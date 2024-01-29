# import time
# import requests
# import random
# import json
# from datetime import datetime, timedelta
# from seleniumwire import webdriver
# from selenium.webdriver.common.by import By


# # List of accounts with Property Code, Username, and Password
# accounts = [
#     {'username': 'akshay01', 'password': 'akshay0120'}
# ]

# # Create an empty list to store results
# results = []


# # # Number of months to fetch in each API request
# months_per_request = 3

# # Get the current date
# current_date = datetime.now()

# # Calculate the start date for the loop (3 years ago from the current date)
# start_date = current_date - timedelta(days=365 * 3)

# # Initialize the driver
# driver = webdriver.Chrome()

# try:
#     for account in accounts:
#         username = account['username']
#         password = account['password']

#         url = 'https://www.eglobe-solutions.com/hms/dashboard'

#         # Go to the login page
#         driver.get(url)
#         time.sleep(4)

#         # Input credentials and submit the form
#         driver.find_element(By.NAME, 'Username').send_keys(username)
#         driver.find_element(By.NAME, 'Password').send_keys(password)

#         # Wait for the login process to complete
#         time.sleep(random.randint(6, 8))

#         # Click on the button (assuming this is what btnER does)
#         driver.find_elements(By.NAME, 'button')[0].click()

#         # Wait for the button click to take effect
#         time.sleep(2)

#         authorization_value = next(
#             (request.headers['authorization'] for request in driver.requests if 'authorization' in request.headers), None)
#         print(f"Auth = {authorization_value}")

#         # Set up the endpoint and headers for the POST request
#         headers = {
#             'Content-Type': 'application/json',
#             'Authorization': authorization_value
#         }

#         body = {
#             "SearchBy": "BookingDate",
#             "FromDate": "1-Jan-2023",
#             "TillDate": "22-Nov-2023"
#         }
#         post_endpoint = "https://www.eglobe-solutions.com/cmapi/bookings/search"
#         post_response = requests.post(
#             post_endpoint, headers=headers, json=body)

#         post_response_content = post_response.json()

#         hotelcodes = post_response_content.get('BookingList', [])
#         hotelcode = hotelcodes[0].get(
#             'EgsPropertyId', None) if hotelcodes else None

#         while start_date < current_date:
#             # Calculate the end date for the API request
#             end_date = start_date + timedelta(days=30 * months_per_request)

#             # Format the date strings
#             date_from = start_date.strftime("%d %b %Y")
#             date_till = end_date.strftime("%d %b %Y")

#             # Build the API request URL with the current date range
#             api_url = "https://www.eglobe-solutions.com/hmsapi/reports/ArcReport"

#             main_body = {
#                 "SearchBy": "BookingDate",
#                 "DateFrom": date_from,
#                 "DateTill": date_till
#             }

#             response = requests.post(api_url, headers=headers,json=main_body)

#             # Process the response and update the results list
#             response_content = response.json()

#             bookingList = response_content['Result']['Data']
#             # bookingList = response_result.get('Data', [])
#             for booking in bookingList:
#                 try:
#                     booking_date = datetime.strptime(
#                         booking['BookingTime'], "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%d")
#                 except ValueError:
#                     booking_date = datetime.strptime(
#                         booking['BookingTime'], "%Y-%m-%dT%H:%M:%S.%f").strftime("%Y-%m-%d")

#                 try:
#                     arrival_date = datetime.strptime(
#                         booking['CheckInDate'], "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%d")
#                 except ValueError:
#                     arrival_date = datetime.strptime(
#                         booking['CheckInDate'], "%Y-%m-%dT%H:%M:%S.%f").strftime("%Y-%m-%d")

#                 lead_time = (datetime.strptime(arrival_date, "%Y-%m-%d") -
#                              datetime.strptime(booking_date, "%Y-%m-%d")).days

#                 bkglist = {
#                     'hotelName': booking['PropertyName'],
#                     'res': str(booking['BookingId']),
#                     'bookingDate': booking_date,
#                     'guestName': booking['GuestName'],
#                     'arrivalDate': datetime.strptime(booking['CheckInDate'], "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%d"),
#                     'deptDate': datetime.strptime(booking['CheckOutDate'], "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%d"),
#                     'room': booking['BookedRoomsInfo'].split('(')[0].strip(),
#                     'pax': f"{booking['NumAdults']}\{booking['NumChildren']}",
#                     'source': booking['ChannelName'],
#                     'totalCharges': booking['Amount_BookingTotal'],
#                     'noOfNights': booking['NumNights'] * booking['NumRooms'],
#                     'lead': lead_time,
#                     'hotelCode': str(hotelcode),
#                     'isActive': "true" if booking['BookingStatus'] == 'BOOKED' else "false"
#                 }
#                 results.append(bkglist)

#             # Increment the start date for the next iteration
#             start_date = end_date
        
#         # if results:
#                     # collection.insert_many(results)
#                     # print(f"Inserted data into MongoDB for account {username}")

#         # Save the final results to a JSON file after processing all date ranges
#         with open(f'eglobe_data.json', 'w') as json_file:
#             json.dump(results, json_file, indent=2)

# finally:
#     # Close the browser in the finally block to ensure it happens even if there's an exception
#     if 'driver' in locals():
#         driver.quit()