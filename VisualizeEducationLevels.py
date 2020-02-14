##load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

#load file and check first five rows
df = pd.read_csv(r'C:\Users\dveras\Documents\train.csv')
df.head()

##create new dataframe with just 3 columns
new = df[['age','income_level','education']].copy()

#calculate count of each education level
count = new['education'].value_counts()

##transform this calculation into standalone dataframe
count2 = count.to_frame()

##plot results into horizontal bar graph
ax = count2.plot.barh(rot=0)
