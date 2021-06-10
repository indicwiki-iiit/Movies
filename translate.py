from googletrans import Translator
translator = Translator()

from deeptranslit import DeepTranslit
trans = DeepTranslit('telugu').transliterate

import pandas as pd

df = pd.read_csv('data/Dataset8900 - FinalKB_english.csv')

final = []

for i in range(0,1000):
    # final.append(trans(str(df.iloc[i][26]))[0]['pred'])
    final.append(translator.translate(str(df.iloc[i][28]),dest='te',src='en').text)

for el in final:
    print(el)