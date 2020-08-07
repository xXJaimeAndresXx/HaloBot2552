import numpy as np
import cv2
import random
from rand import randomFile

def crear_frame():
    cap = cv2.VideoCapture("HaloCinematics/"+randomFile()) #video_name is the video being called
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    n=random.randint(0,total)
    print("Frame "+str(n)+" out "+str(total))
    cap.set(1,n) # Where frame_no is the frame you want
    ret, frame = cap.read() # Read the frame
    cv2.imwrite("IMG/here.png",frame)

