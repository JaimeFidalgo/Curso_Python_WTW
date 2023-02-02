#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# 1.0 DataFrame and Series Definition

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# 2.0 DataFrame Creation 

# 2.1 Dictionary

# In[4]:


dict = {
        "name":["Pedro","Antonio","Ángela","María"],
        "edad": [18,54,25,42],
        "email": ["pedro@gmail.com","antonio@hotmail.com","angela@yahoo.com","maria@icloud.com"]}
dict


# In[5]:


df = pd.DataFrame(dict)


# In[6]:


df


# 2.2 n-array

# In[8]:


n_darray = [["name","edad","email"],
["Pedro",18,"pedro@gmail.com"],
["Antonio",54,"antonio@hotmail.com"],
["Ángela",25,"angela@yahoo.com"],
["María",42,"maria@icloud.com"]]


# In[9]:


n_darray


# In[10]:


df_1 = pd.DataFrame(n_darray)


# In[11]:


df_1


# In[22]:


headers = n_darray[0]
headers


# In[23]:


body = n_darray[1:]


# In[24]:


body


# In[25]:


df_1= pd.DataFrame(body, columns = headers)


# In[26]:


df_1


# 3.0 Get header list from DataFrame

# In[27]:


df.columns


# In[29]:


headers = df.columns.tolist()


# In[30]:


headers


# 4.0 Size of DataFrame

# In[31]:


df.shape


# In[32]:


nrows = df.shape[0]
ncols= df.shape[1]


# In[34]:


nrows


# In[35]:


ncols


# 5.0 Create DataFrame from csv

# In[38]:


df_2 = pd.read_csv("createdf.csv", sep= ",")


# In[39]:


df_2


# In[40]:


df_2.to_excel("createdf.xlsx")


# 6.0 read from excel

# In[41]:


df_3 = pd.read_excel("createdf.xlsx")


# In[42]:


df_3


# 7.0 Write df to csv

# In[44]:


df_3.to_csv("writecsv.csv", index = False)


# 8.0 Write df to excel

# In[47]:


df_3.to_excel("writeexcel.xlsx", index = False)


# 9.0 Select data from df
# 

# 9.1 loc

# In[48]:


df_loc = df_3.loc[0,"email"]


# In[49]:


df_loc


# In[51]:


df_loc = df_3.loc[[0,1],["name","email"]]


# In[52]:


df_loc


# In[57]:


df_loc = df_3.loc[1:,["edad","email"]]


# In[58]:


df_loc


# 9.1 iloc

# In[59]:


df_iloc = df_3.iloc[0,1]


# In[60]:


df_iloc


# In[61]:


df_iloc = df_3.iloc[0,[1,2]]


# In[62]:


df_iloc


# In[69]:


df_iloc = df_3.iloc[1:,1:]


# In[70]:


df_iloc


# 10.0 Filters

# In[71]:


df


# In[73]:


filter = df["edad"] > 26


# In[74]:


filter


# In[75]:


df[filter]


# In[76]:


df[df["edad"] > 26]


# 11.0 Sorting

# In[82]:


df_sorted = df.sort_values(by="edad", ascending = False)


# In[83]:


df_sorted


# In[90]:


df_sorted = df.sort_values(by=["edad","name"], ascending = [True,False])


# In[91]:


df_sorted


# 12.0 Add and Delete Columns

# In[92]:


df["estudios"] = ["actuario","ingeniero","medico","profesor"]


# In[93]:


df


# In[107]:


df.drop("estudios", axis=1, inplace = True)


# In[108]:


df


# In[111]:


df.loc[df.shape[0]] = ["Jesus", 10 , None]


# In[112]:


df


# In[114]:


df.drop(df.shape[0]-1, axis = 0)


# In[115]:


headers = df.columns


# 14.0 Loops over columns

# In[122]:


for i in headers:
    
    if (df.loc[:,i].dtype == "object"):
        print(df.loc[:,i].str.upper())
    


# 15.0 Loops over rows

# In[123]:


df


# In[127]:


for i in range(df.shape[0]):
    a = df.iloc[i].tolist()
    if ("Antonio" in a):
        print(a)
    else:
        print("no antonio")
   
    


# In[ ]:




