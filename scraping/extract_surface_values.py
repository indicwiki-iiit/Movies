from selenium import webdriver
import time
import sys
import pandas as pd
import os

# For firefox
driver = webdriver.Firefox()

# get urls for surface list of 8927 movies 250 at a time
from links import surface_urls

titles = []
ratings = []
duration = []
rated = []
genres = []
synopsis = []
votes = []
gross = []
directors = []
imdbids = []
posters = []
release = []
cast = []

for url in surface_urls:
    driver.get(url)

    head = driver.find_elements_by_class_name("mode-advanced")
    for movies in head:

        info1 = movies.find_element_by_tag_name("img")
        titles.append(info1.get_attribute("alt"))
        posters.append(info1.get_attribute("src"))
        imdbids.append(info1.get_attribute("data-tconst"))
        info2 = movies.find_element_by_class_name("lister-item-year")
        release.append(info2.text)
        duration.append(movies.find_element_by_class_name("runtime").text)
        genres.append(movies.find_element_by_class_name("genre").text)
        ratings.append(movies.find_element_by_class_name("ratings-imdb-rating").text)
        try:
            rated.append(movies.find_element_by_class_name("certificate").text)
        except:
            rated.append("NaN")
        stathead = movies.find_element_by_class_name("sort-num_votes-visible")
        span_tags = stathead.find_elements_by_tag_name("span")
        votes.append(span_tags[1].text)
        try: 
            if(span_tags[3].text == 'Gross:'):
                gross.append(span_tags[4].text)
        except:
            gross.append("NaN")
        plothead = movies.find_element_by_class_name("lister-item-content")
        ptags = plothead.find_elements_by_tag_name("p")
        synopsis.append(ptags[1].text)
        peeps = ptags[2].find_elements_by_tag_name("a")
        directors.append(peeps[0].text)
        



data = list(zip(imdbids,titles,release,duration,ratings,rated,genres,directors,synopsis,votes,gross,posters))
df = pd.DataFrame(data,columns=['IMDbID','Title','Release Year','Duration','Rating','Rated','Genre','Director','Synopsis','Votes','Gross','Poster'])
df.to_csv('newmainwith8900.csv')
