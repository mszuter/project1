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
from statsmodels.formula.api import ols, glm

plt.style.use('ggplot')

input_file = sys.argv[1]

data_frame = pd.read_csv(input_file)
plot_data = data_frame.query(('Height == Height & Lateral_Branches == Lateral_Branches'))
#sns.distplot(plot_data['Height'], bins = 20, kde = False,\
#             rug=True, label="Histogram w/o Density")
#plt.show()

#sns.factorplot(x='Weeding', y='Height',hue='Fence',\
#               data=plot_data, kind='box')
#plt.legend(loc="best")
print(plot_data)
sns.lmplot(x='Height', y='Lateral_Branches', data=plot_data)
y=plot_data['Lateral_Branches']
X=sm.add_constant(plot_data['Height'])
lm = sm.OLS(y, X).fit()
print(lm.summary())

##Plot the data with histograms
sns.jointplot(x='Height', y='Lateral_Branches', data=plot_data, kind='reg')


##Poisson regression on lateral branches (count data)
pois_reg = glm('Lateral_Branches~Height', data=plot_data, family=sm.families.Poisson()).fit()
print(pois_reg.summary())
print("\nQuantities you can extract from lm:\n%s" % dir(pois_reg))
print("\nCoefficients:\n%s" % pois_reg.params)
print(pois_reg.predict())
plot_data['PoissonPredictions'] = pd.Series(pois_reg.predict(), index=plot_data.index)

sns.lmplot(x='Height', y='PoissonPredictions', data=plot_data)
plt.show()