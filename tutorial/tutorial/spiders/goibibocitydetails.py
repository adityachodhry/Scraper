# import scrapy,time,json,re
# from selenium import webdriver

# class GoibiboCityDetailsSpider(scrapy.Spider):
#     name = "goibibocitydetails"

#     def start_requests(self):
#         # Initialize the URL for the first page
#         url = 'https://hermes.goibibo.com/hotels/v13/search/data/v3/6727020267875173073/20231105/20231106/1-2-0?s=popularity&cur=INR&locusData={"countryCode":"IN"}'
#         yield scrapy.Request(url, callback=self.parse)

#     def __init__(self):
#         self.driver = webdriver.Chrome()
#         # self.page_count = 1 # Keep track of the page count

#     def parse(self, response):
#         self.driver.get(response.url)

#         page_source = self.driver.page_source

#         # Use regular expressions to extract JSON data within HTML tags
#         json_data = self.extract_json_data(page_source)

#         if json_data:
#             # Extract and yield data from the current page
#             for item in json_data.get("data", []):
#                 hotel_name = item.get('hn')
#                 location = item.get('l')
#                 rank = item.get('rnk')
#                 hotel_code = item.get('hc')
#                 hotel_star_rating = item.get('hr')

#                 yield {
#                     'rank': rank,
#                     'hotel_name': hotel_name,
#                     'hotel_code': hotel_code,
#                     'location': location,
#                     'starRating': hotel_star_rating
#                 }

#             # Check if there is a "next" value in the JSON for pagination
#             next_page = json_data.get("next")
#             if next_page:
#                 next_url = 'https://hermes.goibibo.com/hotels/v13/search/data/v3/6727020267875173073/20231105/20231106/1-2-0/then?s=popularity&cur=INR&locusData={"countryCode":"IN"}' + f'&next={next_page}'

#                 # Navigate to the next URL
#                 if next_url != response.url:
#                     next_url = str(next_url)
#                     yield scrapy.Request(next_url, callback=self.parse,dont_filter=True)
#                     time.sleep(10)

#     def extract_json_data(self, page_source):
#         # Define a regular expression pattern to find the JSON data within HTML tags
#         pattern = r'<html><head><meta name="color-scheme" content="light dark"></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">(.*?)</pre></body></html>'
#         match = re.search(pattern, page_source)

#         if match:
#             json_str = match.group(1)
#             try:
#                 # Attempt to parse the JSON data
#                 json_data = json.loads(json_str)
#                 return json_data
#             except json.JSONDecodeError as e:
#                 self.logger.error(f"Failed to parse JSON data: {e}")
#                 return None
#         else:
#             self.logger.error("No JSON data found in the page source.")
#             return None

#     def closed(self, reason):
#         # Close the Selenium driver when the spider is done
#         self.driver.quit()
