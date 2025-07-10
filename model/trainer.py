
import pandas as pd
from pprint import  pprint
import classify
from model.classify import Classify
from model.cleaner import clean_data


class Trainer:

    def __init__(self, path, target):
        # self.model = Classify()
        # self.df = self.model.from_data_to_dict(path, target)
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

















