import requests as rq
from bs4 import BeautifulSoup as bs

url = "https://www.scrapethissite.com/pages/simple/"

rp = rq.get(url)

#print(rp.text)

def saveFileFirst():
    with open("Learning/WebScraping/Simple.html", "w+", encoding="utf-8") as f:
        f.write(rp.text)

#saveFileFirst()

with open("Learning/WebScraping/Simple.html") as f:
    content = f.read()

soup = bs(content, 'html.parser')
#print(soup)
h3s = soup.find_all("h3")
for h3 in h3s:
    print(h3.text.strip())

spans = soup.find_all("span")
for span in spans:
    print(span.text.strip())