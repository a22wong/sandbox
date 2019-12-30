import json
import csv

f = open("tempetyres.json", 'r')
data = json.loads(f.read())
f.close()

# for item_key, item_data in data.items():
#   print(item_key)
#   for key, val in item_data.items():
#     print(key, val)

with open("tempetyres.csv", 'w') as csv_file:
  w = csv.writer(csv_file)
  first = list(data.keys())[0]
  row = [key for key in data[first].keys()]
  w.writerow(row)
    
  for value in data.values():
    row = [val for val in value.values()]
    # print("= = = = = = = = = = = = = = = = = = = =")
    # print(row)
    w.writerow(row)


if __name__ == "__main__":
  pass