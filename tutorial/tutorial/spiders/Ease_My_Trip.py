# import re
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException, NoSuchElementException
# import json
# from datetime import datetime, timedelta

# hotel_id = '1513013'
# data_list = []

# checkin_date = datetime.now().date()
# checkout_date = checkin_date + timedelta(days=1)

# checkin_date_str = checkin_date.strftime("%d/%m/%Y")
# checkout_date_str = checkout_date.strftime("%d/%m/%Y")

# url = f"https://www.easemytrip.com/hotels/{hotel_id}/?cin={checkin_date_str}&cOut={checkout_date_str}&Rooms=1&pax=2&ecid=EMTHOTEL-{hotel_id}"

# driver = webdriver.Chrome()

# # Open the URL in the webdriver
# driver.get(url)

# wait = WebDriverWait(driver, 10)

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

                
#                 # room_rates_element = room_element.find_element(By.CSS_SELECTOR, 'div.act_price')
#                 # room_rates_text = room_rates_element.text
#                 # room_rates_numeric = int(re.search(r'\d+', room_rates_text).group())

                
            
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
#     with open(f"Aditya_Data.json", "w") as json_file:
#         json.dump(data_list, json_file, indent=2)

#     driver.quit()
