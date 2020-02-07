import  cv2, dlib, sys
import numpy as np

cap = cv2.VideoCapture('../face_detect_sample.mp4')
ret, img = cap.read()
print(ret)
print(len(img))
print(dlib.__version__)