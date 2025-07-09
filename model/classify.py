import pandas as pd
from pprint import  pprint
from cleaner import clean_data

class Classify:

    def __init__(self):
        pass


    def from_data_to_dict(self ,url: str, unique_column):

        df = pd.read_csv(url)

        df = clean_data(df, "id" )

        columns = list(df.columns)
        print(columns)

        dict_data = dict()

        for val in df[unique_column].unique():
            count = int(df[unique_column].value_counts()[val]) / len(df)

            dict_data[(val, count)] = dict()

            for  col in columns:
                current = df.groupby([unique_column ,col]).size()/count
                if (val, count) in dict_data.keys():
                    dict_data[(val, count)][col] = current[val].to_dict()
                else:
                    dict_data[(val, count)][col] = {}

        print("dict ",dict_data)
        return dict_data


Classify.from_data_to_dict(r"C:\\Users\\User\Desktop\\DATA\\NaiveBayes\\data_for_NB_buys_computer-Sheet1.csv", 'Buy_Computer')
