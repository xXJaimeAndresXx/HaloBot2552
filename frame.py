import numpy as np
import cv2
import random
from PIL import Image, ImageChops
from rand import randomFile

#Get the frame from the specified file
def crear_frame():
    cap = cv2.VideoCapture("HaloCinematics/"+randomFile()) 
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    n=random.randint(0,total)
    print("Frame "+str(n)+" out "+str(total))
    cap.set(1,n) 
    ret, frame = cap.read() 
    cv2.imwrite("IMG/here.png",frame)
#Erase white/black borders
def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)




#    if np.any(frame[1, 1] != 0):
 #       print("No letterbox available")
  #      
   # else:   
    #    height= frame.shape[0]
     #   width= frame.shape[1]
      #  letterboxtop= height*0.15
       # letterboxbottom= height-letterboxtop
        #print("letterbox: "+str(letterboxtop))
        #print("letterbox: "+str(letterboxbottom))

        #crop_img= frame[int(letterboxtop):int(letterboxbottom),0:width]
        #cv2.imwrite("IMG/here.png",crop_img)







