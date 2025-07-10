import pandas as pd
from pprint import  pprint
from cleaner import clean_data

class Classify:

    def __init__(self):
        self.count_unique_label = {}


    def set_count_unique_label(self,unique_keys):
        for key in unique_keys:
            if key in self.count_unique_label.keys():
                self.count_unique_label[key] += 1
            else:
                self.count_unique_label[key] = 1



    def csv_to_full_nested_count_dict(self, file_path, column_name):
        df = pd.read_csv(file_path)
        df = clean_data(df, "id")

        unique_values_per_col = {
            col: df[col].unique() for col in df.columns if col != column_name
        }

        result = {}
        unique_keys = df[column_name].unique()
        self.set_count_unique_label(unique_keys)

        for key in unique_keys:
            sub_df = df[df[column_name] == key]
            inner_dict = {}
            for col, unique_vals in unique_values_per_col.items():
                value_counts = sub_df[col].value_counts().to_dict()
                inner_dict[col] = {val: value_counts.get(val, 0) for val in unique_vals}
            result[key] = inner_dict
        pprint(result)

        return result

    def probability(self , dict_data):
            options_columns = list(dict_data.values())[0]
            input_dict = {}

            for key, val in options_columns.items():
                options = dict(enumerate(list(val.keys())))
                query = input(f" select {key}  \n  {options} \n ")
                if int(query) in options.keys():
                    input_dict[key] = options[int(query)]
                else:
                    raise ValueError("Invalid choice")
            print(input_dict)
            return self.probability_calculate(input_dict, dict_data)

    def probability_calculate(self, input_dict, data_dict):

        final_dict = {}
        p = sum(self.count_unique_label.values())
        print(p)
        for label in data_dict.keys():
            prob = 1
            final_dict[label] = prob

            for col, val in data_dict[label].items():
                loc = input_dict[col]

                final_dict[label] *= val[loc]/ self.count_unique_label[label]

            final_dict[label] *= self.count_unique_label[label]/ p

        print("dictttt", final_dict)
        return final_dict


c = Classify()
c.probability(c.csv_to_full_nested_count_dict(r"C:\\Users\\User\Desktop\\DATA\\NaiveBayes\\data_for_NB_buys_computer-Sheet1.csv", 'Buy_Computer'))






