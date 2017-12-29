# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 18:23:49 2017

@author: sicher
"""
import pandas as pd
import sys
import math
from ggplot import *
import matplotlib.pyplot as plt

plt.style.use('ggplot')

input_file = sys.argv[1]

data_frame = pd.read_csv(input_file)
#print(data_frame.dropna(subset = ['Health Status']))
data_frame['Health Status'].fillna('A', inplace=True)
#print(data_frame)
df = data_frame[:]
for idx, row in data_frame.iterrows():
    if data_frame.loc[idx, 'Survival'] == 1:
        data_frame.loc[idx, 'Health Status'] = 'D'
#print(data_frame)
#print(df)
mask = (df['Survival'] == 1)
df.loc[mask, 'Health Status'] = 'D'
#print(df)
plt1 = ggplot(aes(x = 'Weeding', y='Height'), data=data_frame) + geom_boxplot() + xlab('Weeding treatment') + ylab('Height') + ggtitle('Test Plot')
print(plt1)
