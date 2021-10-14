import requests
from bs4 import BeautifulSoup
url = "https://mlh.io/seasons/2021/events"

r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')

title = soup.title
print(title.text)

events = soup.find_all("a", class_ = "event-link")

for event in events:
    print(event['title'] + ':' + event['href'])
