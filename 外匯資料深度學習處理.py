#!/usr/bin/env python
# coding: utf-8

# In[9]:


#載入需要的套件
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import *
from statsmodels.tsa import stattools


get_ipython().run_line_magic('matplotlib', 'inline')

#載入過去五年的歐元兌美元匯率資料
FX_data = pd.read_csv(r'C:\Users\npc94\OneDrive\桌面\EURUSD=X.csv',index_col=0,parse_dates=True)


# In[11]:


import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense

#https://keras.io/zh/optimizers/


# In[12]:


tf.keras.optimizers.Adam(
    learning_rate=0.001)


# In[13]:


def set_seeds(seed=100):
    random.seed(seed)
    np.random.seed(seed)
    tf.random.set_seed(100)


# In[14]:


set_seeds()
model = Sequential()
model.add(Dense(64, activation='relu',
        input_shape=(lags,)))
model.add(Dense(64, activation='relu'))
model.add(Dense(1, activation='sigmoid')) # <5>
model.compile(optimizer=optimizer,
              loss='binary_crossentropy',
              metrics=['accuracy'])


# In[ ]:


#https://medium.com/analytics-vidhya/ml-classification-algorithms-to-predict-market-movements-and-backtesting-2382fdaf7a32
    
#https://medium.com/analytics-vidhya/keras-tensorflow-to-predict-market-movements-and-backtest-using-backtrader-d51b0b3e9070

