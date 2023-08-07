import numpy as np
import cv2
import pyautogui
from tkinter import *

def normalize(x):
  minn, maxx = x.min(), x.max()
  return (x - minn) / (maxx - minn)

def scan(video_capture,cascade,image_size=(32, 32)):
  _, frame = video_capture.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  boxes = cascade.detectMultiScale(gray, 1.3, 10)
  if len(boxes) == 2:
    eyes = []
    for box in boxes:
      x, y, w, h = box
      eye = frame[y:y + h, x:x + w]
      eye = cv2.resize(eye, image_size)
      eye = normalize(eye)
      eye = eye[10:-10, 5:-5]
      eyes.append(eye)
    return (np.hstack(eyes) * 255).astype(np.uint8)
  else:
    return None
  
def return_resolution():
    RES_SCREEN = pyautogui.size() 
    # RES_SCREEN[0] -> width
    # RES_SCREEN[1] -> height
    width, height = RES_SCREEN[0],RES_SCREEN[1] 
    return width,height