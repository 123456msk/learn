import torch
import matplotlib.pyplot as plt
import random

def synthetic_data(w,b,nums_examples):
    X = torch.normal(0,1,(nums_examples,len(w)))
    y = torch.matmul(X,w) + b
    y += torch.normal(0,0.01,y.shape)
    return X,y.reshape(-1,1)

true_w = torch.tensor([2,-3.4])
true_b = 4.2

features,labels = synthetic_data(true_w,true_b,nums_examples=1000
                                 )