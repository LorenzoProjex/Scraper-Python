import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_data_from_url(url, class_name_title, class_name_price):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    titles = [title.text.strip() for title in soup.find_all(class_=class_name_title)]
    prices = [price.text.strip() for price in soup.find_all(class_=class_name_price)]
    
    return titles, prices

# URL of website you want to scrape
base_url = 'https://www.website.com/products/page/{}'

# Name of HTML class you want to extract data from, in this example... the product title.
class_name_title = 'CHANGE_ME_TO_THE_CLASS_NAME'

# Name of HTML class you want to extract data from, in this example... the product price.
class_name_price = 'CHANGE_ME_TO_THE_CLASS_NAME'

all_titles = []
all_prices = []

# Using this option allows you to loop through as many pages as you require (from 1 to infinity).
for page_number in range(0, 10):
    url = base_url.format(page_number)
    titles, prices = extract_data_from_url(url, class_name_title, class_name_price)
    
    # Check if the lengths of titles and prices match before extending the lists
    if len(titles) == len(prices):
        all_titles.extend(titles)
        all_prices.extend(prices)

# Create a DataFrame from the titles and prices
data = {'Title': all_titles, 'Price': all_prices}
df = pd.DataFrame(data)

# Export to an Excel file
df.to_excel('titles_and_prices.xlsx', index=False)
