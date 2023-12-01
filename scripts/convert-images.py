#!/usr/bin/python3
'''convert b&w TIFF icon images to JPEG, resizing, rotating, and accounting for transparency'''
#using black or white masks as appropriate, since JPEG doesn't support transparency

from PIL import Image
from glob import glob
import re
from os import path

def has_bad_extrema(img):
    #b&w images are either flat (an error) or suspicious if they don't use the full pixel depth
    #assuming image modes are either 8-bit or binary
    mode = img.mode
    extra = img.getextrema()
    full = 255
    depth = 0
    dmin = full
    dmax = 0

    if 'A' in mode:
        #has additional transparency layer
        #check that at least one layer uses full depth
        #get overall min/max pixel values
        for i in range(len(extra)):
            depth = max(extra[i][1] - extra[i][0], depth)
            dmin = min(extra[i][0], dmin)
            dmax = max(extra[i][1], dmax)
    else:
        #no transparency layer
        if mode == '1':
            #1-bit pixel case, range of 0-1
            full = 1
        dmin = extra[0]
        dmax = extra[1]
        depth = dmax - dmin
    if depth != full:
        return True, dmin, dmax
    return False, dmin, dmax

def scale_pixels(myImage, dmin, dmax):
    #scale problematic 1-bit and 8-bit pixel depth to full range
    #For 1-bit images, this rescales pixels if they exceed allowed pixel values
    #we're presuming the pixel values are binary
    full = 255
    if myImage.mode == '1':
        full = 1
    data = myImage.getdata()
    myImage.putdata(data, full/dmax, -dmin)
    return myImage

def is_transparent(myImage):
    #If there is no Alpha 'A' channel, check for transp. info
    if 'A' not in myImage.mode:
        if myImage.info.get('transparency', None) is not None:
            return True
        else:
            return False
    return True

def add_mask(filename, myImage):
    #paste image onto black or white background
    #expects files named to indicate b or w color
    #couldn't get composite to work with LA mode, so it's in RGBA for now
    if(re.search(r"black", filename)):
        #icon should be black, mask with white
        white_mask = Image.new("RGBA", myImage.size, (255,255,255))
        myImage = Image.alpha_composite(white_mask, myImage)
    if(re.search(r"white", file)):
        #icon is white, mask with black
        black_mask = Image.new("RGBA", myImage.size, (0,0,0))
        myImage = Image.alpha_composite(black_mask, myImage)
    return myImage


in_dir = './'
out_dir = './test/'
pattern = 'ic*dp'
size = (128, 128)

file_list = [path.basename(x) for x in glob(in_dir + pattern)]
for file in file_list:
    im = Image.open(file)
    out_im = im.resize(size).rotate(270)
    bad_depth, dmin, dmax = has_bad_extrema(out_im)
    if bad_depth:
        #scale pixels simply to span their mode depth
        out_im = scale_pixels(out_im, dmin, dmax)
    elif is_transparent(im):
        out_im = add_mask(file, out_im.convert('RGBA'))
    out_im = out_im.convert('L').save(out_dir + file, 'jpeg')
