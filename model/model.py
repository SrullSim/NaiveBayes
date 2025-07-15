from pprint import pprint
import pandas as pd


class Model:

    def __init__(self, path, column_to_work_on, drops= None):
        self.DF = pd.read_csv(path)
        self.column_to_work_on = column_to_work_on
        if drops:
            self.DF.drop(drops, axis=1, inplace=True)

    @staticmethod
    def unique_values(dataframe,column):
        return dataframe[column].unique()

    @staticmethod
    def amount_of_unique_values(dataframe,column,value):
        return float(dataframe.loc[dataframe[column] == value,column].count())

    @staticmethod
    def amount_of_all_values(dataframe):
        return float(dataframe.shape[0])

    def all_columns(self, classifier):
        columns = self.DF.columns
        return [col for col in columns if col != classifier]

    def split_dataframe_by_value(self,column,value):
        return self.DF.groupby(column).get_group(value)

    def dict_class(self):
        class_dict = {}
        all_values = self.amount_of_all_values(self.DF)
        for val in self.unique_values(self.DF,self.column_to_work_on):
            unique_values = self.amount_of_unique_values(self.DF,self.column_to_work_on,val)
            class_dict[val] = unique_values / all_values
        return class_dict

    def dict_values(self):
        dict1 = {}
        for val in self.unique_values(self.DF, self.column_to_work_on):
            split_df = self.split_dataframe_by_value(self.column_to_work_on, val)
            column = self.all_columns(self.column_to_work_on)
            col_dict = {}
            for col in column:
                count_val = self.amount_of_all_values(split_df)
                unique_val = self.unique_values(self.DF, col)
                split_unique_val = self.unique_values(split_df, col)
                inner_dict = {}
                if len(unique_val) == len(split_unique_val):
                    for value in unique_val:
                        value_count = self.amount_of_unique_values(split_df, col, value)
                        inner_dict[value] = value_count / count_val
                else:
                    count_val += len(unique_val)
                    for value in unique_val:
                        value_count = self.amount_of_unique_values(split_df, col, value) + 1
                        inner_dict[value] = value_count / count_val
                col_dict[col] = inner_dict
            dict1[val] = col_dict
        # pprint(dict1)
        return dict1


    def dict_values1(self):
        """ build dict of all values in df  """

        all_columns = [col for col in self.DF.columns if col != self.column_to_work_on]
        unique_values_dict = {col: self.unique_values(self.DF, col) for col in all_columns}
        target_unique_values = self.unique_values(self.DF, self.column_to_work_on)
        result = {}

        for target_val in target_unique_values:
            split_df = self.split_dataframe_by_value(self.column_to_work_on, target_val)
            count_in_class = self.amount_of_all_values(split_df)
            col_dict = {}

            for col in all_columns:
                unique_vals = unique_values_dict[col]
                unique_vals_in_class = self.unique_values(split_df, col)
                inner_dict = {}


                if len(unique_vals) == len(unique_vals_in_class):
                    for val in unique_vals:
                        count_val = self.amount_of_unique_values(split_df, col, val)
                        inner_dict[val] = count_val / count_in_class if count_in_class > 0 else 0
                else:
                    smoothed_denominator = count_in_class + len(unique_vals)
                    for val in unique_vals:
                        count_val = self.amount_of_unique_values(split_df, col, val) + 1
                        inner_dict[val] = count_val / smoothed_denominator if smoothed_denominator > 0 else 0

                col_dict[col] = inner_dict

            result[target_val] = col_dict
        # pprint(result)
        return result

