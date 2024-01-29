# import requests
# import json
# import datetime
# from datetime import timedelta, timezone

# hotel_name = 'Amar Kothi Udaipur'

# api_url = 'https://us.trip.com/restapi/soa2/14975/homepageSuggest'

# body = {
#     "keyword": hotel_name,
#     "head": {
#     }
# }

# response = requests.post(api_url, json=body)

# if response.status_code == 200:
#     response_content = response.json()

#     with open('suggest.json', 'w') as json_file:
#         json.dump(response_content, json_file, indent=2)


#     result = response_content['result']

#     for data in result:

#         id = data.get("id")
#         print(id)


