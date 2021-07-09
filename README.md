# Movies
Movies is a branch of IndicWiki Project


## Description

The goal of this project is to automate the process of generation of Movie wikipedia articles in Telugu language. 

## Installation
Create virtual environment in the project folder using the following commands.

```bash
$ pip install virtualenv
$ virtualenv -p python3.7 venv
```
After the successful creation of virtual environment (venv), clone the repository or down the zip folder of the project and extract it into the project folder.

Activate the virtual environment and headover to install the dependencies by following command.
```bash
$ pip install -r requirements.txt
```
requirements.txt comes along with the Project Directory. 



This repository contains the details and data under TeWiki Project for Movies domain.  
You can find the detailed report [here](https://github.com/indicwiki-iiit/Movies/blob/main/report.md) 
You can also find the sample article [here].(https://github.com/indicwiki-iiit/Movies/blob/main/Templates/Sample%20Article.pdf) 

## Github Structure

### Details regarding structure

### Stats
> Github folder Link: https://github.com/indicwiki-iiit/Movies/tree/main/Stats
- This folder contains the statistcs that were observed from the dataset.
    - _Domains, Attributes - Movies.pdf_ -- This file contains all the section details, attributes used in the section, their attributes count and the description of the section.
    - _Template, translation details.pdf_ -- It has details about the attributes that have been translated and translitered along with the tools that have been used. It also mentions the details about the atributes that had limited values and hence were manually translitered(Example:countries -> USA:యు.స్.ఎ).
    - _stats - Attrs-Record values.pdf_ -- This file has details about the attributes and their record count and it also has extra details about the stub articles, not stub articles, average, lowest, highest word count movie articles.
    - _stats - bool values.csv_ -- It has boolen representation for each record value, i.e. "1" indicating that the value is present and "0" means that the value is not present.

### Templates
> Github folder Link: https://github.com/indicwiki-iiit/Movies/tree/main/Templates
- This folder contains the templates that are used for article generation
  - _main_template.j2_ -- Contains the final Jinja2 Template for the article generation.
### Data
> Github folder Link: https://github.com/indicwiki-iiit/Movies/tree/main/data
- _Dataset8900 - FinalKB.csv_ -- This is the final dataset obtained after web scraping from the IMDB website using Selenium and wikidata using wptools.
- _Accentremover.py_ -- Python Code to remove all the special characters with accents. ex. à,é
- _Analyse.py_ -- Code used to analyse if the attribute holds any value for a particular record or not. So, for each attribute if there’s a value. It gives 1 and if there is not any value present it shows 0 and this is stored in a csv file.
- Bingtranslate.py_ -- Translates the required attributes to Telugu using Bing Translator API.
- _Cleanedup.py_ -- Code to remove duplicate records which exist because of extracting data from Wikidata.
- _Emptyvalues.csv_ -- Contains Boolean values sshowing availability a particular attribute from a particular movie.
- _Merge.py_ -- This code is used for merging databases(csv files).
- _sweet.py_ -- The code present in this file is to generate a sweetviz report.
- _Translate.py_ -- For transliterating attributes,this file is used.

### Scraping
> Github folder Link: https://github.com/indicwiki-iiit/Movies/tree/main/scraping 
- This folder contains files of codes written for all the extraction of attributes from different sources.
  - _extract_awards.py_ -- This code is used for extracting data from the IMDB awards page for every movie 
  - _extract_cast.py_ -- This code is used for extracting crew details like  set_decorator, art_director, film_editor, cinematography,production_design,composer,production_designer,producer from IMDB cast webpage.
  - _extract_images.py_ -- This code is used for extracting images from wikipedia using wikipedia links extracted from wikidata.
  - _Extract_main.py_ -- All the data like cast details, release date,director,writer, synopsis,trivia, storyline, tagline,film locations,production company, runtime,color,sound mix and all such attributes which could not be extracted from the surface level of imdb website, are extracted using this code
  - _extract_songs.py_ -- This code is used for extracting songs from IMDB songs page.
  - _extract_surface_values.py_ -- Attributes like genre,rating,rated,votes,gross,plot are extracted using IMDB webpages.
  - _links.py_ -- This contains links for awards,songs,cast and crew, surface level attributes.
  - _Wptools.py_ -- This code is used for extracting narrative location, distributed_by, distributed_format, part_of_series, main_subject and based_on attributes from wikidata using wptools.
### 123.pkl
> Github file Link: https://github.com/indicwiki-iiit/Movies/blob/main/123.pkl
- This is the final pickle file generated from the dataset.
### Readme.md
> Github file Link: https://github.com/indicwiki-iiit/Movies#readme
- This file has links to the sample article created. It has English Wikipedia,Telugu Wikipedia and tewiki sandboxes. This also has a link to the documentation of what is done every week.  
### SWEETVIZ_REPORT.html:
> Github file Link: https://github.com/indicwiki-iiit/Movies/blob/main/SWEETVIZ_REPORT.html
- This is an exploratory data analysis report made to check how many unique values are present for each attribute and how many missing values the attribute has.
### genXML.py
> Github file Link: https://github.com/indicwiki-iiit/Movies/blob/main/genXML.py
- This file contains the code for generating an XML file which has the data after rendering for an article.
### makepkl.py:
> Github file Link: https://github.com/indicwiki-iiit/Movies/blob/main/makepkl.py
- This file contains code for reading the dataset and generating a pickle file
### render.py
> Github file Link: https://github.com/indicwiki-iiit/Movies/blob/main/render.py
- This is the code used for rendering the movie articles using jinja2 template named main_template.j2 file in templates folder.
### requirements.txt:
> Github file Link: https://github.com/indicwiki-iiit/Movies/blob/main/requirements.txt
- This contains all the packages and libraries that are necessary for building this project.
