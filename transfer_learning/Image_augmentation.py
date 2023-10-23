from PIL import Image 
import os 
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from skimage import io
import numpy as np

datagen = ImageDataGenerator(
    rotation_range = 30,
    width_shift_range = 0.2,
    height_shift_range = 0.2,
    shear_range = 0.2,
    zoom_range = 0.2,
    horizontal_flip = True,
    fill_mode = "reflect"
)
files = os.listdir("../dataImage")
a = [2, 5, 6, 15, 8, 12, 4, 7, 3, 11, 10, 14, 13, 1, 9]
for j in range (0, 15):
    for i in range (1, 76):
        s1 = "../dataImage/" + files[j]
        if i < 10:
            s1 += "/l"+ str(a[j]) +"nr00" + str(i) + ".jpg"
        else:
            s1 += "/l"+ str(a[j]) +"nr0" + str(i) + ".jpg"
        x = io.imread(s1)
        x = x.reshape((1,) + x.shape)
        flag = 0
        cc = "../augmented/" + files[j] +"/"
        for batch in datagen.flow(x,
                                batch_size = 16,
                                save_to_dir = cc,
                                save_prefix = "aug",
                                save_format = "jpg" 
                                ):
            flag += 1
            if flag > 7:
                break