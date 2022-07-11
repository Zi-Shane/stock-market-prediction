# %%
import numpy as np
import pandas as pd
import os

def split_sequence2(sequence: pd.DataFrame, timestep: int) -> tuple[list[list[int]], list[int]]:
    X = list()
    y = list()
    for i in range(sequence.shape[0] - timestep - 1):
        tmp = list()
        for j in range(timestep):
            tmp.append(sequence['Close'][i + j])
        
        X.append(tmp)
        y.append(sequence['Close'][i + timestep])
        
    return X, y


def split_sequence(sequence: pd.DataFrame, timestep: int):
    X = list()
    y = list()
    for i in range(len(sequence)):
        end_idx = i + timestep
        if end_idx > len(sequence) - 1:
            break
        seq_x, seq_y = sequence['Close'][i:end_idx].to_numpy(), sequence['Close'][end_idx]
        X.append(seq_x)
        y.append(seq_y)
    return np.array(X), np.array(y)


# %%
data = pd.read_csv(os.getcwd() + '/datasets/BRK-A.csv')
X, y = split_sequence2(data[:10], 2)

for a, b in zip(X, y):
    print(a, b)

# print(data['Close'][:10])
