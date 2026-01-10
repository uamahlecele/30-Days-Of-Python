import requests
import json
from bs4 import BeautifulSoup

# url = 'https://archive.ics.uci.edu/dataset/109/wine'

# response = requests.get(url)

# content = response.content

# soup = BeautifulSoup(content, 'html.parser')

# print(soup.title)
# print(soup.title.get_text())
# # print(soup.body)
# status = response.status_code
# print(status)


#Exercises: Day 22

#1. 

url = 'http://www.bu.edu/president/boston-university-facts-stats/'

response = requests.get(url)

status = response.status_code
print(status)

content = response.content

soup =  BeautifulSoup(content, 'html.parser')

# products = soup.title

# with open("store_scrape.json","w") as f:
#     json.dump(products,f)

# tables = soup.find_all('table',{'cellpadding':3})

# table = tables[0]
# for td in table.find('tr').find_all('td'):
#     print(td.text)
# print(soup.get_text)



