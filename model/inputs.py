from model import Model
from probabilityCalculater import ProbabilityCalculater



class Inputs:
    def __init__(self,model):
        self.model = model
        self.dict_values = self.model.dict_values()
        self.calculate = ProbabilityCalculater(self.model)

    def create_dict(self):
        column_options = list(self.dict_values.values())[0]
        input_dict = {}
        for k, v in column_options.items():
            options = dict(enumerate(list(v.keys())))
            choice = input(f"{k}:\n {options}\n")
            try:
                if int(choice) in options.keys():
                    input_dict[k] = options[int(choice)]
                else:
                    print("Not a valid option please start again")
                    return self.create_dict()
            except Exception as ex:
                print("error: ", ex)
                return self.create_dict()
        return input_dict

    def probability(self):
        return self.calculate.probability(self.create_dict())

a = Model(r'C:\Users\User\Desktop\DATA\NaiveBayes\data_for_NB_buys_computer-Sheet1.csv','Buy_Computer','id')
b = Inputs(a)
print(b.probability())
