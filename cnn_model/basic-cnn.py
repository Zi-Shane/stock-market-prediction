import tensorflow as tf
import numpy as np
import pandas as pd
import os

# fix Could not create cudnn handle: CUDNN_STATUS_NOT_INITIALIZED
# Could not create cudnn handle: CUDNN_STATUS_NOT_INITIALIZED
physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], enable=True)

n_steps = 5
n_features = 1

model = tf.keras.Sequential()
model.add(tf.keras.layers.Conv1D(filters=64, kernel_size=3, strides=1, input_shape=(n_steps, n_features)))
model.add(tf.keras.layers.MaxPool1D(pool_size=2))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(50, activation='relu'))
model.add(tf.keras.layers.Dense(1))

model.compile(optimizer='adam', loss='mse')


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


data = pd.read_csv('/home/shane/python-workspaces/stock-market-prediction/datasets/BRK-A.csv')

X, y = split_sequence(data[:-1000], n_steps)
# X.shape (10000, 5)
# y.shape (10000, 1)

# batch, n_steps, n_features
X = X.reshape(X.shape[0], X.shape[1], n_features)
# X.shape (10000, 5, 1)


# ---printout---
# for a, b in zip(X, y):
#     print(a, b)

# print(data['Close'][:10])

model.fit(X, y, epochs=10)
