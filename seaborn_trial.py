# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 15:03:00 2017

@author: sicher
"""
import seaborn as sns
import pandas as pd
import sys
import math
#from ggplot import *
import matplotlib.pyplot as plt
import statsmodels.api as sm

plt.style.use('ggplot')

input_file = sys.argv[1]

data_frame = pd.read_csv(input_file)
plot_data = data_frame.query(('Height == Height & Lterl_Brnches == Lterl_Brnches'))
#sns.distplot(plot_data['Height'], bins = 20, kde = False,\
#             rug=True, label="Histogram w/o Density")
#plt.show()

#sns.factorplot(x='Weeding', y='Height',hue='Fence',\
#               data=plot_data, kind='box')
#plt.legend(loc="best")
print(plot_data)
sns.lmplot(x='Height', y='Lterl_Brnches', data=plot_data)
y=plot_data['Lterl_Brnches']
X=sm.add_constant(plot_data['Height'])
lm = sm.OLS(y, X).fit()
print(lm.summary())
plt.show()
