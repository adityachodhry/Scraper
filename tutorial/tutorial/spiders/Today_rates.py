# import scrapy
# import json
# from datetime import datetime, timedelta
# import pandas as pd

# list = []

# hotelid = '201412232059037179'

# class RoomItem(scrapy.Item):
    
#     CheckIn = scrapy.Field()
#     CheckOut = scrapy.Field()
#     Price = scrapy.Field()


# class MmtspiderSpider(scrapy.Spider):
#     name = "rates"
#     allowed_domains = ["www.makemytrip.com"]
#     allowed_domains = ["www.goibibo.com"]
#     allowed_domains = ["www.agoda.com"]
#     allowed_domains = ["www.booking.com"]
#     allowed_domains = ["www.expedia.com"]
#     allowed_domains = ["www.cleartrip.com"]
    
#     def start_requests(self):
#         # Initialize a start date
#         start_date = datetime.now().date()

#         # Define the number of days to scrape
#         num_days = 7

#         for k in range(num_days):
#             checkin = (start_date + timedelta(days=k)).strftime("%m%d%Y")
#             checkout = (start_date + timedelta(days=k+1)).strftime("%m%d%Y")
#             url = f"https://www.makemytrip.com/hotels/hotel-details/?hotelId={hotelid}&checkin={checkin}&checkout={checkout}&roomStayQualifier=2e0e&city=CTXSG"
#             yield scrapy.Request(url, callback=self.parse, meta={'checkin': checkin, 'checkout': checkout})

#     def parse(self, response):
#         checkin = datetime.strptime(response.meta['checkin'], "%m%d%Y")
#         checkout = datetime.strptime(response.meta['checkout'], "%m%d%Y")
        
#         room_rates = response.css('div.cstmTooltipHover p.font20 blackText latoBlack::text')
        
        
#         rates = {
#             "checkIn": checkin.strftime("%Y-%m-%d"),
#             "checkOut": checkout.strftime("%Y-%m-%d"),
#             "price": int(room_rates)
#         }

#         list.append(rates)
#         print(list)

#         # # Convert the list of dictionaries to a DataFrame
#         # df = pd.DataFrame(list)

#         # # Save the DataFrame to an Excel file
#         # excel_filename = 'Gir_Pride_1.xlsx'
#         # df.to_excel(excel_filename, index=False)

#         # self.log(f'Data saved to {excel_filename}')
