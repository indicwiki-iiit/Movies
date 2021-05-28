from selenium import webdriver
import time
import sys
import pandas as pd
import os

# For Firefox
driver = webdriver.Firefox()


def get_data(url):
	driver.get(url)
	try:
		p=driver.find_element_by_class_name("track-list")
		head=driver.find_elements_by_class_name("playback-dynamic")
		l=[]
		song=[]
		for i in head:
 			l.append(i.text)
		for lis in l:
			each=lis.split('\n')
			song.append({each[1]:[each[2],each[3]]})
		return song
	except:
		head1=driver.find_elements_by_class_name("soundTrack")
		l=[]
		for i in head1:
			l.append(i.text)
			song_text=[]
		for s in l:
			s=s.split("\n")[0]
			song_text.append(s)
		return song_text

def main():
	df=pd.read_csv("songs.csv")
	for i in range(len(links)):
		try:
			a=get_data(links[i])
		except:
			a='NaN'
		df.loc[i,'Songs']=str(a)
		df.to_csv("songs.csv")

if __name__ == '__main__':
    main()