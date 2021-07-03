import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
import seaborn as sns
##https://raw.githubusercontent.com/DUanalytics/datasets/master/csv/denco.csv
url="https://raw.githubusercontent.com/DUanalytics/datasets/master/csv/denco.csv"
df=pd.read_csv(url)
df
df.shape
df.columns
df.head(3)
len(df)
df.dtypes
pd.options.display.float_format ='{:.2f}'.format
df
df.describe( )
df['region']= df['region'].astype( 'category')
df['region']
df.describe()
df.region.value_counts()
df.region.value_counts().plot(kind='bar')
df.custname.value_counts().sort_values(ascending=False).head(5)
df.custname.value_counts().sort_values(ascending=True).head(5)
df.custname.value_counts().sort_values(ascending=False).tail(5)
########
df.groupby('custname').size().sort_values(ascending=False).head(5)
df.groupby('custname').revenue.sum().sort_values(ascending=False).head(5) 
#########aggregate function is used
df.groupby('custname').agg({'revenue':[np.sum,max,min,'count']}).head(5)
#############sort by
df.groupby('custname')['revenue'].aggregate([np.sum,max,min,'count'])
df.groupby('custname')['revenue'].aggregate([np.sum,max,min,'count']).sort_values(by='count')
#####which part numbers bringing in to significant portion of revenue
df.groupby('partnum')['revenue'].aggregate([np.sum,'count',max,min]).head(5).sort_values(by='count')
df.groupby('partnum').agg({'revenue':[np.sum,max,min,'count']}).head(5)
df.groupby('partnum')['revenue'].agg([np.sum,max,min,'count']).sort_values(by='sum',ascending=False).head(5)
####top profit making companies
df.groupby('partnum')['margin'].agg([np.sum,max,min,'count']).sort_values(by='sum',ascending=False).head(5)
df.groupby('partnum').size().sort_values(ascending=False).head(5)
####REGIONS GIVING MAXIMUM REVENUE
df[['revenue','region']].groupby('region').revenue.max().sort_values(ascending=False).head(5).plot(kind='barh') 
######barh {h-horizontal}