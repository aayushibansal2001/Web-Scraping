import bs4


# Step 0: Install all the requirements in terminal
# pip install requests
# pip install bs4
# pip install html5lib

import requests
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com"

# Step 1: Get the HTML
r = requests.get(url)
htmlContent = r.content

# Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

# Step 3: HTML Tree traversal

# Commonly used types of Objects:
# print(type(title)) # 1. Tag
# print(type(title.string)) # 2. NavigableString
# print(type(soup)) # 3. BeautifulSoup

# Get the title of the HTML page
title = soup.title
print(title)

# Get all paragraphs from the page
paras = soup.find_all('p')
print(paras)

# Get first para element in the HTML page
print(soup.find('p')) 

# Get classes of any element in the HTML Page
print(soup.find('p')['class'])

# Find all elements whose class is lead
print(soup.find_all("p", class_ = "lead"))

# Get the text from the tags/soup
print(soup.find('p').get_text())

# Get all the anchor tags from the page
anchors = soup.find_all('a')

all_links = set() # making a set so that we don't get repeated links

# Get all the links on the page
for link in anchors:
    if(link.get('href') != '#'):
        linkText = "https://codewithharry.com" + link.get('href')
        all_links.add(linkText)
        print(linkText)

    