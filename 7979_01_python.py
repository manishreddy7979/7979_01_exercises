#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt


# In[6]:


#B1
#data=pd.read_csv('imdb.csv',escapechar='\\')
def que1(data):
    data['GenereCombo']=data[data.columns[16:]].T.apply(lambda x: '|'.join(x.index[x==1]),axis=0)
    ans=data.groupby(["type","year","GenereCombo"]).agg({"imdbRating":['min','max','mean'],"duration":['sum']})
    return ans
#que1(data)


# In[9]:


#B2-1
#data=pd.read_csv("imdb.csv",escapechar='\\')
def que21(data):
    data['Title_Length']=data['title'].apply(lambda x:len(x.split('(')[0].replace(" ","").rstrip()))
    rel=data['Title_Length'].corr(data['imdbRating'])
    return rel
#que21(data)


# In[13]:


#B2-2
#data=pd.read_csv("imdb.csv",escapechar='\\')
def que22(data):
    data['Title_Length']=data['title'].apply(lambda x:len(x.split('(')[0].replace(" ","").rstrip()))
    data['quantile']=pd.qcut(data['Title_Length'],4,labels=False)
    df1=pd.crosstab(data['year'],data['quantile'],margins=False)
    df1['min']=data.groupby('year')['Title_Length'].min()
    df1['max']=data.groupby('year')['Title_Length'].max()
    return df1
#que22(data)


# In[14]:


#B3
#df=pd.read_csv("diamonds.csv")
def que3(df):
    df['z']=df['z'].apply(pd.to_numeric,errors='coerce')
    df['volume']=df.apply(lambda df: df['x']*df['y']*df['z'] if df['depth']>60 else 8,axis=1)
    df["bin"]=pd.qcut(df["volume"],q=5,labels=['1','2','3','4','5'])
    a=pd.crosstab(df["bin"],df["cut"],normalize='columns')
    return a
#que3(df)


# In[15]:


#B4
#df=pd.read_csv("movie_metadata.csv",escapechar="\\")
def que4(df):
    ans=pd.DataFrame()
    hh=df['title_year'].unique()
    for x in hh:
        a=df[(df['title_year']==x)]
        b=a.sort_values(by=['gross'], ascending=False)
        g=b.head(round(len(a)*0.10))
        ans=ans.append(g)
    q=ans.groupby('title_year').agg({'imdb_score':'mean','movie_title':'unique'})
    return q
#que4(df)


# In[16]:


#B5
#data=pd.read_csv("imdb.csv",escapechar='\\')
def que5(data):
    data["decile"]=pd.qcut(data["duration"],10,labels=False)
    x=data.groupby("decile")[["nrOfNominations","nrOfWins"]].sum()
    x["count"]=data.groupby("decile")["year"].count()
    y=data.iloc[:,16:47]
    z=y.groupby("decile")[y.columns[1:28]].sum()
    z=z.transpose()
    e=z.apply(lambda x: x.nlargest(3).index,axis=0).transpose()
    x["top genres"]=e[0]+","+e[1]+","+e[2]
    return x
#que5(data)


# In[17]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[18]:


data = pd.read_csv("movie_metadata.csv")


# In[19]:


data_groupby_gross = data.groupby(['title_year'])['gross'].count()
data_groupby_gross.plot()


# In[20]:


data_groupby_duration = data.groupby(['duration'])['movie_title'].count()
data_groupby_duration.plot()


# In[21]:


print(data['content_rating'].value_counts())
data_content_rating=data['content_rating'].value_counts(dropna=False)
data_content_rating.plot(kind="bar")


# In[22]:


sns.heatmap(data.corr())


# In[23]:


sns.factorplot(y='imdb_score',kind='box',data=data)


# In[ ]:




