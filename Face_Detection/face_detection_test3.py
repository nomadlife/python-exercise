# test 3
import  cv2, dlib, sys
import numpy as np

cap = cv2.VideoCapture('face_detect_sample.mp4')
scaler = 0.3

while True:
    ret, img = cap.read()
    if not ret:
        break
        
    img = cv2.resize(img, (int(img.shape[1] * scaler), int(img.shape[0] * scaler)))
    
    cv2.imshow('img', img)
    cv2.waitKey(30)