import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
df=pd.read_csv('/content/ht.csv')
df.head()
from sklearn.impute import SimpleImputer
im = SimpleImputer(missing_values= np.nan, strategy='mean')
phvalue = df[['pH']]
df['pH']=im.fit_transform(phvalue)
df.dropna()
from sklearn.preprocessing import LabelEncoder
lc=LabelEncoder()
df['Crop']=lc.fit_transform(df['Crop'])
df['Fertilizer']=lc.fit_transform(df['Fertilizer'])

df1= df.copy()
x=df1[['Nitrogen','Phosphorus','Potassium','pH','Crop']]
y=df1[['Fertilizer']]
from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=0.85,test_size=0.15,random_state=10)

from sklearn.ensemble import RandomForestClassifier

model=RandomForestClassifier(n_estimators=500,max_depth=30,min_samples_split=2,min_samples_leaf=2,max_features='sqrt',random_state=40)
model.fit(x_train,y_train)

joblib.dump(model,'model.pkl')


