
# importing the module 
from PIL import Image 
import os 

files = os.listdir("../dataImage")
files2 = os.listdir("../dataImage_tif")
a = [2, 5, 6, 15, 8, 12, 4, 7, 3, 11, 10, 14, 13, 1, 9]
# importing the image  
for j in range(0, 15):
    for i in range (1, 76):
        s1 = "../dataImage/" + files[j]
        s2 = "../dataImage_tif/" + files2[j]
        if i < 10:
            s2 += "/l"+ str(a[j]) +"nr00" + str(i) + ".tif"
        else:
            s2 += "/l"+ str(a[j]) +"nr0" + str(i) + ".tif"
        im = Image.open(s2) 
        rgb_im = im.convert("RGB") 
        if i < 10:
            s1 += "/l"+ str(a[j]) +"nr00" + str(i) + ".jpg"
        else:
            s1 += "/l"+ str(a[j]) +"nr0" + str(i) + ".jpg"
        rgb_im.save(s1) 