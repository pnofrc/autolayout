# November 2021, copyleft || Funix || Zine Camp, Worm, Rotterdam


import cv2
import pytesseract as pt
import os
from PIL import Image, ImageEnhance

def read_img(img):
    img = cv2.imread(img)
    return pt.image_to_string(img)

name = "silenzionubi"


im = Image.open(f'OCR/scans/{name}.jpg')
enhancer = ImageEnhance.Contrast(im)
factor = 1.5
im_output = enhancer.enhance(factor)
!mkdir OCR/scansN/
im_output.save(f'OCR/scansN/{name}.png')

txt = read_img(f'OCR/scansN/{name}.png')

!mkdir OCR/txt
got = open(f'OCR/txt/{name}.txt','w')
got.write(txt)
got.close()