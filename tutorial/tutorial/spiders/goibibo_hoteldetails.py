# import requests,json,datetime

# num_days = 90
# room_info_list = []
# for k in range(num_days):
#     start_date = datetime.date.today()
#     checkin_date = start_date + datetime.timedelta(days = k)
#     checkout_date = checkin_date + datetime.timedelta(days=1)
#     checkin_str = checkin_date.strftime("%Y-%m-%d")
#     checkout_str = checkout_date.strftime("%Y-%m-%d")

#     data = {
#         'deviceDetails': {
#             'appVersion': '108.0',
#             'deviceId': '94e676d0-d9e9-400d-9a97-3f2e6adf84ba',
#             'deviceType': 'Desktop',
#             'bookingDevice': 'DESKTOP'
#         },
#         'searchCriteria': {
#             'vcId': '6771549831164675055',
#             'giHotelId': '6888854996029052636',
#             'checkIn': checkin_str,
#             'checkOut': checkout_str,
#             'roomStayCandidates': [
#                 {
#                     'adultCount': 2,
#                     'childAges': []
#                 }
#             ],
#             'comparatorHotelIds': [],
#             'countryCode': 'IN',
#             'cityCode': '',
#             'locationId': 'RGNCR',
#             'locationType': 'region',
#             'currency': 'INR',
#             'limit': 20,
#             'tripType': '',
#             'personalCorpBooking': False
#         },
#         'requestDetails': {
#             'visitorId': '94e676d0-d9e9-400d-9a97-3f2e6adf84ba',
#             'visitNumber': 1,
#             'loggedIn': False,
#             'couponCount': 3,
#             'funnelSource': 'HOTELS',
#             'idContext': 'B2C',
#             'pageContext': 'DETAIL',
#             'channel': 'B2Cweb',
#             'brand': 'GI',
#             'siteDomain': 'in',
#             'journeyId': '-2066572494e676d0-d9e9-400d-9a97-3f2e6adf84ba',
#             'requestId': '2b970580-1a89-4e9f-b1d0-e63235750e51',
#             'sessionId': '751876b2-b493-461e-85ae-8e699fb38513'
#         },
#         'filterCriteria': [],
#         'featureFlags': {
#             'addOnRequired': True,
#             'applyAbsorption': True,
#             'bestCoupon': True,
#             'freeCancellationAvail': True,
#             'responseFilterFlags': True,
#             'soldOutInfoReq': True,
#             'walletRequired': True,
#             'detailPersuasionCardsRequired': True,
#             'bestOffersLimit': 3
#         },
#         'expData': '{APE:10,PAH:5,PAH5:T,WPAH:F,BNPL:T,MRS:T,PDO:PN,MCUR:T,ADDON:T,CHPC:T,AARI:T,NLP:Y,RCPN:T,PLRS:T,MMRVER:V3,BLACK:T,IAO:F,EMIDT:1,AIP:T,APT:T,SOU:T,CV2:T,MLOS:T,SRRP:T,unificationReviewV2:True}'
#     }

#     headers = {'Content-Type': 'application/json',
#             'Tid': 'avc'}

#     response = requests.post(
#         'https://mapi.goibibo.com/clientbackend-gi/cg/search-rooms/desktop/2?language=eng&region=in&currency=INR&idContext=B2C&countryCode=IN&ck=a1c8a5db-7c0b-42fc-9012-19be33be13d3', json=data, headers=headers)

#     if response.status_code == 200:
    
#         response_data = json.loads(response.content)
        
#         try :
#             rooms = response_data["response"]["exactRooms"]

#             hotel_id = response_data["response"]["hotelDetails"]["hotelId"]

#             for room in (rooms):

#                 room_name = room["roomName"]
#                 room_id = room['roomCode']
#                 checkin = data['searchCriteria']['checkIn']
#                 checkout = data['searchCriteria']['checkOut']

#                 rate_plans = room['ratePlans']

#                 for plan in rate_plans:
#                     for inclusion in plan['inclusionsList']:
#                         try:
#                             if inclusion['category'] == 'MEAL' : 
#                                 meal_plan = inclusion['inclusionCode']
#                         except :
#                             pass
#                     price_map = plan["tariffs"][0]["priceMap"]
#                     for key, value in price_map.items():
#                         if isinstance(value, dict) and "details" in value:
#                             price = value["details"][2].get("amount")
#                             if price is not None:
#                                 break

#                     room_info = {
#                         'otaPId' : hotel_id,
#                         'rId': room_id,
#                         'checkInDate ':checkin,
#                         'checkOutDate':checkout,
#                         'roomType' : room_name,
#                         'roomPlan' : meal_plan ,
#                         'price' : int(price),
#                     }

#                     print (room_info)
#                     room_info_list.append(room_info)
#         except:
#             pass

# with open('White_Castle_goibibo_rates_0811.json', 'w') as json_file:
#     json.dump(room_info_list, json_file, indent=4)