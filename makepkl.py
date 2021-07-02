# import pandas as pd

# df = pd.read_csv("data/dataset8930.csv")
# df.fillna("NaN")
# df.to_pickle("./123.pkl")

import pickle
import pandas as pd


def main():
    moviesFile = 'data/FinalKB Telugu.csv'
    moviesDF = pd.read_csv(moviesFile)
    moviesDF = moviesDF.fillna('NaN')
    pickle.dump(moviesDF, open('./123telugu.pkl', 'wb'))


if __name__ == '__main__':
    main()