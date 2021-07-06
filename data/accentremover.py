import unicodedata
import pandas as pd

df = pd.read_csv("./data/accents.csv")

def strip_accents(text):

    try:
        text = unicode(text, 'utf-8')
    except NameError: # unicode is a default on python 3 
        pass

    text = unicodedata.normalize('NFD', text)\
           .encode('ascii', 'ignore')\
           .decode("utf-8")
    return str(text)

def main():
    # for j in range(len(df.columns)):
    for i in range(len(df)):
        df.iloc[i][0] = strip_accents(str(df.iloc[i][0]))

    df.to_csv("./data/accentscleaned.csv") 

if __name__ == '__main__':
    main()