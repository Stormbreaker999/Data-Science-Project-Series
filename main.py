import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
import os
import pickle
filename='model.sav'
def algorithm():
    #Loading Data and refining it
    #We are going to use four attributes for training and our target column is TARGET
    df=pd.read_csv("infolimpioavanzadoTarget.csv")

    refined_data=df[['open', 'high', 'low', 'close']]

    print(refined_data.head())
    print(refined_data.isnull().sum())
    #Splitting Dataset
    #Making the close value of today as open value for tomorrow to make prediction
    X=refined_data.loc[:, 'open':'low']
    Y=refined_data.loc[:, 'close'].shift(-1)

    '''Plotting Data to Understand correlation'''
    figure, axis = plt.subplots(1, 3)
    axis[0].scatter(y=Y,x=X['open'])
    axis[1].scatter(y=Y, x=X['high'])
    axis[2].scatter(y=Y, x=X['low'])
    plt.show()

    #dropping last null value
    X=X.iloc[:X.shape[0]-1]
    Y=Y[:Y.shape[0]-1]



    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.25, random_state=16)

    #Starting the training using Linear Regression

    regressor=LinearRegression()
    regressor.fit(X_train, y_train)

    #Making Predictions
    Y_pred=regressor.predict(X_test)

    reg_score=regressor.score(X_test,y_test)
    return regressor

class SMPredictor:
    def __init__(self):
        self.regressor=algorithm()
    def predict(self, open, high, low):
        return self.regressor.predict(np.array([open, high, low]).reshape(1,-1))
    def __repr__(self):
        return "Regressor with parameters"+str(self.regressor.coef_)

class CreatePredictor(SMPredictor):
    def __init__(self):

        if not os.path.isfile(filename):
            super().__init__()
            pickle.dump(self.regressor, open(filename, 'wb'))
        else:
            #Asking user if he wants to train again
            train=str(input("Train Again(y/n):"))
            if train=='y':
                super().__init__()
                pickle.dump(self.regressor, open(filename, 'wb'))
            #Otherwise load parameters
            else:
                self.regressor=pickle.load(open(filename, 'rb'))


        print("Regressor created successfully")