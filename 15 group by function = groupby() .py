#!/usr/bin/env python
# coding: utf-8

# ### what is pandas groupby fuction?
# #### pandas groupby function is used to split the data into groups based on some criteria.
# 
# #syntax = DataFrame.groupby()
# 
# ### Any groupby opration involves one of the following oprations on the original object:
# 
# 
# - Splitting the object
# - Applying a function
# - Combining the result

# In[1]:


import pandas as pd


# In[3]:


df = pd.read_csv(r'B:\Worked dataset\student_results.csv')
df


# In[4]:


gr1 = df.groupby(by = 'Section')
gr1


# In[7]:


gr1.groups


# In[11]:


df.groupby(by =['Class', 'Section']).groups


# In[ ]:





# In[8]:


gr2 = df.groupby(by =['Class', 'Section'])
gr2


# In[10]:


gr2.groups


# In[ ]:





# In[14]:


for Section, df_1 in gr2:
    print(Section)
    print(df_1)  #print as key and values wise


# In[15]:


list(gr2)


# In[16]:


dict(list(gr1))


# In[19]:


gr3 = df.groupby('Class').get_group(10)
gr3 


# In[22]:


gr4 = df.groupby('Section').get_group('A')
gr4 


# In[23]:


gr1.sum()


# In[24]:


gr1.mean()


# In[26]:


gr1.describe()


# In[27]:


gr1.agg(['sum','max','mean'])


# In[ ]:




