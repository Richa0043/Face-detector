# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 14:59:00 2019

@author: Richa Rani
"""

import cv2


cap=cv2.VideoCapture(0)
hand_cascade = cv2.CascadeClassifier('hand.xml')
while(True):
    ret,frame = cap.read()
    gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    hands= hand_cascade.detectMultiScale(gray,1.1,5)
    for(x,y,w,h) in hands:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()