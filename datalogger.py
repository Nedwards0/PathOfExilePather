import pyautogui
import time
from datetime import datetime
import cv2
import numpy as np
import pandas
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image as im
import pandas as pd
x=[]
y=[]
time.sleep(10)
try:
    count=0
    while True:
        count+=1
        now = datetime.now()
        screenshot = pyautogui.screenshot()
        #print(screenshot)
        current_time = now.strftime("%H:%M:%S")
        print(current_time)
        image = (np.array(screenshot))
        print(image)
        if(count==1):
            df = pd.DataFrame({'x':[image], 'y':1}, columns=['x','y'])
        else:
            df2 = pd.DataFrame({'x':[image], 'y':1}, columns=['x','y'])
            frames=[df,df2]
            df = pd.concat(frames)
        data = im.fromarray(image)
        data.save(str("ImagesData/")+str(count)+'.png')

        time.sleep(5)
except KeyboardInterrupt:
    df.to_csv('data.csv')


