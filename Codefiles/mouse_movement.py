import numpy as np
from keras import *
from keras.layers import *
from helpers import *
from keras.models import load_model
import time
import os

######## Run Mouse Pointer for t seconds ########
rootdir='Eyenetic/Codefiles'
t=10
cascade = cv2.CascadeClassifier(rootdir+"/haarcascade_eye.xml")
video_capture = cv2.VideoCapture(0)
width, height = return_resolution()
model=load_model(rootdir+'/model.h5')

begin = time.time()
while True:
  
  eyes = scan(video_capture, cascade)
  if not eyes is None:
    eyes = np.expand_dims(eyes / 255.0, axis = 0)
    x, y = model.predict(eyes, verbose=0)[0]
    pyautogui.moveTo(x * width, y * height)
  if time.time()- begin > t:
    break
video_capture.release()
cv2.destroyAllWindows()
