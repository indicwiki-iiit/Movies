from selenium import webdriver
import time
import sys
import os
import csv
import pandas as pd

# For Firefox
driver = webdriver.Firefox()

# Links for awards
from links import links_for_awards

def get_data(url):
    driver.get(url)
    awards = driver.find_elements_by_class_name("awards")
    lis=[]
    for award in awards:
        td=award.find_elements_by_tag_name("td")
        for i in td: 
            lis.append(i.text)
    nom=[]
    win=[]
    fn=0
    fw=0
    for i in lis:
        if "Nominee" in i:
            fn=1
            fw=0
        if "Winner" in i:
            fw=1
            fn=0
        if(fn==1):
            nom.append(i)
        elif(fw==1):
            win.append(i)

    nomd={}
    for i in nom:
        if "Nominee" in i:
            s=i.split('\n')
            title_name=s[1]
            nomd[title_name]=[]
        if "Nominee" not in i:
            nomd[title_name].append(i.split('\n'))
    wind={}
    for i in win:
        if "Winner" in i:
            s=i.split('\n')
            title_name=s[1]
            wind[title_name]=[]
        if "Winner" not in i:
            wind[title_name].append(i.split('\n'))
    return nomd,wind

def main():
    df=pd.read_csv("awards.csv")
    for i in range(len(links_for_awards)):
        try:
            nominee,winner=get_data(links_for_awards[i])   
        except:
            nominee={}
            winner={}
            
        df.loc[i,'Nominee']=str(nominee)
        df.loc[i,'Winner']=str(winner)
        df.to_csv("awards.csv")

if __name__ == '__main__':
    main()