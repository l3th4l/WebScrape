import urllib.request
import os 
import pandas as pd 

path = 'imgs'

if not os.path.isdir(path):
    os.mkdir(path) 

#Url list 
df = pd.read_csv("amazon_masala.csv")

def download(product_list, save_folder = path):
    for id, product in product_list.iterrows():
        #print(product)

        print(product['Product Name'])
        try:
            urllib.request.urlretrieve(product['Image URL'], path + '/' +  product['Product Name'] + '.png')
        except:
            print(product['Product Name'] + ' COUND NOT BE RETRIEVED')

download(df)