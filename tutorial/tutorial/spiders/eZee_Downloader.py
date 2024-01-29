# import time, re
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException, NoSuchElementException
# import json
# from datetime import datetime, timedelta

# # List of accounts with Property Code, Username, and Password
# accounts = [
#     {'username': 'Sejal', 'password': 'Retvensservices@9feb', 'property_code': '14766'}
# ]

# driver = webdriver.Chrome()

# data_list = []

# checkin_date = datetime.now().date()
# checkout_date = checkin_date + timedelta(days=1)

# checkin_date_str = checkin_date.strftime("%d/%m/%Y")
# checkout_date_str = checkout_date.strftime("%d/%m/%Y")



# driver = webdriver.Chrome()
# wait = WebDriverWait(driver, 5)
# try:
#     for account in accounts:
#         username = account['username']
#         password = account['password']
#         property_code = account['property_code']

#         try:
#             url = f"https://live.ipms247.com/login/"

#             driver.get(url)
#             time.sleep(4)
#             # Input credentials and submit the form
#             driver.find_element(By.ID, 'sel_master_login').send_keys(username)
#             driver.find_element(By.ID, 'email').send_keys(password)
#             driver.find_element(By.ID, 'password').send_keys(property_code)
            
#             time.sleep(4)

#             driver.find_elements(By.CLASS_NAME, 'btn-block')[0].click()


# try:
#     # Extracting hotel information
#     hotel_name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.headcol.mgr15.ng-binding"))).text

#     user_rating_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.review-bg-g.ng-binding')))
#     user_rating_text = user_rating_element.text
#     user_rating_num = float(re.search(r'\d+\.\d+', user_rating_text).group())

#     num_reviews_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.Review-Section-count')))
#     num_reviews_text = num_reviews_element.text
#     num_reviews_num = int(re.search(r'\d+', num_reviews_text).group())


#     # Extracting room information
#     room_elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.box_body.mrel.ng-scope')))

#     for room_element in room_elements:
#         room_name_element = room_element.find_element(By.CSS_SELECTOR, 'h4.ng-binding')
#         room_name = room_name_element.text

#         room_plan_elements = room_element.find_elements(By.CSS_SELECTOR, 'div.wid_75_b_in span[ng-bind-html="_m"]')

#         for room_plan_element in room_plan_elements:
#             plan = room_plan_element.text

#             room_rates_elements = room_element.find_elements(By.CSS_SELECTOR, 'div.act_price')
#             for room_rates_element in room_rates_elements:
#                 room_rates_text = room_rates_element.text
#                 room_rates_num = int(re.search(r'\d+', room_rates_text).group())



#                 if "Breakfast" in plan and "dinner" in plan and "lunch" in plan and "included" in plan and not("not" in plan): 
#                     mealPlan = "AP"
#                 elif "Breakfast" in plan and "dinner" in plan or "lunch" in plan and "included" in plan:
#                     mealPlan = "MAP"
#                 elif "Breakfast included" in plan:
#                     mealPlan = "CP"
#                 else:
#                     mealPlan = "EP"

                
            
#             # Create a dictionary for each room and append to the data list
#                 room_data = {
#                     "Hotel_Id": hotel_id,
#                     "Hotel_Name": hotel_name,
#                     "Checkin": checkin_date_str,
#                     "Checkout": checkout_date_str,
#                     "User_Rating": user_rating_num,
#                     "Number_of_Reviews": num_reviews_num,
#                     "Room_Name": room_name,
#                     "Room_Plan": mealPlan,
#                     "Room_Rates": room_rates_num,
#                     "plan" : plan
#                 }

#                 data_list.append(room_data)

# except NoSuchElementException as e:
#     print(f"Element not found: {e}")
# except TimeoutException as e:
#     print(f"Timeout exception: {e}")
# except Exception as e:
#     print(f"An error occurred: {e}")
# finally:
#     # Save data to a JSON file
#     with open(f"EMT_Hotel_Data.json", "w") as json_file:
#         json.dump(data_list, json_file, indent=2)

#     driver.quit()
