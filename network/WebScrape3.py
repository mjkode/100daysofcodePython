import requests
from bs4 import BeautifulSoup
urls = 'https://www.py4e.com/lessons' #'https://www.geeksforgeeks.org/'
grab = requests.get(urls)
soup = BeautifulSoup(grab.text, 'html.parser')
# opening a file in write mode
f = open("webscrap3links.txt", "w")
print("")
print("FILE OPEN")
# traverse paragraphs from soup
for link in soup.find_all("a"):
    data = link.get('href')
    f.write(data)
    f.write("\n")

f.close()
print("FILE CLOSED")
