# importing libraries
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor 
from sklearn.datasets import  load_iris
from sklearn.model_selection import train_test_split

def flower(sepal_length_,sepal_width_,
petal_length_,
petal_width_):
    iris= load_iris()
    iris.target_names
    iris.data
    iris_df=pd.DataFrame(iris.data,columns=iris.feature_names)


    y=iris.target
    from sklearn.model_selection import train_test_split

    # regt=DecisionTreeRegressor()

    x=iris_df
    xtrain,xtest ,ytrain,ytest =train_test_split(x,y,train_size=0.8,random_state=4)

    # regt.fit(xtrain,ytrain)

    # path=regt.cost_complexity_pruning_path(xtrain,ytrain)

    # ccp_alphas, impurities = path.ccp_alphas, path.impurities

    regt=DecisionTreeRegressor(random_state=4,ccp_alpha=0.01)
    regt.fit(xtrain.values,ytrain)

    xtest= np.array([sepal_length_,
                        sepal_width_,
                        petal_length_,
                        petal_width_]
                        )
    xtest= xtest.reshape(1,4)

    return regt.predict(xtest)
