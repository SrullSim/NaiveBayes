from pprint import pprint

import pandas as pd
from pandas import read_excel


class Cleaner:

    def __init__(self):
        pass

def clean_data(df: pd, columns_to_drop = None) :

        clean = df.dropna()
        if columns_to_drop:
            clean = df.drop(columns=columns_to_drop)
        return clean




