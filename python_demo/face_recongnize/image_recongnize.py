# -*- coding:utf-8 -*-
#!/usr/bin/env python3
import dlib
import cv2
from datetime import datetime

img = cv2.imread('5.png')
cnn_face_detector = dlib.cnn_face_detection_model_v1('mmod_human_face_detector_1.dat')

t1=datetime.now()
dets = cnn_face_detector(img, 1)

print("num of face detected: {}".format(len(dets)))

for k, v in enumerate(dets):
	print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(k, v.rect.left(), v.rect.top(), v.rect.right(), v.rect.bottom()))

	face=dlib.rectangle(v.rect.left(), v.rect.top(), v.rect.right(), v.rect.bottom())
	cv2.rectangle(img, (face.left(), face.top() + 10), (face.right(), face.bottom()), (0, 255, 0), 2)
	cv2.imshow('image', img)
	
t2 = datetime.now()

print('time spend:', (t2 - t1).microseconds)
cv2.waitKey(0)
cv2.destroyAllWindows()
