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

plt.style.use('ggplot')

input_file = sys.argv[1]

data_frame = pd.read_csv(input_file)
plot_data = data_frame.query('Height == Height')
sns.distplot(plot_data['Height'], bins = 20, kde = False,\
             rug=True, label="Histogram w/o Density")
plt.show()