from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt

iris=datasets.load_iris()
print(type(iris))
print(iris.keys())
print(iris.target_names)
X=iris.data
Y=iris.target
df=pd.DataFrame(X,columns=iris.feature_names)
print(df.head())
