from selenium import webdriver
import time
import sys
import os
import csv
import pandas as pd

# from links import wikilinks

temp = ['https://en.wikipedia.org/wiki/The_Shawshank_Redemption','https://en.wikipedia.org/wiki/The_Godfather','https://en.wikipedia.org/wiki/Baahubali_2:_The_Conclusion']

# For Firefox
driver = webdriver.Firefox()

poster_link = []



def get_data(url):
    driver.get(url)
    a = driver.find_element_by_class_name("infobox-image")
    b = a.find_element_by_tag_name("a")
    c = b.get_attribute("href")
    poster_link.append(c)
    # print(c)

# get_data('https://en.wikipedia.org/wiki/The_Shawshank_Redemption')

def main():
    df = pd.read_csv('data/images data - Sheet1.csv')
    for i in range(len(df)):
        try:
            get_data(df.iloc[i][0])
        except:
            poster_link.append('NaN')
            
    data = list(zip(poster_link))
    df = pd.DataFrame(data,columns=['poster'])
    df.to_csv('posters.csv')

if __name__ == '__main__':
    main()