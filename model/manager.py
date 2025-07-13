from model import Model
from trainer import Trainer
from inputs import Inputs


class Manager:

    def menu(self):
        print("Welcome to the program")
        path = input("enter path to the CSV file")
        column_to_work_on = input("Which column to work on ")
        columns_to_drop = drop_column_fun()
        try:
            model = Model(path, column_to_work_on, columns_to_drop)
            test = Trainer(model)
            if test.test() >= 0.9:
                ans = Inputs(model)
                return f"The answer to you query is: {ans.probability()}"
            else:
                return "Your dataset is not big enough, did not pass test"
        except:
            return "Un-valid model"


def drop_column_fun():
   drop_column = input("do you want to remove any columns? (y/n)")
   if drop_column not in ('y', 'n'):
       print("invalid input , try again")
       return drop_column_fun()
   elif drop_column == 'n':
       return None
   else:
       amount = int(input("How many"))
       if amount == 1:
           column = input("What column")
       else:
           print("put a comma between columns")
           column = list(input("what columns").split(","))
   return column



if __name__ == '__main__':
    manager = Manager()
    answ = manager.menu()
    print(answ)