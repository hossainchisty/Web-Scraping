import requests
# pip install requests
from bs4 import BeautifulSoup
# pip install beautifulsoup

search = "weather today at my location"

url = f"https://www.google.com/search?&q={search}"

read = requests.get(url)

soup = BeautifulSoup(read.text, 'html.parser')

temp = soup.find("div",class_='BNeawe')                      
print(temp.text)                                 