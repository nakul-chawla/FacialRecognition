# coding: utf-8
# In[1]:
import numpy as np
import cv2
# In[2]:
def save_pic():
    face_cascade=cv2.CascadeClassifier('data\haarcascade_frontalface_alt2.xml') #cascade is being used, to save the frontal face
    cap = cv2.VideoCapture(0) #switch on the camera
    while(1): #to keep the camera switched on
        ret,frame = cap.read()
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #convert image into grayscale because, color images are not needed to find face in images.
        faces = face_cascade.detectMultiScale(gray) #1.grayscale image,2.decrease factor to improve,3,
        for(x,y,w,h) in faces:
            #print(x,y,h,w)
            gray_roi = gray[y:y+h,x:x+w]
            color_roi = frame[y:y+h,x:x+w]
            color = (0,255,0)
            stroke= 2
            end_cwidth = x + w
            end_cheight = y + h
            cv2.rectangle(frame, (x,y),(end_cwidth, end_cheight), color, stroke)
            img_item= "my-image%d.png"%(faces.shape[0])
            cv2.imwrite(img_item,color_roi) #to save the picture.
        cv2.imshow('frame', frame)
        if cv2.waitKey(33)== 27 & 0xFF!= ord('q'): #click escape to exit.
            break
    cap.release() # release the camera
    cv2.destroyAllWindows() # destroy the window