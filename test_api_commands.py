import requests

x = requests.get("https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/que-faire-a-paris-/records", {"tags":"Peinture","limit":"5"})
print (x.json())