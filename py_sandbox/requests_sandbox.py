import requests
import json

# url = "https://en.wikipedia.org/w/api.php"

# querystring = {"action":"query","format":"json","prop":"description","list":"search","srsearch":"accenture","srlimit":"1","utf8":"1","formatversion":"2"}

# payload = ""
# headers = {
#     'Accept': "application/json",
#     'cache-control': "no-cache",
#     'Postman-Token': "03624171-cc8f-462b-bd89-c57174d857d3"
#     }

# response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

# print(response.text)

# response_json = json.loads(response.text)

# response_json['query']['search'][0]['snippet']

# def build_url(args):
#     url = ""
#     for arg in args:
#         url += arg
#     return url

# url = build_url([
#     "base/",
#     "relative_path"
# ])


# print(url)