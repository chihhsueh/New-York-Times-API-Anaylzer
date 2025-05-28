import requests
import json



qeury = "election"

url = f"https://api.nytimes.com/svc/archive/v1/2020/1.json?api-key={API_Key}"

response = requests.get(url)
content = response.json()

count = 1
for item in content["response"]["docs"]:
  print(count,item["abstract"], item["subsection_name"])
  count +=1