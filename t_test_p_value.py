#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 17:17:59 2018
"""

#https://machinelearningmastery.com/use-statistical-significance-tests-interpret-machine-learning-results/

from pandas import read_csv
from scipy.stats import ttest_ind

# load results1
result1 = read_csv('Sig1.csv', header=None)
values1 = result1.values[:,0]
# load results2
result2 = read_csv('Sig2.csv', header=None)
values2 = result2.values[:,0]
# calculate the significance
value, pvalue = ttest_ind(values1, values2)
#value, pvalue = ks_2samp(values1, values2)

print(value, pvalue)
if pvalue > 0.05:
	print('Samples are likely drawn from the same distributions (fail to reject H0)')
else:
	print('Samples are likely drawn from different distributions (reject H0)')
    
