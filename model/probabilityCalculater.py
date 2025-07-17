

class ProbabilityCalculater:
    def __init__(self,model):
        self.model = model
        self.dict_values = self.model.dict_values()
        self.dict_class_values = self.model.dict_class()

    def probability(self,input_dict):
        """ calculate the probability for dict of option """
        prob_dict = {}
        # mult probability for each option column
        for keys in self.dict_values:
            probability = 1
            for key, value in input_dict.items():
                if self.dict_values[keys][key][value] != 0 :
                    probability *= self.dict_values[keys][key][value]
                # add 1 if found 0
                else:
                    self.dict_values[keys][key][value] += 1
                    probability *= self.dict_values[keys][key][value]
                prob_dict[keys] = probability * self.dict_class_values[keys]
        return max( prob_dict,key=prob_dict.get)


