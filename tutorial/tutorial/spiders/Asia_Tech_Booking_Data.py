# import time ,re
# import requests
# import json 
# from datetime import datetime
# from bs4 import BeautifulSoup
# from selenium import webdriver
# # from pymongo import MongoClient
# from selenium.webdriver.common.by import By


# # List of accounts with Property Code, Username, and Password
# accounts = [
#     {'usertype': 'Admin', 'username': 'takhatvilla', 'password': 'Hotel@123'}
# ]

# driver = webdriver.Chrome()

# response_content = {}

# # # MongoDB connection
# # client = MongoClient('mongodb://localhost:27017/')
# # db = client['BI']  # DataBase Name
# # collection = db['Asia_Tech']  # Collection Name

# try:
#     for account in accounts:
#         usertype = account['usertype']
#         username = account['username']
#         password = account['password']

#         try:
#             url = 'https://www.asiatech.in/booking_engine/admin/login'

#             # Go to the login page
#             driver.get(url)
#             time.sleep(4)

#             # Input credentials and submit the form
#             driver.find_element(By.ID, 'sel_master_login').send_keys(usertype)
#             driver.find_element(By.ID, 'email').send_keys(username)
#             driver.find_element(By.ID, 'password').send_keys(password)

#             # Wait for the login process to complete
#             time.sleep(4)

#             driver.find_elements(By.CLASS_NAME, 'btn-block')[0].click()

#             time.sleep(4)

#             hotel_name_element = driver.find_element(By.CLASS_NAME, 'username')
#             hotel_name = hotel_name_element.text

#             html_content = driver.page_source

#             # Use a regular expression to extract the value of reg_id
#             reg_id_match = re.search(r'var reg_id = "reg_id=" \+ \'(\d+)\'', html_content)

#             if reg_id_match:
#                 reg_id_value = reg_id_match.group(1)
#                 print(f"Found reg_id: {reg_id_value}")
#             else:
#                 print("No reg_id found.")

#             # Set up the endpoint and headers for the POST request
#             endpoint = "https://www.asiatech.in/booking_engine/admin/ajaxrequest/showbooking/booking_result1.php"
#             headers = {
#                 'Content-Type': 'application/json'
#             }
       
#             # Define the structure for storing data
#             result = []

#             page_number = 1

#             while True :

#                 # Set up the body for the POST request
#                 body = {
#                     "register_id": reg_id_value,
#                     "page": str(page_number),
#                     "ckin": "2015-01-01",
#                     "ckout": "2023-12-19",
#                     "search_book_status": "1"
#                 }
#                 # Make the POST request
#                 response = requests.post(endpoint, headers=headers, json=body)

#                 # Print the response status code
#                 print(
#                     f"Status Code for account {username} ({username}): {response.status_code}")

#                 response_content = response.json()
                
#                 # Check if data is empty
#                 if not response_content:
#                     print("No more data. Exiting loop.")
#                     break

#                 soup = BeautifulSoup(str(response_content), 'html.parser')
#                 # Extract table data
#                 table = soup.find('table')
#                 rows = table.find_all('tr')

#                 # Iterate through each row in the table
#                 for row in rows[1:]:  # Skip the header row
#                     columns = row.find_all('td')

#                     # Extracting values from each column
#                     parsed_date_1_str = columns[5].text.strip()
#                     parsed_date_2_str = columns[6].text.strip()

#                     parsed_date_str = datetime.strptime(columns[3].text.strip(), "%d-%b-%y").strftime("%y-%m-%d")
#                     parsed_date_1_str = datetime.strptime(parsed_date_1_str, "%d-%b-%y")
#                     parsed_date_2_str = datetime.strptime(parsed_date_2_str, "%d-%b-%y")

#                     parsed_date = datetime.strptime(columns[3].text.strip(), "%d-%b-%y").strftime("%Y-%m-%d")
#                     parsed_date_1 = datetime.strptime(columns[5].text.strip(), "%d-%b-%y").strftime("%Y-%m-%d")
#                     parsed_date_2 = datetime.strptime(columns[6].text.strip(), "%d-%b-%y").strftime("%Y-%m-%d")

#                     # isActive = True if columns[13].text.strip() == "CNF" else False
#                     isActive = str(columns[13].text.strip() == "CNF").lower()

#                     # Extracting values from each column
#                     num_nights = (parsed_date_2_str - parsed_date_1_str).days
#                     # Calculate lead time
#                     lead_time_days = (parsed_date_1_str -
#                                     datetime.strptime(parsed_date_str, "%y-%m-%d")).days
                    
#                     room_info = columns[7].text.strip()
#                     room_type_match = re.match(r'(.*) \((\d+)\)', room_info)

#                     if room_type_match:
#                         room_type = room_type_match.group(1).strip()
#                         num_rooms_booked = int(room_type_match.group(2))
#                     else:
#                         room_type = room_info
#                         num_rooms_booked = 1

#                     # Extracting values from each column
#                     booking_data = {
#                         # Extracting values from each column
#                         'hotelName': hotel_name,
#                         "res": columns[1].text.strip(),
#                         "source": columns[2].text.strip(),
#                         "bookingDate": parsed_date,
#                         "guestName": columns[4].text.strip(),
#                         "arrivalDate": parsed_date_1,
#                         "deptDate": parsed_date_2,
#                         "room": room_type,
#                         "totalCharges": int(columns[10].text.strip()),
#                         "isActive": isActive,
#                         "noOfNights": num_nights * num_rooms_booked,
#                         "lead": lead_time_days,
#                         "hotelCode" : str(reg_id_value)
#                     }
#                     result.append(booking_data)

#                 page_number += 1

#             # if result:
#             #     collection.insert_many(result)
#             #     print(f"Inserted data into MongoDB for account {username}")
#         except Exception as e:
#             print(f"An error occurred for account {username}: {str(e)}")

# except Exception as e:
#     print(f"An error occurred: {str(e)}")

# finally:
#     # Close the WebDriver
#     driver.quit()
# # Convert the result to JSON format
    
# with open('Asia_Tech_Final_Booking_Data.json', 'w') as json_file:
#     json.dump(result, json_file, indent=2)


