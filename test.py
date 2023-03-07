import requests
from bs4 import BeautifulSoup

url_news = "https://maarweb.com/search.php?term=&type=sites&page=2"
headers = {"User-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}
response = requests.get(url_news,headers=headers)
soup = BeautifulSoup(response.text, "lxml")
match_items = soup.find_all("div", class_="resultContainer")

for match in match_items:
    link = match.find('a', class_='result')['href']
    
    print(f'link:{link}')