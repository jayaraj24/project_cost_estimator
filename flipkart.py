import requests
from bs4 import BeautifulSoup

# Set the URL of the website
url = 'https://www.flipkart.com/search?q=walkie+talkie&sid=j9e%2Cabm&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_sc_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_sc_na_na&as-pos=1&as-type=RECENT&suggestionId=walkie+talkie%7CHome+Appliances&requestId=96933aca-4668-4eda-8638-76b4ae8a12be&as-searchtext=wakki%20'
r = requests.get(url)
print(r)

soup = BeautifulSoup(r.text, 'html.parser')
print(soup)
