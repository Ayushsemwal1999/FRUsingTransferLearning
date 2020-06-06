#!/usr/bin/env python
# coding: utf-8

# In[6]:


import cv2
import numpy as np
cap = cv2.VideoCapture(0)
count = 0
while count<80:
    ret, frame = cap.read()
    count += 1
    key = cv2.waitKey(10)
    #face = cv2.resize(face_extractor(frame), (400,400))
    file_name_path = 'C:/Users/Dell/Desktop/FR/test/ayush/'+ str(count) + '.jpg'
    cv2.imwrite(file_name_path, frame)
    cv2.imshow('Face Cropper', frame)
    if cv2.waitKey(1) == 13:
            cv2.destroyAllWindows()
            webcam.release()
            break
cap.release()
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:





# In[ ]:




