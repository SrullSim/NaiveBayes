import pandas as pd
from pprint import  pprint
import model
import probabilityCalculater


class Trainer:

    def __init__(self,model):
        self.model =model
        self.probable = probabilityCalculater.ProbabilityCalculater(self.model)

    def sample(self,fraction):
        return self.model.DF.sample(frac=fraction)

    @staticmethod
    def left_sample(sample,original):
        return original[~original.index.isin(sample.index)]

    @staticmethod
    def data_frame_to_dict(dataframe):
        return dataframe.to_dict('index')


    def test(self):
        right = 0
        wrong = 0
        test_sample = self.sample(0.7)
        original_dataframe = self.model.DF
        self.model.DF = test_sample
        trial_data = self.left_sample(test_sample,original_dataframe)
        for k,v in self.data_frame_to_dict(trial_data.drop(self.model.column_to_work_on,axis=1)).items():
            if str(self.probable.probability(v)) == str(trial_data.loc[k,self.model.column_to_work_on]):
                right += 1
            else:
                wrong += 1

        return right / (right + wrong)


# model = Model(r'C:\Users\User\Desktop\DATA\NaiveBayes\data_for_NB_buys_computer-Sheet1.csv','Buy_Computer','id')
# model = Model('phishing.csv','class','Index')


# tester = Trainer(model)

# print(tester.test())

