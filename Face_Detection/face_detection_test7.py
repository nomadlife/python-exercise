# test 7 - center of face

import  cv2, dlib, sys
import numpy as np

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('../shape_predictor_68_face_landmarks.dat')

cap = cv2.VideoCapture('../face_detect_sample.mp4')
scaler = 0.5

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
    
    dlib_shape = predictor(img, face)
    shape_2d = np.array([[p.x, p.y] for p in dlib_shape.parts()])

    # compute center of face
    top_left = np.min(shape_2d, axis=0)
    bottom_right = np.max(shape_2d, axis=0)

    center_x, center_y = np.mean(shape_2d, axis=0).astype(np.int)

    # visualize
    img = cv2.rectangle(img, pt1=(face.left(), face.top()), pt2=(face.right(), face.bottom()), 
                        color=(255, 255, 255), thickness=2, lineType=cv2.LINE_AA)
    
    for s in shape_2d:
        cv2.circle(img, center=tuple(s), radius=1, color=(255,255,255), thickness=2, lineType=cv2.LINE_AA)

    cv2.circle(img, center = tuple(top_left), radius=1, color=(255,0,0), thickness=2, lineType=cv2.LINE_AA)
    cv2.circle(img, center = tuple(bottom_right), radius=1, color=(255,0,0), thickness=2, lineType=cv2.LINE_AA)
    cv2.circle(img, center = tuple((center_x, center_y)), radius=1, color=(0,0,255), thickness=2, lineType=cv2.LINE_AA)

    cv2.imshow('img', img)
    cv2.waitKey(10)