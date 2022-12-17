import numpy as np


def sigmoid(x):
    return 1/(1+np.exp(-x))

def Y(x,theeta):
    return np.dot(x,theeta)

def value(x,theeta):
    return sigmoid(Y(x,theeta))

def cost(x,theeta,y):
    m=x.shape[0]
    data= -(1/2*m)*(np.sum(y*np.log(value(x,theeta))+(1-y)*np.log(1-value(x,theeta))))
    return data

