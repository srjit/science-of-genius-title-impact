import numpy as np


def calculate(X,Y,bins):

   c_XY = np.histogram2d(X,Y,bins)[0]
   c_X = np.histogram(X,bins)[0]
   c_Y = np.histogram(Y,bins)[0]

   H_X = shannon_entropy(c_X)
   H_Y = shannon_entropy(c_Y)
   H_XY = shannon_entropy(c_XY)

   MI = H_X + H_Y - H_XY
   return MI


def shannon_entropy(c):
    c_normalized = c / float(np.sum(c))
    c_normalized = c_normalized[np.nonzero(c_normalized)]
    H = -sum(c_normalized* np.log2(c_normalized))  
    return H
