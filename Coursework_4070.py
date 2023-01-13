#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
df=pd.read_csv('CO2_emission.csv',encoding='latin-1')
df.head()


# In[11]:


df.columns


# In[13]:


df.info()


# In[14]:


df.describe()


# In[88]:


df.isnull().sum()


# In[89]:


sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')


# In[124]:


df_ev=pd.read_csv('ElectricCarPrices.csv',encoding='latin-1')
df_ev.head(12)


# In[122]:


final_df=pd.merge(df,df_ev,on='Year',how='left')


# In[ ]:





# In[ ]:


df.drop


# In[68]:


plt.pie(country_val[:10],labels=country_names[:10])

