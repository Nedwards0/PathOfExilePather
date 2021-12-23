import pandas as pd
from PIL import Image as im

k=pd.read_csv('data.csv')  
img=(k.iloc[0][0])
data = im.fromarray(int(img.strip()))
data.save("TEST"+'.png')