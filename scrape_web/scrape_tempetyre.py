import requests
import urllib.request
import time
from bs4 import BeautifulSoup

DEBUG = False

def get_tempetyres_brands():
  """
  Returns list of brands from tempetyres type search page.
  """
  print("* getting all tempetyres brands...")
  url = "https://www.tempetyres.com.au/tyres"
  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")

  brands = [brand.text for brand in soup.find(id="Brand").findAll("option")][1:]

  if DEBUG:
    for brand in brands:
      print(brand)

  print(f"* ...done ({len(brands)} brands)")
  return brands

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

def get_links_from_all_tempetyres_brand_pages(brands):
  """
  Returns a list of all linked tyres for all tempetyres brand.
  """
  print("* getting links to all tempetyres tires...")
  links = []

  try:
    for index, brand in enumerate(brands):
      if DEBUG:
        if index > 2: break
      print('*', index, brand, end='\r')
      links += get_links_from_one_tempetyres_brand_page(brand)
  except KeyboardInterrupt:
    print("** INTERRUPTING SCRAPE **")
    pass

  if DEBUG:
    for link in links:
      print(link)

  print(f"* ...done: ({len(links)} links)")
  return links

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

def scrape_all_tempetyres(links):
  """
  Returns dict of data from all tempetyres product pages.
  """
  output = {}
  TEMPETYRES_BASE_URL = "https://www.tempetyres.com.au"

  print("* scraping tempetypres...")
  try:
    for index, link in enumerate(links):
      print('*', index, link.split('?')[1], end='\r')
      try:
        data = scrape_one_tempetyres(TEMPETYRES_BASE_URL+link)
        output[data["TIRE"]] = data
      except KeyboardInterrupt:
        raise KeyboardInterrupt
      except:
        print(f"failed to scrape: {link}")
        if DEBUG:
          import sys, traceback
          traceback.print_exc(file=sys.stdout)
          sys.exit()
        pass
  except KeyboardInterrupt:
    print("** TERMINATING SCRAPE EARLY **")
    pass
    
    
  if DEBUG:
    for item in output.items():
      print(item)

  print(f"* ...done ({len(output)} tires)")
  return output

def save_data_to_json(data):
  import json
  JSON_FILE_NAME = "tempetyres.json"
  print("* writing data to .json...", end='\r')
  json_data = json.dumps(data)
  with open(JSON_FILE_NAME, "w") as json_file:
    json_file.write(json_data)

  print(f"* JSON data written to {JSON_FILE_NAME}")

def save_data_to_csv(data):
  import csv
  CSV_FILE_NAME = "tempetyres.csv"
  print("* writing data to .csv...", end='\r')
  with open(CSV_FILE_NAME, 'w') as csv_file:
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

  print(f"* CSV data written to {CSV_FILE_NAME}")


def main():
  # TODO: 99% sure not all pages are being scraped because of request ratelimits
  # TODO: write to csv with each scrape
  brands = get_tempetyres_brands()
  links = get_links_from_all_tempetyres_brand_pages(brands)
  scraped_tempetyres = scrape_all_tempetyres(links)
  save_data_to_csv(scraped_tempetyres)
  save_data_to_json(scraped_tempetyres)

if __name__ == '__main__':
  # TODO: argparser
  try:
    main()
  except Exception as e:
    print(e)