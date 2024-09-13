import requests
from bs4 import BeautifulSoup

# Set the URL of the website
url = 'https://baofengtech.com/shop/'

# Fetch the HTML content of the page
response = requests.get(url, headers={
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"})
if response.status_code == 200:
    print("Successfully fetched the webpage.")
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")
    exit()

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all product elements
products = soup.find_all('div', class_="archive-products")

# Iterate through each product and extract details
for product in products:
    # Extract the product link
    link_tag = product.find('div', class_='product-inner')
    print(link_tag)
    if link_tag:
        link = link_tag.find('div', class_='product-inner')
        print(
            '------------------------------------------------------------------------------')
        print(link)
        link = link_tag.get('href')
    else:
        print("Product link not found.")
        link = "N/A"

    # Extract the product price
    price_tag = product.find('span', class_='woocommerce-Price-currencySymbol')
    if price_tag:
        price = price_tag.text
    else:
        print("Product price not found.")
        price = "N/A"
    desc = product.find('h3', class_="a-spacing-mini")
    if desc:
        price = desc.text
    else:
        print("Product desc not found.")
        desc = "N/A"
    # Print the product details
    print(f"Product Link: {link}")
    print(f"Product Price: {price}")
    print(f"Product desc: {desc}")
    print("-" * 40)  # Separator for better readability
