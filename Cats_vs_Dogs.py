import cv2
import os
from matplotlib import pyplot as plt
from keras.models import *
from keras.layers import *
from keras.optimizers import Adam
import numpy as np
import os
from sklearn.model_selection import train_test_split

df_x = []
df_y = []
traint_path = "./kagglecatsanddogs_3367a/PetImages"
files = os.listdir(traint_path)
print(files)

for file in files:
    animal = file.split('.')[0]
    if animal == 'cat':
        df_y.append(0)
    else:
        df_y.append(1)
    img = cv2.imread(os.path.join(traint_path,file))
    #img = cv2.resize(img,(64,64))
    df_x.append(img)
    df_x = np.asarray(df_x)
    df_y = np.asarray(df_y)
    print('Processing Done')
    print(df_x.shape)