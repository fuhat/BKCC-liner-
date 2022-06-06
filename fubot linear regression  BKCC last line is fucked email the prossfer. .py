#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np 
import pandas as pd 
import matplotlibpyplot as plt
import seaborn
sb.set()
import datetime as dt 


# In[3]:


import matplotlib.pyplot as plt


# In[5]:


import seaborn as sb
sb.set()


# In[6]:


import datetime as dt


# In[7]:


import pandas_datareader as pdr


# In[51]:


stocks = "GOOG BKCC".split()
start = dt.date.today()- dt.timedelta(365)


# In[52]:


data = pdr.get_data_yahoo(stocks, start)["Close"]
data.tail()


# In[53]:


returns= np.log(data).diff()
returns.head()


# In[54]:


returns.corr()


# In[57]:


sample= returns.sample(60).corr()


# In[58]:


sample


# In[61]:


sameple = returns.sample(60).corr()
plt.scatter(x=sample['GOOG'], y=sample['BKCC']);


# In[65]:


reg = np.polyfit(sample['BKCC'], sample['GOOG'], deg=1)


# In[67]:


reg


# In[68]:


trend = np.polyval(reg,sample['BKCC'])
plt.scatter(sample['BKCC'],sample['GOOG'])
plt.plot(sample['BKCC'], trend );


# In[69]:


data = pd.DataFrame(pdr.get_data_yahoo('BKCC', start)['Close'])
time =np.arange(1, len(data) + 1)
data['time'] = time
data = data[['time' , 'Close']]
data.tail()


# In[70]:


reg = np.polyfit(data['time'], data['Close'], deg = 1)
reg


# In[71]:


tend= np.polyval(reg,data['time'][-63:])
std = data['Close'][-63:].std()
plt.figure(figsize=(10,6))
plt.plot(data['time'], data['Close'], label="BKCC")
plt.plot(data['time'][-63:], trend, 'r--')


# In[ ]:




