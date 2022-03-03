# import libraries
import requests
import pandas
from bs4 import BeautifulSoup
from datetime import date

# get todays date
today = date.today()
time = today.strftime("%m-%d-%y")
print()
print("date =", today)

# get content from news site
news_site = "https://www.nbcnews.com/business"
res = requests.get(news_site)
soup = BeautifulSoup(res.content, 'html.parser')

# scrape headlines from content
headlines = soup.find_all('span', {'class': 'tease-card__headline'})
len(headlines)
print(len(headlines))
for i in range(len(headlines)):
    print(headlines[i].text)
    print()

    data_nbc = pandas.DataFrame(headlines)
    data_nbc.to_csv(
        "nbc_business.csv", index=True, header=False)
