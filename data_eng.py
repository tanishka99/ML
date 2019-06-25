#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


#reading csv files from URL 
df=pd.read_csv('http://13.234.66.67/summer19/datasets/info.csv')


# In[3]:


df.info()


# In[4]:


df


# In[5]:


#
X=df.iloc[:,0:].values
X


# In[6]:


#removing missing values or replacing missing value with some relevant data
#df.describe()
from sklearn.preprocessing import Imputer


# In[7]:


imp=Imputer(missing_values='NaN',axis=0,strategy='mean')


# In[8]:


impute=imp.fit(X[:,1:3]) #this is only fitting of columns that we want to process


# In[9]:


# time for transforming the fitted columns transform-data nikalta h ,r fit-schema nikalta h
X[:,1:3]=impute.transform(X[:,1:3])


# In[10]:


X


# In[11]:


# string ko label krna int/float
from sklearn.preprocessing import LabelEncoder


# In[12]:


cont=LabelEncoder()  #this id for country labelling


# In[13]:


#now applying col frst in this label enc
X[:,0]=cont.fit_transform(X[:,0])


# In[14]:


X


# In[15]:


#labelling last column
p=LabelEncoder()


# In[16]:


X[:,3]=p.fit_transform(X[:,3])


# In[17]:


X


# In[18]:


#now encoding first column---making subcolumn of first column
from sklearn.preprocessing import OneHotEncoder


# In[19]:


firstcl=OneHotEncoder(categorical_features=[0])   #col no jispe kaam krvanan h,defining exact col no. where we wanna make category 


# In[22]:


X=firstcl.fit_transform(X).toarray()  #after transformation we need to convert into numpy array thus we used to array function


# In[24]:


X.astype(int) #to show in int only


# In[ ]:




