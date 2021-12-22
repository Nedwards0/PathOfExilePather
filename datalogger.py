import pyautogui
import time
from datetime import datetime
import cv2
import numpy as np
import pandas
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image as im

x=[]
try:
    count=0
    while True:
        count+=1
        now = datetime.now()
        screenshot = pyautogui.screenshot()
        current_time = now.strftime("%H:%M:%S")
        print(current_time)
        image = (np.array(screenshot))
        x.append(image)
        print(type(image))
        data = im.fromarray(image)
        data.save(str("ImagesData/")+str(count)+'.png')
        time.sleep(5)
except KeyboardInterrupt:
    print(x)


