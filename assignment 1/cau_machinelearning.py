# -*- coding: utf-8 -*-
"""cau_MachineLearning의 사본

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CVKTco3eyFtFKsUAroaAfU0HjG62pcxe
"""

import numpy as np

import matplotlib.pyplot as plt

m=100

x_point=np.random.uniform(low=0.0, high=100.0,size=m)

"""Randomized X"""

y_point=np.random.normal(0.0,5.0,m)

for i in range(0,m):
  y_point[i]=y_point[i]+x_point[i]*8+27

"""Randomized Y based on X, y=8*x+27+n (n is normal distribution)"""

y=8*x+27

"""the linear function _ y=8x+27"""

plt.scatter(x_point,y_point)