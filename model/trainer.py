import pandas as pd
import classify


class Trainer:

    def __init__(self):
        pass


    def get_query(self):
        pass


def probability( dict_data: dict[dict[dict]]):
        options_columns = list(dict_data.values())[0]
        input_dict = {}

        for key, val in options_columns.items():
            options = dict(enumerate(list(val.keys())))
            query = input(f" select {key} from here \n  {options} \n " )
            if int(query) in options.keys():
                input_dict[key] = options[int(query)]
            else:
                raise ValueError("Invalid choice")
        print(input_dict)
        return calculate(input_dict, dict_data)


def calculate(input_dict, data_dict):
    num = 1
    final_dict = {}
    for label in data_dict.keys():
        print(label, "label")
        for col , val in input_dict.items():
            num *= data_dict[label][col][val]
            print(num , data_dict[label][col][val])
        print("num ", num)
        num *= data_dict[label[1]]

        final_dict[label] = num

    print(final_dict)
    return final_dict















probability(classify.from_data_to_dict(r"C:\\Users\\User\Desktop\\DATA\\NaiveBayes\\data_for_NB_buys_computer-Sheet1.csv", 'Buy_Computer'))










