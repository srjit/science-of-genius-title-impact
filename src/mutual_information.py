import numpy as np
import math


def get_number_of_bins(length):
    ## optimal number of bins
    ## https://stats.stackexchange.com/questions/179674/number-of-bins-when-computing-mutual-information
    return math.floor(np.sqrt(length/5))


def calculate(X,Y):
    
   #bins = get_number_of_bins(len(X))
   bins = 6
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
