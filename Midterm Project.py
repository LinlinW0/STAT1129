#!/usr/bin/env python
# coding: utf-8

# In[1]:


list=[2,4,6,8,4,5,2,1,9,0,4,
      6,7,4,3,2,1,9,10,3,7,9,
      6,0,1,3,5,6,7,8,9,10,2,
      3,6,8,9,10,6,7,4,3]
list.sort()
frequency={}
for i in list:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
for key,value in frequency.items():
    print(key,":",value)


# In[2]:


import matplotlib.pyplot as plt
import numpy as np

plt.hist(list)
plt.show()


# In[4]:


#convert to json
import json
y=json.dumps(frequency)
print(y)


# In[5]:


#create a new file and store it
f=open("Midterm.txt","w")
f.write(y)
f.close()


# In[6]:


#Q2
import pandas as pd
df=pd.read_csv('Amazon-orders.csv')
df.head()


# In[7]:


df.shape


# In[8]:


df=df.fillna(0)
df.head()


# In[9]:


df["Item Total"]=df["Item Total"].str.replace('$','').astype(float)
df.head()


# In[10]:


df["Item Total"].sum()


# In[11]:


df["Item Total"].mean()


# In[12]:


df["Item Total"].median()


# In[13]:


df["Item Total"].max()


# In[14]:


df["Item Total"].min()


# In[15]:


df['Order Date']=pd.to_datetime(df['Order Date'])
df.head()


# In[16]:


df.plot.scatter(x='Order Date',y='Item Total',title='Item Total Per Day',rot=90)


# In[17]:


monthly_order=df.groupby(pd.Grouper(key='Order Date',freq='1M')).sum()["Item Total"]


# In[18]:


monthly_order.plot.bar(figsize=(20,10))

