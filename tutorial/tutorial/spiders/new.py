# import time,requests,random,json
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# # List of accounts with Property Code, Username, and Password
# accounts = [
    
#     {'property_code': '28654', 'username': 'admin', 'password': 'Soldout@20251234', 'hotel_name': 'Backpackers Park'},
#     {'property_code': '34941', 'username': 'admin', 'password': 'PrideofG!R@1234', 'hotel_name': 'Gir Pride Resort'},
#     {'property_code': '43354', 'username': 'admin', 'password': 'UK@12345', 'hotel_name': 'Hotel King City'},
#     # {'property_code': '27074', 'username': 'alesayi', 'password': 'Ezee@789', 'hotel_name': 'La Fontaine'},
#     # {'property_code': '41540', 'username': 'admin', 'password': 'Soldout@20251234', 'hotel_name': 'Holy Land'},
#     # {'property_code': '41769', 'username': 'admin', 'password': 'Rahul@1234', 'hotel_name': 'Hotel Caesars Palace'},
#     # {'property_code': '33311', 'username': 'HOTELRAMAYAINN', 'password': 'Ramaya@1234', 'hotel_name': 'Ramaya Inn'},
#     # {'property_code': '42146', 'username': 'Admin', 'password': 'Virender@1972', 'hotel_name': 'Jagdish Residency'},
#     # {'property_code': '35644', 'username': 'retvensadmin', 'password': 'Kgpb3pvZAWf7Bx@', 'hotel_name': 'Clover Villa'},
#     # {'property_code': '43450', 'username': 'admin', 'password': 'Amish@2023', 'hotel_name': 'BD Resort'},
#     # {'property_code': '42474', 'username': 'Admin', 'password': 'sudha@2023', 'hotel_name': 'ABI Residency'},
# ]

# # Create an empty list to store results
# results = []

# driver = webdriver.Chrome()

# try:
#     for account in accounts:
#         property_code = account['property_code']
#         username = account['username']
#         password = account['password']
#         hotel_name = account['hotel_name']

#         try:
#             url = 'https://live.ipms247.com/login/'

#             # Go to the login page
#             driver.get(url)
#             time.sleep(4)

#             # Input credentials and submit the form
#             driver.find_element(By.NAME, 'username').send_keys(username)
#             driver.find_element(By.NAME, 'password').send_keys(password)
#             driver.find_element(By.NAME, 'hotelcode').send_keys(property_code)
#             driver.find_element(By.ID, 'universal_login').submit()

#             # Wait for the login process to complete
#             time.sleep(random.randint(6,8))

#             # Click on the button (assuming this is what btnER does)
#             driver.find_elements(By.CLASS_NAME, 'btnER')[0].click()

#             # Wait for the button click to take effect
#             time.sleep(4)

#             # Get the cookies
#             cookies = driver.get_cookies()

#             # Find the SSID cookie
#             ssid_cookie = next((cookie['value'] for cookie in cookies if cookie['name'] == 'SSID'), None)

#             # Check if SSID cookie is found before proceeding
#             if not ssid_cookie:
#                 print(f"SSID cookie not found for account {username} ({property_code}). Skipping.")
#             else:
#                 print(f'SSID for account {username} ({property_code}): {ssid_cookie}')

#                 # Set up the endpoint and headers for the POST request
#                 endpoint = "https://live.ipms247.com/rcm/services/servicecontroller.php"
#                 headers = {
#                     'Cookie': f'SSID={ssid_cookie}',
#                     'Content-Type': 'application/json'
#                 }

#                 # Set up the body for the POST request
#                 body = {

#                     "action": "getInventoryData",
#                     "service": "inventoryrates",
#                     "startdate": "2023-12-05",
#                     "allocationmode": "ALLOCATED",
#                     "enddate": "2024-12-19"
#                 }

#                 # Make the POST request
#                 response = requests.post(endpoint, headers=headers, json=body)

#                 # Print the response status code and content
#                 print(f"Status Code for account {username} ({property_code}): {response.status_code}")

#                 response_content = response.json()

#                 print(response_content)

#                 # Append the result to the list
#                 results.append({
#                     'property_code': property_code,
#                     'username': username,
#                     'hotel_name': hotel_name,
#                     'response_code': response.status_code,
#                     'response_content': response_content
#                 })

#         except Exception as e:
#             print(f"An error occurred for account {username} ({property_code}): {str(e)}")

# finally:
#     # Close the browser in the finally block to ensure it happens even if there's an exception
#     if 'driver' in locals():
#         driver.quit()
    
#     print(response.text)


# # Save the results to a JSON file
# with open('results.json', 'w') as json_file:
#     json.dump(results, json_file, indent=2)
