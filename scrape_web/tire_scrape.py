import requests
import urllib.request
import time
from bs4 import BeautifulSoup

DEBUG = False

def scrape_one_products_page(url):
  """
  Returns list of urls found in one prioritytire products page.
  """
  response = requests.get(url)
  if DEBUG: print(response)
  soup = BeautifulSoup(response.text, "html.parser")

  # TODO: this is only getting half the links
  cards = soup.findAll("article", class_="card")
  # cards = soup.findAll("li", class_="product ng-scope")
  
  print(len(cards))

  urls = []
  for i, card in enumerate(cards):
    urls.append(card['data-url'])
    # if DEBUG: print(f"[{i}] {card['data-url']}")

  

  return urls
  # product_grid = soup.findAll("ul", class_="productGrid")

  # for product in product_grid:
  #   # print(product)
  #   card = product.findAll("article", class_="card")
  #   for c in card:
  #     print(c['data-url'])

# all_urls = []
# for i in range(30):
#   url = f"https://www.prioritytire.com/by-performance/all-terrain-tires/?p={i}"
#   urls = scrape_one_products_page(url)
#   if len(urls) > 0:
#     all_urls+=urls
#   else:
#     break

# for i, url in enumerate(all_urls):
#   print(f'[{i}] {url}')

def scrape_one_prioritytire(url):
  """
  Returns dict of data from one prioritytire product page.
  """
  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")

  tabs = soup.findAll("div", class_="tab_ctm_fd_sec")

  desc_ctm = {}

  # TODO: get price

  for tab in tabs:
    key = tab.findAll("span", class_="desc_ctm_name")[0]
    value = tab.findAll("span", class_="desc_ctm_val")[0]
    desc_ctm[key.text] = value.text

  if DEBUG:
    for item in desc_ctm.items():
      print(item)

  return desc_ctm

# url = "https://www.prioritytire.com/pirelli-scorpion-verde-ao-235-50r18-97v-tire-2016/"
# print(scrape_one_prioritytire(url))

def get_tempetyres_brands():
  """
  Returns list of brands from tempetyres type search page.
  """
  print("* getting all tempetyres brands...", end='\r')
  url = "https://www.tempetyres.com.au/tyres"
  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")

  brands = [brand.text for brand in soup.find(id="Brand").findAll("option")][1:]

  if DEBUG:
    for brand in brands:
      print(brand)

  print(f"* getting all tempetyres brands: done ({len(brands)} brands)")
  return brands

# get_tempetyres_brands()

def get_links_from_one_tempetyres_brand_page(brand):
  """
  Returns a list of all linked tyres for a given brand.
  """
  # print(f"* getting links to tyres from {brand}...")
  url = f"https://www.tempetyres.com.au/tyres?Brand={brand}"
  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")

  links = []

  for container in soup.findAll("div", class_="image-container"):
    links.append(container.find("a", href=True)["href"])

  if DEBUG:
    for link in links:
      print(link)

  return links

# get_links_from_one_tempetyres_brand_page("Accelera")

def get_links_from_all_tempetyres_brand_page():
  """
  Returns a list of all linked tyres for all tempetyres brand.
  """
  print("* getting links to all tempetyres tyres...", end='\r')
  links = []

  for index, brand in enumerate(get_tempetyres_brands()):
    # if DEBUG:
    if index > 2: break
    print(index, brand, end='\r')
    links += get_links_from_one_tempetyres_brand_page(brand)

  if DEBUG:
    for link in links:
      print(link)

  print(f"* getting links to all tempetyres tyres: done ({len(links)} links)")
  return links


# get_links_from_all_tempetyres_brand_page()

def scrape_one_tempetyres(url):
  """
  Returns dict of data from one tempetyres product page.
  """
  # print(f"* scraping data from {url}...", end='\r')
  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")

  output = {}

  output["TIRE"] = soup.find("div", class_="content-bg-titlebar").find("h1").text
  output["NAME"] = soup.find("p", class_="sub-heading").text
  output["PRICE"] = soup.find("div", class_="txtprice-large").text.replace(" each", "")
  output["STOCK"] = soup.find("span", class_="stocklevel-large").find("span").text
  for row in soup.find(id="tyre_specs").findAll("tr"):
    spec = row.findAll("td")
    output[spec[0].text] = spec[1].text
  output["DESCRIPTION"] = soup.find(id="tyre_descr").findAll("div", class_="col-xs-12")[1].text
  output["DELIVERY"] = "TODO"
  output["INSTALLATION"] = "TODO"
  output["OTHER SIZES"] = "TODO"

  if DEBUG:
    for item in output.items():
      print(item)

  return output

# url = "https://www.tempetyres.com.au/tyreproducts?accelera-2555519-111w-iota"
# scrape_one_tempetyres(url)

def scrape_all_tempetyres():
  """
  Returns dict of data from all tempetyres product pages.
  """
  output = {}
  TEMPETYRES_BASE_URL = "https://www.tempetyres.com.au"

  links = get_links_from_all_tempetyres_brand_page()

  print("* scraping tempetypres...")
  try:
    for index, link in enumerate(links):
      print(index, link.split('?')[1], end='\r')
      try:
        data = scrape_one_tempetyres(TEMPETYRES_BASE_URL+link)
        output[data["TIRE"]] = data
      except:
        print(f"failed to scrape: {link}")
        if DEBUG:
          import sys, traceback
          traceback.print_exc(file=sys.stdout)
          sys.exit()
        pass
  except KeyboardInterrupt:
    pass
    
    
  if DEBUG:
    for item in output.items():
      print(item)

  return output

scraped_tempetyres = scrape_all_tempetyres()

def save_data_to_json(data):
  import json
  print("* writing data to .json...", end='\r')
  json_data = json.dumps(data)
  with open("tempetyres.json", "w") as json_file:
    json_file.write(json_data)

def save_data_to_csv(data):
  import csv
  print("* writing data to .csv...", end='\r')
  with open("tempetyres.csv", 'w') as csv_file:
    w = csv.writer(csv_file)
    if data == None: return
    # write headers
    first = list(data.keys())[0]
    row = [key for key in data[first].keys()]
    w.writerow(row)
    # write data
    for value in data.values():
      row = [val for val in value.values()]
      w.writerow(row)

save_data_to_csv(scraped_tempetyres)
save_data_to_json(scraped_tempetyres)