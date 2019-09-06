from six.moves import input
import numpy as np

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

def main():

    print("Predict Type of Iris Flower")
    print("=="*20)
    print("Please Enter Values in the required fields")
    print("=="*20)
    while True:
        try:
            sl = eval(input('sepal length (cm) : '))
            print("*"*20)
            sw = eval(input('sepal width (cm) : '))
            print("*"*20)
            pl = eval(input('petal length (cm) : '))
            print("*"*20)
            pw = int(input('petal width (cm): '))
            print("*"*20)


            data = load_iris()

            x = data["data"]
            y = data["target"]

            clf = LogisticRegression(multi_class="ovr", solver="lbfgs")
            clf.fit(x, y)

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
        print("Prediction says the flower type Is", type)

        break

