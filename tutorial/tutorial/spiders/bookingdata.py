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


# class BookingRankings(scrapy.Spider):
#     name = "bookingrankings"
#     rank = 1
#     offset_number = 10
#     start_urls = [
#         f"https://www.booking.com/searchresults.html?ss=Ahmedabad&checkin={checkin_date_str}&checkout={checkout_date_str}"]

#     def parse(self, response):

#         property_cards = response.css(
#             'div[data-testid="property-card-container"]')

#         if not property_cards:
#             self.log("No property cards found. Please check the CSS selector.")

#         for card in property_cards:
#             item = {}

#             item['rank'] = BookingRankings.rank
#             BookingRankings.rank += 1

#             item['name'] = card.css('h3 div[data-testid="title"]::text').get()

#             # Exclude hotels with names starting from 'fab' or 'oyo'
#             if item['name'] and (item['name'].strip().lower().startswith('fab') or item['name'].strip().lower().startswith('oyo')):
#                 continue

#             anchor = card.css('a[data-testid="title-link"]::attr(href)').get()
#             parsed_anchor = urlparse(anchor)
#             query_params = parse_qs(parsed_anchor.query)
#             all_sr_blocks = query_params.get("all_sr_blocks")
#             item['OtaPId'] = str(all_sr_blocks[0].split("_")[0][:-2])

#             try:
#                 item['starCategory'] = len(
#                     card.css('div[data-testid="rating-stars"] span').extract())
#             except:
#                 item['starCategory'] = '-'
#             try:
#                 item['userRating'] = float(
#                     card.css('div[data-testid="review-score"] div:nth-child(1)::text').get())
#             except:
#                 item['userRating'] = '-'

#             rating_count = card.css(
#                 'div[data-testid="review-score"] div:nth-child(2)::text').get()
#             try:
#                 item['numberOfRatings'] = int(rating_count.replace(
#                     ",", "").replace(" reviews", "").replace(" review", ""))
#             except:
#                 item['numberOfRatings'] = rating_count

#             item['discountedPrice'] = int(card.css(
#                 'span[data-testid="price-and-discounted-price"]::text').get().replace("\xa0", " ").split(' ')[1].replace(",", ""))

#             # Extract distance from center
#             item['distanceFromCenter'] = card.css(
#                 'span[data-testid="distance"]::text').get()

#             # # Extract price for X nights
#             # item['priceForXNights'] = card.css(
#             #     'div[data-testid="price-for-x-nights"].abf093bdfe.f45d8e4c32::text').get()

#             # # Extract number of adults
#             # item['numberOfAdults'] = int(item['priceForXNights'].split(
#             #     ' ')[-2]) if item['priceForXNights'] else None

#             ranks.append(item)

#         next_page = f"https://www.booking.com/searchresults.html?ss=Ahmedabad&ssne=Indore&checkin={checkin_date_str}&checkout={checkout_date_str}" + '&offset=' + str(
#             BookingRankings.offset_number) + '/'

#         if BookingRankings.offset_number <= 100:
#             BookingRankings.offset_number += 10
#             yield response.follow(next_page, callback=self.parse)

#             final_data = {
#                 "timestamp": str(datetime.datetime.now(timezone.utc)),
#                 "otaId": 3,
#                 "cityCode": "CTAMD",
#                 "ranking": ranks[:100]
#             }

#             with open('Ahmedabad_hotels_booking_071123.json', 'w', encoding='utf-8') as json_file:
#                 json.dump(final_data, json_file, ensure_ascii=False, indent=4)
