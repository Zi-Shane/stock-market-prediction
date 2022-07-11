# %%
import numpy as np
import pandas as pd
import os

def split_sequence(sequence: pd.DataFrame, timestep: int):
    X = list()
    y = list()
    for i in range(sequence.shape[0] - timestep - 1):
        tmp = list()
        for j in range(timestep):
            tmp.append(sequence['Close'][i + j])
        
        X.append(tmp)
        y.append(sequence['Close'][i + timestep])
        
    return X, y


def split_sequence2(sequence: pd.DataFrame, timestep: int):
    
    return X, y


# %%
data = pd.read_csv(os.getcwd() + '/datasets/BRK-A.csv')
X, y = split_sequence(data[:10], 2)
print(X, y)

print(data[:10])
