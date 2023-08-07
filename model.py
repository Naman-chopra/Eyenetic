import numpy as np
from keras import *
from keras.layers import *
from helpers import *
import time
import os

root='Eyenetic/image/'
print (root)

width, height = return_resolution()

filepaths = os.listdir(root)
X, Y = [], []
for filepath in filepaths:
  x, y, _ = filepath.split(' ')
  x = float(x) / width
  y = float(y) / height
  X.append(cv2.imread(root + filepath))
  Y.append([x, y])
X = np.array(X) / 255.0
Y = np.array(Y)
print (X.shape, Y.shape)

model = Sequential()
model.add(Conv2D(32, 3, 2, activation = 'relu', input_shape = (12, 44, 3)))
model.add(Conv2D(64, 2, 2, activation = 'relu'))
model.add(Flatten())
model.add(Dense(32, activation = 'relu'))
model.add(Dense(2, activation = 'sigmoid'))
model.compile(optimizer = "adam", loss = "mean_squared_error")
model.summary()

epochs = 200
clk = time.time()
for epoch in range(epochs):
  model.fit(X, Y, batch_size = 32)
  print (f"Epoch {epoch + 1}/{epochs}")
clk = time.time() - clk
clk = round(clk, 2)
print (f"Training took {clk} seconds")
