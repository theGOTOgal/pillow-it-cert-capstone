#!/usr/bin/python3
'''convert set of b&w TIFF icon images to JPEG, resizing, rotating, and accounting for transparency'''

from PIL import Image, ImageOps
from glob import glob
import re
from os import path
import pathlib

def has_bad_extrema(img):
    #Compare image pixel extrema to their full mode range
    #flag if these B&W images don't use exactly the full depth
    #Note: assumes images are 8-bit or binary
    mode = img.mode
    extra = img.getextrema()
    full = 255

    if len(mode) > 1:
        #multiband image has extrema for each band
        depth = 0
        for i in range(len(extra)):
            #get the max range out of all bands
            depth = max(extra[i][1] - extra[i][0], depth)
    else:
        #single band image
        depth = extra[1] - extra[0]
        if mode == '1':
            #1-bit mode, range of 0-1
            full = 1
    if depth != full:
        #b&w images should use full pixel range
        return True
    return False



def fix_palette(myImage):
    #fix problematic P mode images
    #I found it wasn't necessary to fix the 1-bits
    img_pal = myImage.getpalette()
    for i in range(0, 3):
        img_pal[i] = 255
    for i in range(3, 6):
        img_pal[i] = 0
    myImage.putpalette(img_pal)
    return myImage


def process_trans(filename, myImage):
    #expects files named to indicate b or w color
    alpha = myImage.getchannel('A')
    if(re.search(r"black", filename)):
        #icon should be black
        myImage = ImageOps.invert(alpha)
    if(re.search(r"white", file)):
        #icon is white
        myImage = alpha
    return myImage


in_dir = '../images/'
out_dir = '../processed/'
pattern = 'ic*dp'
size = (128, 128)
flagged = []
count = 0

#make output dir if does not exist
pathlib.Path(out_dir).mkdir(parents=True, exist_ok=True)

file_list = [path.abspath(x) for x in glob(in_dir + pattern)]
for file in file_list:
    print(file)
    img = Image.open(file)
    out_img = img.resize(size).rotate(270)
    bad_depth = has_bad_extrema(out_img)
    if bad_depth: #these will be my 'P' and '1' mode imgs
        #ignore '1' modes that were flagged, fix 'P' ones
        if out_img.mode == 'P':
            out_img = fix_palette(out_img)
        flagged.append(path.basename(file))
        count += 1
    elif img.mode == 'LA':
        out_img = process_trans(file, out_img)
        count += 1
    else:
        print(f'Your script missed some image:\n{file}')
    out_img = out_img.convert('L').save(out_dir + path.basename(file), 'jpeg')

print(f'{count} images done processing.\n  The following images were flagged during processing:\n')
print("\n".join(flagged))
