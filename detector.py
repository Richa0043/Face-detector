
"""
Created on Sat Mar  9 00:25:41 2019

@author: Richa Rani
"""

import pyttsx3
import cv2



recog = cv2.face.LBPHFaceRecognizer_create()
recog.read('recoginzer/trainningData.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceDetect = cv2.CascadeClassifier(cascadePath);


cam = cv2.VideoCapture(0)


####font = cv2.InitFont(cv2.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0,q 1, 1)
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    count=0
    id=0
    ret, img =cam.read()#it basically returns two things ret and img,img is used nad ret is ignored
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray, 1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        id, conf = recog.predict(gray[y:y+h,x:x+w])
        first = "absent"
        second = "absent"
        speaker=pyttsx3.init()


        if id==1:
            id="harsha"
            speaker.say("harsha ")
            first="present"
            count=0

        elif id==2:
            id="richa"
            speaker.say("richaa")
            second = "present"
            count=0
        elif id==3:
            id="prerna"
            speaker.say("prerna")
            second = "present"
            count=0
        elif id==5:
            id="pankaj verma"
            speaker.say("pankaj verma")
            second = "present"
            count=0
        speaker.runAndWait() 
        f='richa is:{} and prerna is:{}'.format(first,second)
        fp=open("richa.txt",'w')
        fp.write(f)
        fp.close()
        if count>=40:
            fp = open("richa.txt", 'w')
            fp.write("all absent")
            fp.close()
        count += 1
##        cv2.putText(img, str(id),(x,y+h),font,255,1)
        cv2.putText(img,str(id),(x,y+h),font,0.55,(0,255,0),1)


    cv2.imshow('Face',img)

    if cv2.waitKey(1)== 27:
        break
cam.release()
cv2.destroyAllWindows()