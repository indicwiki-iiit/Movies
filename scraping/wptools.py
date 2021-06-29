#Distribution_company,distribution_format, distributed_by, followed_by, part_of_series, main_subject. based_on
import pandas as pd
import wptools
df = pd.read_csv("det1.csv")

for i in range(2457,8931):
    movies=df.loc[i]['movie_name']
    movie_name=movies
    imdb_id=""
    narrative_id=""
    image_id=""
    distributed_by=""
    distribution_format=""
    part_of_series=""
    main_subject=""
    based_on=""
    try:
        page = wptools.page(movie_name)
        page.get_wikidata()
        x = page.data['wikidata']
        print(x)
        try:
            narrative_id = x['narrative location (P840)']
        except:
            narrative_id = ""
        try:
            image_id = x['image (P18)'] 
        except:
            image_id = ""
        try:
            distributed_by = x['distributed by (P750)']
        except:
            distributed_by = ""
        try:
            distribution_format = x['distribution format (P437)']
        except:
            distribution_format = ""
        try:
            part_of_series = x['part of the series (P179)']
        except:
            part_of_series = ""
        try:
            main_subject = x['main subject (P921)']
        except:
            main_subject = ""
        try:
            based_on = x['based on (P144)']
        except:
            based_on = ""
        try:
            imdb_id = x['IMDb ID (P345)']
        except:
            imdb_id = ""
                    
        print("*********************")
        print(movie_name)
        print(imdb_id)
        print(narrative_id)
        print(image_id)
        print(distributed_by)
        print(distribution_format)
        print(part_of_series)
        print(main_subject)    
        print(based_on)
        #df.at[i,'movie_name'] = movie_name
        df.loc[i,'imdb_id'] = str(imdb_id)
        df.loc[i,'narrative_id'] = str(narrative_id)
        df.loc[i,'image_id'] = str(image_id)
        df.loc[i,'distributed_by'] = str(distributed_by)
        df.loc[i,'distribution_format'] = str(distribution_format)
        df.loc[i,'part_of_series'] = str(part_of_series)
        df.loc[i,'main_subject'] = str(main_subject)
        df.loc[i,'based_on']=str(based_on)
        df.to_csv("det1.csv")
    except:
        pass
        