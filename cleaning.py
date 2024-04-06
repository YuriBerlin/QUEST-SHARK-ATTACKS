#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


def clean(df):
    df.columns = df.columns.str.lower().str.replace(" ", "")
    df.drop(columns=['source','name','pdf','href','hrefformula','unnamed:11','casenumber', 'casenumber.1', 'originalorder', 'unnamed:21', 'unnamed:22'], inplace=True)
    df.dropna(how ='all', inplace=True)
    df['year'] = df['year'].apply(lambda i: int(i) if pd.notna(i) else i)
    df.injury = df.injury.apply(lambda i: "unknown" if pd.isna(i) else i)
    df.injury = df.injury.apply(lambda i: str(i))
    df.injury = df.injury.apply(lambda i: i.lower())
    df.age_numeric = pd.to_numeric(df.age, errors='coerce')
    return df

