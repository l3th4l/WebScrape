from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("chromedriver")

def get_products(page = 1):

    products = [] #Product names
    img_urls = [] #Product image

    driver.get("https://www.amazon.in/s?k=masala&rh=p_n_is_pantry%3A9574335031&dc&page=" + str(page) + "&qid=1580033436&rnid=9574334031&ref=sr_pg_2")

    content = driver.page_source

    soup = BeautifulSoup(content, 'html.parser')

    items = soup.find_all('div', {"class" : "sg-col-4-of-24 sg-col-4-of-12 sg-col-4-of-36 s-result-item sg-col-4-of-28 sg-col-4-of-16 sg-col sg-col-4-of-20 sg-col-4-of-32"})

    for element in items:
        #gets the product name
        pr_name = element.find('span', {"class" : "a-size-base-plus a-color-base a-text-normal"})
        #gets the product image
        pr_img = element.find('img', {"class" : "s-image"})

        products.append(pr_name.text)
        img_urls.append(pr_img['src'])

    return zip(products, img_urls)

#Pages 
pgs = [1, 2]

#pandas dataframe for products
df = pd.DataFrame({'Product Name' : [], 'Image URL' : []})

#Get products from all of the pages
for page in pgs:
    df = df.append(pd.DataFrame(get_products(page), columns = ['Product Name', 'Image URL'] ), ignore_index = True)

print(df)

#save a the list of product names and image URLs
df.to_csv("amazon_masala.csv", index=False)