# import scrapy
# import json
# import datetime
# from datetime import timedelta, timezone
# from urllib.parse import urlparse, parse_qs

# checkin_date = datetime.datetime.now().date() + timedelta(days=1)
# checkout_date = checkin_date + timedelta(days=1)

# checkin_date_str = checkin_date.strftime("%Y-%m-%d")
# checkout_date_str = checkout_date.strftime("%Y-%m-%d")

# ranks = []


# class trivagoRankings(scrapy.Spider):
#     name = "trivago_rankings"
#     rank = 1
#     offset_number = 10
#     start_urls = [
#         f"https://www.trivago.in/en-IN/srl/hotels-bhopal-india?search=200-64980;dr-20240115-20240116"]

#     def parse(self, response):

#         property_cards = response.css('div.bg-white rounded-md shadow-nux-15')

#         if not property_cards:
#             self.log("No property cards found. Please check the CSS selector.")

#         for card in property_cards:
#             item = {}

#             item['rank'] = trivagoRankings.rank
#             trivagoRankings.rank += 1

#             item['name'] = card.css('span[itemprop="name"]::text').get()

#             # Exclude hotels with names starting from 'fab' or 'oyo'
#             if item['name'] and (item['name'].strip().lower().startswith('fab') or item['name'].strip().lower().startswith('oyo')):
#                 continue
            

#             try:
#                 item['starCategory'] = len(card.css('span[itemprop="starRating"] span.HotelRating_starIcon__4W2rT').extract())

#             except:
#                 item['starCategory'] = '-'
#             try:
#                 item['userRating'] = float(card.css('span[itemprop="ratingValue"]::text').get())

#             except:
#                 item['userRating'] = '-'

#             try:
#                 item['discountedPrice'] = int(card.css('p[itemprop="price"]::text').get().replace("₹", "").replace(",", ""))

#             except:
#                 item['discountedPrice'] = '-'

#             ranks.append(item)

#         next_page = f"https://www.trivago.in/en-IN/srl/hotels-bhopal-india?search=200-64980;dr-20240115-20240116;pa-2" + '&offset=' + str(trivagoRankings.offset_number) + '/'

#         if trivagoRankings.offset_number <= 100:
#             trivagoRankings.offset_number += 10
#             yield response.follow(next_page, callback=self.parse)

#     # Move this block outside the for loop
#     final_data = {
#         "timestamp": str(datetime.datetime.now(timezone.utc)),
#         "ranking": ranks[:100]
#     }

#     with open('Trivago.json', 'w', encoding='utf-8') as json_file:
#         json.dump(final_data, json_file, ensure_ascii=False, indent=4)
