# import json
# from pymongo import MongoClient
# from pymongo.errors import ConnectionFailure

# connection_string = MongoClient('mongodb://localhost:27017/')

# # Specify the file path
# file_path = 'C:\Users\Aditya\Desktop\Learn\tutorial\tutorial\spiders\Udaipur_rankings_03012024.json'

# # Open and read the JSON file with UTF-8 encoding
# with open(file_path, 'r', encoding='utf-8') as file:
#     json_data = json.load(file)

# def push_data_to_mongodb(data):
#     try:
#         # Connect to MongoDB using the connection strin
#         client = MongoClient(connection_string)
#         # Access the desired database
#         db = client.get_database("BI")
#         # Access the collection where you want to push the data
#         collection = db.get_collection("Djubo")
#         # Insert the data (in JSON format) into the collection
#         collection.insert_many(data)
#         print("Data inserted successfully!")
#     except ConnectionFailure as e:
#         print(f"Failed to connect to MongoDB: {e}")
#     finally:
#         client.close()
# push_data_to_mongodb(json_data)