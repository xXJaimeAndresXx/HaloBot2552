import io
from colorthief import ColorThief
from PIL import Image, ImageDraw, ImageOps
import cv2
import numpy as np
from frame import crear_frame

crear_frame()
OGimage="IMG/here.png"
PILimage = Image.open(OGimage)
width, height = PILimage.size
BRwidht= int(width*0.01)
print("Border Widht: "+str(BRwidht))
background=(255,255,255)



color_thief = ColorThief(OGimage)
color_palette=color_thief.get_palette(color_count=9)


color_palette_image = Image.new('RGB', (width, 200))
draw = ImageDraw.Draw(color_palette_image)

porc = width/9
x0 = 0
x1 = porc
for color in color_palette:
    draw.rectangle(((x0, 0), (x1, 600)), fill=color)
    x0 += porc
    x1 += porc

color_palette_image.save('IMG/image.png')
PILpalette= Image.open("IMG/image.png")
PALimage="IMG/image.png"

if isinstance(BRwidht,int) or isinstance(BRwidht,tuple):
    BRimage=ImageOps.expand(PILimage,border=BRwidht,fill=background)
    BRpallete=ImageOps.expand(PILpalette,border=BRwidht,fill=background)
    print("Success Expand")
else:
    print("Invalid Integer") 

BRimage.save("IMG/topBR.png")
BRpallete.save("IMG/bottomBR.png")


img1 = cv2.imread("IMG/topBR.png")
img2 = cv2.imread("IMG/bottomBR.png")
vis = np.concatenate((img1, img2), axis=0)
cv2.imwrite('IMG/out.png', vis)