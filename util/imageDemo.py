# -*- coding:utf-8 -*-
import os,sys
from PIL import Image
def produceImage(file_in, width, height, file_out):
    image = Image.open(file_in)
    resized_image = image.resize((width, height), Image.ANTIALIAS)
    resized_image.save(file_out)

if __name__ == '__main__':
    # file_in = 'D:/images/TR3.jpg'
    # width = 3000
    # height = 4000
    # file_out = '1.jpg'
    # produceImage(file_in, width, height, file_out)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(BASE_DIR)

    print(BASE_DIR)