# test 4 - face detect 
# draw rectangle

import  cv2, dlib, sys
import numpy as np

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('../shape_predictor_68_face_landmarks.dat')

cap = cv2.VideoCapture('../face_detect_sample.mp4')
scaler = 0.3

while True:
    ret, img = cap.read()
    if not ret:
        break
        
    img = cv2.resize(img, (int(img.shape[1] * scaler), int(img.shape[0] * scaler)))
    ori = img.copy()
    
    # detect faces
    faces = detector(img)
    if len(faces) == 0:
        continue
    else:
        face = faces[0]
    
    # visualize
    img = cv2.rectangle(img, pt1=(face.left(), face.top()), pt2=(face.right(), face.bottom()), 
                        color=(255, 255, 255), thickness=2, lineType=cv2.LINE_AA)
    
    cv2.imshow('img', img)
    cv2.waitKey(30)