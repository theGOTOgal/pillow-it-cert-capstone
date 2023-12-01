#!/usr/bin/python3
'''investigate black and white images for color/mode errors'''

from PIL import Image
from os import path
from glob import glob

def has_bad_extrema(img):
    #Compare extrema to the full mode bit depth
    #assuming images are either 8-bit or binary
    mode = img.mode
    extra = img.getextrema()
    full = 255

    if 'A' in mode:
        #has additional transparency layer
        depth = 0
        for i in range(len(extra)):
            depth = max(extra[i][1] - extra[i][0], depth)
    else:
        #no transparency layer
        depth = extra[1] - extra[0]
        if mode == '1':
            #1-bit pixel case, range of 0-1
            full = 1
    if (depth < 0.5*full) or (depth > full):
        #images use less than half or more than max bit depth
        return True
    return False

dir = './'
pattern = 'ic*dp'
image_list = [path.basename(x) for x in glob(dir + pattern)]

for file in image_list:
    img = Image.open(file)
    if has_bad_extrema(img):
        print(f'Image may have problematic contrast levels: {file}')
        print(f'Image mode: {img.mode}')
        print(f'Image extrema: {img.getextrema()}')
