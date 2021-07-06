from googletrans import Translator
translator = Translator()

from deeptranslit import DeepTranslit
trans = DeepTranslit('telugu').transliterate

import pandas as pd

df = pd.read_csv('data/FinalKB Telugu.csv')

final = []

# Used for transliteration using Deeptranslit or translation using Google trans (Uncomment the unused one)
for i in range(len(df)):
    final.append(trans(str(df.iloc[i][29]))[0]['pred'])
    # final.append(translator.translate(str(df.iloc[i][28]),dest='te',src='en').text)

for el in final:
    print(el)