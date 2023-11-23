import requests
from bs4 import BeautifulSoup
import csv

keywords = ['חמאס', 'חטופים']
url = 'https://www.ynet.co.il/news/'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0'}
response = requests.get(url, headers)

data = BeautifulSoup(response.text, 'html.parser')

layout_containers = data.find_all("div", class_="layoutContainer")

fourth_layout_container = layout_containers[3]

articles = fourth_layout_container.find_all("a")


with open('filescv.csv', 'a', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'URL'])

    for link in articles:
        url1 = link["href"]
        response = requests.get(url1, headers)
        data1 = BeautifulSoup(response.text, 'html.parser')
        try:
            dynamic_column = data1.find("div", class_="dynamicHeightItemsColumn").text
            if any(keyword in dynamic_column for keyword in keywords):
                url2 = link['href']
                tilt = link.text
                writer.writerow([tilt, url2])
                print(url2, tilt)
        except:
            pass
