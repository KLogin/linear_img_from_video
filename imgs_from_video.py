# Importing all necessary libraries
import sys
import argparse
from pathlib import Path
import cv2 
import os 

# Params
parser = argparse.ArgumentParser(description='Creating color image from video.')
parser.add_argument('--f', type=Path)
parser.add_argument('--n', default='video_colors', type=str)
parser.add_argument('--w', default=1300, type=int)
parser.add_argument('--h', default=1300, type=int)

args = parser.parse_args()

# Get params
video = args.f
img_name = args.n

# Settings
img_size_w = int(args.w)
img_size_h = int(args.h)

print(str(video))
print(img_size_w)
print(img_size_h)

    
# Read the video from specified path 
cam = cv2.VideoCapture(str(video))
  
# frame 
currentframe = 0
frames_count = cam.get(cv2.CAP_PROP_FRAME_COUNT)
skip_frames = round(frames_count/img_size_w)

# imgs array
imgs = []

while(True): 
    cam.set(cv2.CAP_PROP_POS_FRAMES, currentframe)
      
    # reading from frame 
    ret,frame = cam.read() 
  
    if ret: 
        # if video is still left continue creating images
        print ('Progress: ' + str(round(currentframe/frames_count*100, 2)) + '%') 
  
        # risize. Percent of original size
        resized = cv2.resize(frame, (1, 1), interpolation = cv2.INTER_CUBIC)
  
        # writing the extracted images 
        imgs.append(resized)
  
        # increasing counter so that it will 
        # show how many frames are created 
        currentframe += skip_frames
    else: 
        break

# concat
im_h = cv2.hconcat(imgs)

# risize
square_img = cv2.resize(im_h, (img_size_w, img_size_h), interpolation = cv2.INTER_CUBIC)

# save
cv2.imwrite('./img/' + img_name + '.jpg', square_img)
        
# Release all space and windows once done 
cam.release() 
cv2.destroyAllWindows() 