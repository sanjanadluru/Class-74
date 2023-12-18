import numpy as np
import os
import cv2
from cvzone.FaceDetectionModule import FaceDetector

# Create a path variable that holds relative address to the dataset folder
path = "C:/Users/kvadl/Downloads/TNK-M10-PRO-C74-SAS-BP-main/TNK-M10-PRO-C74-SAS-BP-main/SA1\Face-image-dataset-small"
''' 
Lable the files named 0,1,2 in the path folder as follows

1_0_0_20161219154909149.jpg.chip
10_0_0_20170110225557604.jpg.chip
101_1_2_20170105174739309.jpg.chip
'''
detector = FaceDetector()

# Iterate through each image i.e img in the variable path
for img in os.listdir(path):
    try:
         print(img)
        
    except:
        print("Error in reading")
    





