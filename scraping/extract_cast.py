from selenium import webdriver
import time
import sys
import pandas as pd
import os

# for Firefox
driver = webdriver.Firefox()

#  get links for extra cast
from links import links_for_cast

producers=[]
composers=[]
cinematographers=[]
film_editors=[]
casting=[]
production_design=[]
art_direction=[]
set_direction=[]
titles=[]

def get_extra(url):
    driver.get(url)
    time.sleep(3)
    header=driver.find_element_by_id("fullcredits_content")
    head=header.find_elements_by_class_name("simpleCreditsTable")
    h4tags=header.find_elements_by_tag_name("h4")
    i=0
    flag1=0
    flag2=0
    flag3=0
    flag4=0    
    flag5=0
    flag6=0
    flag7=0
    flag8=0

    asdf = driver.find_element_by_class_name("subpage_title_block__right-column")
    abcd = asdf.find_elements_by_tag_name("a")
    titles.append(abcd[0].text)
    for el in h4tags:
        if(el.text=='Produced by '):
            flag1=1
            protemp = []
            for xl in head[i-1].find_elements_by_tag_name("tr"):
                tag=xl.find_elements_by_tag_name("td")
                protemp.append(tag[0].text)
            producers.append(protemp)

        elif(el.text=='Music by '):
            compotemp = []
            flag2=1
            for xl in head[i-1].find_elements_by_tag_name("tr"):
                tag=xl.find_elements_by_tag_name("td")
                compotemp.append(tag[0].text)
            composers.append(compotemp)    

        elif(el.text=='Cinematography by '):
            ct = []
            flag3=1
            for xl in head[i-1].find_elements_by_tag_name("tr"):
                tag=xl.find_elements_by_tag_name("td")
                ct.append(tag[0].text)
            cinematographers.append(ct)

        elif(el.text=='Film Editing by '):
            ft = []
            flag4=1
            for xl in head[i-1].find_elements_by_tag_name("tr"):
                tag=xl.find_elements_by_tag_name("td")
                ft.append(tag[0].text)
            film_editors.append(ft)

        elif(el.text=='Casting By '):
            cat = []
            flag5=1
            for xl in head[i-1].find_elements_by_tag_name("tr"):
                tag=xl.find_elements_by_tag_name("td")
                cat.append(tag[0].text)
            casting.append(cat)

        elif(el.text=='Production Design by '):
            pot = []
            flag6=1
            for xl in head[i-1].find_elements_by_tag_name("tr"):
                tag=xl.find_elements_by_tag_name("td")
                pot.append(tag[0].text)
            production_design.append(pot)

        elif(el.text=='Art Direction by '):
            artt = []
            flag7=1
            for xl in head[i-1].find_elements_by_tag_name("tr"):
                tag=xl.find_elements_by_tag_name("td")
                artt.append(tag[0].text)
            art_direction.append(artt)

        elif(el.text=='Set Decoration by '):
            sett = []
            flag8=1
            for xl in head[i-1].find_elements_by_tag_name("tr"):
                tag=xl.find_elements_by_tag_name("td")
                sett.append(tag[0].text)
            set_direction.append(sett)

        i+=1

    if(flag1==0):
        producers.append('')
    if(flag2==0):
        composers.append('')
    if(flag3==0):
        cinematographers.append('')
    if(flag4==0):
        film_editors.append('')
    if(flag5==0):
        casting.append('')
    if(flag6==0):
        production_design.append('')
    if(flag7==0):
        art_direction.append('')
    if(flag8==0):
        set_direction.append('')
def main():
    for url in links_for_cast:
        try:
            get_extra(url)
        except:
            producers.append('')
            composers.append('')
            cinematographers.append('')
            film_editors.append('')
            casting.append('')
            production_design.append('')
            art_direction.append('')
            set_direction.append('')
    data = list(zip(titles,producers,composers,cinematographers,film_editors,casting,production_design,art_direction,set_direction))
    df = pd.DataFrame(data,columns=['titles','pro','cmp','cinemat','fe','casting','prodes','artd','setd'])
    df.to_csv('newcast8900.csv')
    time.sleep(3)
if __name__ == '__main__':
	main()