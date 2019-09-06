from six.moves import input
import numpy as np
from os.path import dirname, join


#import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

import warnings
warnings.filterwarnings('ignore')

from sklearn.externals import joblib

def main():

    print("Predict Type of Iris Flower")
    print("=="*20)
    print("Please Enter Values in the required fields")
    print("=="*20)
    while True:
        try:
            try:
                sl = eval(input('sepal length (cm) : '))
            except Exception as e:
                print("Please Enter and Interger of Float")
                break
            print("*"*20)

            try:
                sw = eval(input('sepal width (cm) : '))
            except Exception as e:
                print("Please Enter and Interger of Float")
                break
            print("*"*20)

            try:
                pl = eval(input('petal length (cm) : '))
            except Exception as e:
                print("Please Enter and Interger of Float")
                break
            print("*"*20)

            try:
                pw = eval(input('petal width (cm): '))
            except Exception as e:
                print("Please Enter and Interger of Float")
                break
            print("*"*20)


            #data = load_iris()

            #x = data["data"]
            #y = data["target"]

            #clf = LogisticRegression(multi_class="ovr", solver="lbfgs")
            #clf.fit(x, y)
            file = join(dirname(__file__),"clf.pkl")
            clf = joblib.load(file)

            new = np.array([sl, sw, pl, pw]).reshape(1,-1)
            pred = clf.predict(new)

            if pred ==2:
                type =  'virginica'
            elif pred == 0:
                type = 'setosa'
            else:
                type = "versicolor"

        except EOFError:
            break
        if not sl:
            break
        #10print("Eponential of {} is {}!".format(name, exp))
        print("Predictior says the flower type is", type)
        print()
        proceed = input("Do you wish to continue : ")

        if proceed == "yes":
            continue

        elif proceed == "y":
            continue
        else:
            break
