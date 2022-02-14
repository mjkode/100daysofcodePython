import sys  # for commandline input
from bs4 import BeautifulSoup
import requests

# input url

url = sys.argv[1]
#url = input('What is the URL? ')
print(url)
# urls = 'https://www.py4e.com/lessons' #'https://www.geeksforgeeks.org/'
grab = requests.get(url)
soup = BeautifulSoup(grab.text, 'html.parser')
# opening a file in write mode
f = open("links.txt", "w")
print("")
print("FILE OPEN")
# traverse paragraphs from soup
for link in soup.find_all("a"):
    data = link.get('href')
    f.write(data)
    print(data)
    if data.startswith("#"):
        data = url + data
        print(data)
    if data.startswith("/"):
        data = url[:url.rfind('/')] + data
        # url + data
        print(data)
    print(str(requests.get(data).status_code))
    f.write("\n")

f.close()
print("FILE CLOSED")
