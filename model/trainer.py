
import pandas as pd
from pprint import  pprint
import classify
from model.classify import Classify
from model.cleaner import clean_data


class Trainer:

    def __init__(self, path, target):
        # self.model = Classify()
        # self.df = self.model.from_data_to_dict(path, target)
        # self.target = target
        # self._dict_columns = self.set_dict_columns(self.df)
        pass

    def set_dict_columns(self, df):
        columns = {}
        for col in df[-1].unique():
            if col not in columns.keys():
                columns[col] = 1
            else:
                columns[col] += 1
        return columns

    def check_not_zero(self, val):
        if val != 0:
            return True
        return False








c = Classify()
probability(c.csv_to_full_nested_count_dict(r"C:\\Users\\User\Desktop\\DATA\\NaiveBayes\\data_for_NB_buys_computer-Sheet1.csv", 'Buy_Computer'))










