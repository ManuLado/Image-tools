#"splits image into a matrix of images"

import os
import sys
from PIL import Image

savedir = "."
filename = "imagen.png"
img = Image.open(filename)
width, height = img.size
start_pos = start_x, start_y = (0, 0)
cropped_image_size = w, h = int(width/4), int(height/4)

frame_num = 1
j=0
for col_i in range(0, width, w):
    j+=1
    i=0
    for row_i in range(0, height, h):
        i+=1
        crop = img.crop((col_i, row_i, col_i + w, row_i + h))
        crop.save(str(i)+str(j)+'.png')
	#save_to= os.path.join(savedir, "testing_{:02}.png")
        #crop.save(save_to.format(frame_num))
        #frame_num += 1