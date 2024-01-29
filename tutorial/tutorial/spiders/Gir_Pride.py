import scrapy
import json
from datetime import datetime, timedelta
import pandas as pd

list = []

hotelid = '201412232059037179'

class RoomItem(scrapy.Item):
    HotelID = scrapy.Field()
    CheckIn = scrapy.Field()
    CheckOut = scrapy.Field()
    RoomName = scrapy.Field()
    RoomPlan = scrapy.Field()
    Price = scrapy.Field()
    RoomID = scrapy.Field()


class MmtspiderSpider(scrapy.Spider):
    name = "mmtspider"
    allowed_domains = ["www.makemytrip.com"]
    
    def start_requests(self):
        # Initialize a start date
        start_date = datetime.now().date()

        # Define the number of days to scrape
        num_days = 90

        for k in range(num_days):
            checkin = (start_date + timedelta(days=k)).strftime("%m%d%Y")
            checkout = (start_date + timedelta(days=k+1)).strftime("%m%d%Y")
            url = f"https://www.makemytrip.com/hotels/hotel-details/?hotelId={hotelid}&checkin={checkin}&checkout={checkout}&roomStayQualifier=2e0e&city=CTXSG"
            yield scrapy.Request(url, callback=self.parse, meta={'checkin': checkin, 'checkout': checkout})

    def parse(self, response):
        hotelName = response.css('div.prmProperty h1::text').get()
        checkin = datetime.strptime(response.meta['checkin'], "%m%d%Y")
        checkout = datetime.strptime(response.meta['checkout'], "%m%d%Y")
        i = 0
        while True:
            try:
                room = f'room{i}'
                room_id = (str(response.css(f'div#{room} span.rmPhotos__tag::attr(data-testid)').get())).split('-')[0]
                room_name = response.css(f'div#{room} h2.rmType__roomName::text').get()
                room_plans_count = len(response.css(f'div#{room} div.rmSelect__card--row  h5.rmRatePlan__heading::text').extract())
                

                if not room_name:
                    break  # Break the loop when no more rooms are found

                for j in range(room_plans_count):
                    room_plan = response.css(f'div#{room} div.rmSelect__card--row  h5.rmRatePlan__heading::text')[j].get()
                    room_rates = response.css(f'div#{room} div.rmSelect__card--row div.cstmTooltipHover p.font22.latoBlack::text')[((j+1)*3)-1].extract().replace(",", "")
                    if 'Breakfast' in room_plan and 'Lunch' in room_plan and 'Dinner' in room_plan and '/' in room_plan:
                        rplan = 'MAP'
                    elif 'Breakfast' in room_plan and 'Lunch' in room_plan and 'Dinner' in room_plan:
                        rplan = 'AP'
                    elif 'Breakfast' in room_plan:
                        rplan = 'CP'
                    else:
                        rplan = 'EP'
                    
                    rates = {
                        "roomID": int(room_id),
                        "checkIn": checkin.strftime("%Y-%m-%d"),
                        "checkOut": checkout.strftime("%Y-%m-%d"),
                        "roomName": room_name,
                        "roomPlan": rplan,
                        "price": int(room_rates),
                    }

                    list.append(rates)

                i += 1  # Increment i to move on to the next room

            except Exception as e:
                self.logger.error(f"An exception occurred while processing URL {response.url}: {e}")
                break  # Break the loop if an exception occurs

        # Convert the list of dictionaries to a DataFrame
        df = pd.DataFrame(list)

        # Save the DataFrame to an Excel file
        excel_filename = 'Gir_Pride_1.xlsx'
        df.to_excel(excel_filename, index=False)

        self.log(f'Data saved to {excel_filename}')
