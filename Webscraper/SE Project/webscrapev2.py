from typing import Text
from pandas.core.frame import DataFrame
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pathlib import Path
import pandas as pd
products= []






shopee = "https://shopee.ph/Ceramic-Matte-Full-Screen-Film-For-REALME-3-5-5i-5PRO-6-6i-6PRO-7-7i-C2-C3-C11-C15-C17-i.324268637.7761207154?position=32"

rating = []


CO = webdriver.FirefoxOptions()
CO.add_argument('--ignore-certificate-errors')
CO.add_argument('--start-maximized')
driver = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\geckodriver.exe',options=CO)

driver.get(shopee)
driver.implicitly_wait(10)

i = 1

title = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[1]/span')
print(title.text)
prod_title = {'Product_Name': title.text}
products.append(prod_title)


while True:
    solid_button = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/div/div[3]/div[2]/button[2]")
    if int(solid_button.text)== 1:
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        time.sleep(4)
    
        prod_reviews = driver.find_elements_by_class_name('shopee-product-rating__content')
        for prod_review in prod_reviews:
            print(prod_review.text.encode('unicode_escape').decode(u'utf-8'))
            product = {'Product_Reviews': prod_review.text.encode('unicode_escape').decode(u'utf-8')}
            products.append(product)

        
    right_button = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/div/div[3]/div[2]/button[8]')
    if right_button:
        while True: 
                i = i+1
                right_button.click();
                solid_button = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/div/div[3]/div[2]/button[2]")
                if int(solid_button.text)== i:
                    solid_button = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/div/div[3]/div[2]/button[2]")
                    driver.execute_script('window.scrollTo(0,4000);')                
                    time.sleep(3)
                    prod_reviews = driver.find_elements_by_class_name('shopee-product-rating__content')
                    for prod_review in prod_reviews:
                        print(prod_review.text.encode('unicode_escape').decode(u'utf-8'))
                        product = {'Product_Reviews':prod_review.text.encode('unicode_escape').decode(u'utf-8')}
                        products.append(product)
                       
                if int(solid_button.text)!= i:
                    break;

df = pd.DataFrame(products, columns = ['Product_Name','Product_Reviews'])
            
df.to_csv('C:/Users/HP/Documents/Thesis Coding/Web Scrapper Phyton/prodreview.csv',columns=['Product_Name','Product_Reviews'],index = False,encoding = 'utf-8')

driver.close()