# import json
# import os
# from pymongo import MongoClient
# from pymongo.errors import ConnectionFailure

# connection_string = "mongodb+srv://Retvens:JMdZt2hEPsqHuVQl@r-rate-shopper-cluster.nlstcxk.mongodb.net/"

# # Specify the folder path where your JSON files are located
# folder_path = 'C:\\Users\\Retvens\\Documents\\Scrapy\\Uploadable\\temp-rates'


# def push_data_to_mongodb(data):
#     try:
#         # Connect to MongoDB using the connection string
#         client = MongoClient(connection_string)
#         # Access the desired database
#         db = client.get_database("rateshopper")
#         # Access the collection where you want to push the data
#         collection = db.get_collection("rates")
#         # Insert the data (in JSON format) into the collection
#         collection.insert_one(data)
#         print("Data inserted successfully!")
#     except ConnectionFailure as e:
#         print(f"Failed to connect to MongoDB: {e}")
#     finally:
#         client.close()

# # Iterate through all JSON files in the folder
# for filename in os.listdir(folder_path):
#     if filename.endswith(".json"):
#         file_path = os.path.join(folder_path, filename)
#         with open(file_path, 'r', encoding='utf-8') as file:
#             json_data = json.load(file)
#             push_data_to_mongodb(json_data)