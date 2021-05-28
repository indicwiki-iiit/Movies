from selenium import webdriver
import time
import sys
import pandas as pd
import os

# For Firefox
driver = webdriver.Firefox()

# Get links for main pages
from links import links_for_mainpage

titles=[]
images=[]
writers=[]
storyline=[]
tagline=[]
trivia=[]
cast=[]

def get_data(url):
    driver.get(url)
    
    #TITLES
    try:
        header=driver.find_elements_by_class_name("title_wrapper")
        head=header[0]
        x=head.find_element_by_tag_name("h1").text
        titles.append(x)
    except: 
        titles.append('Nan')
    #POSTER
    try:
        header=driver.find_elements_by_class_name("poster")
        head=header[0]
        x=head.find_element_by_tag_name("a")
        images.append(x.find_element_by_tag_name("img").get_attribute("src"))
    except:
        images.append('NaN')

    #WRITER
    try:
        writer_local=[]
        header=driver.find_elements_by_class_name("credit_summary_item")
        head=header[1]
        y=head.find_elements_by_tag_name("a")
        for el in y:
            writer_local.append(el.text)
        writers.append(writer_local)
    except:
        writers.append('NaN')

    #CAST
    try:
        cast_local=[]
        head=driver.find_element_by_class_name("cast_list")
        t = head.find_elements_by_tag_name("tr")
        for el in t:
            cast_local.append(el.text)
        cast.append(cast_local)
    except:
        cast.append('NaN')

    #STORYLINE
    try:
        head=driver.find_element_by_id("titleStoryLine")
        x=head.find_element_by_tag_name("p").text
        storyline.append(x)
    except:
        storyline.append('NaN')

    #TAGLINE
    try:
        header=driver.find_elements_by_id("titleStoryLine")
        head=header[0]
        x=head.find_elements_by_class_name("txt-block")
        y=x[0].text
        tagline.append(y)
    except:
        tagline.append('NaN')

    #TRIVIA
    try:
        head=driver.find_element_by_id("trivia")
        x=head.text
        trivia.append(x)
    except:
        trivia.append('NaN')


def main():
    for url in links_for_mainpage:
        try:
            get_data(url)
        except:
            titles.append('NaN')
            images.append('NaN')
            writers.append('NaN')
            cast.append('NaN')
            storyline.append('NaN')
            tagline.append('NaN')
            trivia.append('NaN')

    data = list(zip(titles,images,writers,cast,storyline,tagline,trivia))
    df = pd.DataFrame(data,columns=['titles','images','writers','cast','storyline','tagline','trivia'])
    df.to_csv('updated_gold.csv')

if __name__ == '__main__':
	main()