#Chih-Hsueh Hsieh
import requests
import json
#creates function to lower amount of code


def get_contents(API_Key, year, month, name):
  #The API url given
  url = f'https://api.nytimes.com/svc/archive/v1/{year}/{month}.json?api-key={API_Key}'
  #api request
  response = requests.get(url)
  #json Reponse
  data = json.loads(response.text)
  #write clean files
  with open(name, "w", encoding="utf-8") as file:
    titles = [
        doc['headline']['main']
        for doc in data.get('response', {}).get('docs', [])
    ]
    for title in titles:
      file.write(title + '\n')
  print(f"File {name} is created")


#My API key I made on NYTimes
API_Key = "8CnFI1j8ibMmmmWpDG0VGGdVJEtjJHoR"
#Example for October 1918, month is 10
get_contents(API_Key, 1918, 10, 'titles_1918.txt')
#Example for October 2020, month is 10
get_contents(API_Key, 2020, 10, 'titles_2020.txt')
