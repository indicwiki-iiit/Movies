import pickle
import pandas as pd

# Makes a .pkl file which can be for loading data into the template
def main():
    moviesFile = 'data/FinalKB Telugu.csv'
    moviesDF = pd.read_csv(moviesFile)
    moviesDF = moviesDF.fillna('NaN')
    pickle.dump(moviesDF, open('./123.pkl', 'wb'))

if __name__ == '__main__':
    main()