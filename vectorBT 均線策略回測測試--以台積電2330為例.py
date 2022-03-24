#!/usr/bin/env python
# coding: utf-8

# ## 載入相關套件

# In[1]:


import vectorbt as vbt


# In[2]:


from numba import njit


# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ## 從Yahoo finance下載股價資料，載入過去五年台積電(2330)收盤資料

# In[4]:


data = pd.read_csv(r'C:\Users\npc94\OneDrive\桌面\2330.TW.csv',index_col=0,parse_dates=True)

price= data['Close']


# In[5]:


data.head()


# In[6]:


data.tail()


# ## 設定資料頻率為"日"，並設定交易策略為20天均線和60天均線策略

# In[7]:


vbt.settings.array_wrapper['freq'] = 'd'
risk_free=0.01

sma20 = price.rolling(20).mean()
sma60 = price.rolling(60).mean()
entries = (sma20 > sma60) & (sma20.shift() < sma60.shift())
exits = (sma20 < sma60) & (sma20.shift() > sma60.shift())

pf= vbt.Portfolio.from_signals(price, entries, exits, fees=0.001425,init_cash=10000) #設定交易稅為千分之1.425以及初始資金為10000


# ## 投資部位變動繪製

# In[8]:


price.plot()
sma20.plot()
sma60.plot()
entries.astype(int).plot(secondary_y=True,figsize=(10,6))
(-exits.astype(int)).plot(secondary_y=True,figsize=(10,6))


# ## 交易進出資料

# In[9]:


pf.orders.records_readable


# ## 交易圖表繪製

# In[10]:


fig = price.vbt.plot(trace_kwargs=dict(name='Close'))
sma20.vbt.plot(trace_kwargs=dict(name='Fast MA'), fig=fig)
sma60.vbt.plot(trace_kwargs=dict(name='Slow MA'), fig=fig)
pf.positions.plot(close_trace_kwargs=dict(visible=False), fig=fig)


# ## 交易獲利統計

# In[11]:


pf.total_profit()


# ## 交易數據圖表統計

# In[12]:


pf.stats()

