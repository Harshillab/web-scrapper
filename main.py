import requests
from bs4 import BeautifulSoup

url = "https://toscrape.com/"
r  = requests.get(url)
htmlContent = r.content
print(htmlContent)

soup =BeautifulSoup(htmlContent,'html.parser')
print(soup.prettify)
page_title = soup.title
page_body = soup.body
page_head = soup.head
print(page_title,page_body,page_head)
title = soup.title
print(type(title.string))
print(type(soup))
print(type(title))

# print(anchors)

print(soup.find('p'))
# print(soup.find('p')['class'])
print(soup.find_all("p", class_="row"))
print(soup.find('p').get_text())
print(soup.get_text())

anchors = soup.find_all('a')
all_links = set()
for link in anchors:
    if(link.get('href') !='#'):
        linkText = "https://toscrape.com/"+link.get('href')
        all_links.add(link)
        print(linkText)
for link in anchors:
    print(link.get('href'))
 

navbarSupportedContent = soup.find(id="navbarSupportedContent")
print(navbarSupportedContent)


for link in soup.find_all("a"):  
    print("Inner Text is: {}".format(link.text))  
    print("Title is: {}".format(link.get("title")))  
    print("href is: {}".format(link.get("href"))) 