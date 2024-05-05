# pillow-it-cert-capstone
*Python Imaging Library (pillow) scripts for modifying some test icon images.*

A capstone project for some IT coursework I did.

## Problem Summary

Given a set of Tiff images, use pillow (Python Imaging Library fork) to reformat the images so they are ready for upload to a website.

The output images need to be:
- rotated so they are right-side-up
- resized to be 128x128 pixels
- saved as jpegs

Upon inspection, input images are:
- in many different 'modes,' such as 'LA' (greyscale with transparency) and 'P' (palette mode)
- in black and white or grayscale 
- most must be converted to a different mode before they can be saved as jpegs

Satisfying the requirements of the project was fairly simple.  And one could be pretty happy with the most straightforward execution of the aforementioned steps...if you didn't look at the output images.

## The plot thickens

I'm not sure why this sample project was created with pitfalls you aren't required to fix or notice, but I hope it was to provide an opportunity for learners to go further.  In any case, if the goal is for all of the resulting images to convey potentially useful information, a bit more has to be done!  Things get complicated because some images have some attributes, and even errors/inconsistencies, that don't convert simply:

- some images include a transparency layer that obscures the image data when it is converted to a non transparency-supporting mode.  I need a way to deal with the transparency layer on images that have one.
- some images have errors, such as pixel values inconsistent with their mode.  For example, a one-bit image should have pixel values of only 0 or 1, but instead has pixel values of 0 and 255.

Much of the evolution of the project is captured in the 'examine_images' Jupyter notebook that you'll find in the scripts directory.  If you're looking at this project, that notebook provides a thorough explanation of what I've done.

## How to run this code

The full solution is a simple Python script (convert_images.py) that utilizes a few, common Python libraries.  As is, the scripts search for images following a certain naming convention in the relative path of '../images', the same directory structure as this git project.

Stepping through the notebook will run experiments on test images.  It will try to show (pop up in your default image viewer) and save a few images.

## Future considerations and fixes

This project was a nice introduction to using pillow.  It was definitely a learning process but I'm happy to have successfully completed the project with no lingering issues to resolve.  I understand a lot more about image files, transparency, and composites now.

## Thanks for reading

As mentioned, this is a small project that was part of some fun automation practice for a class I took.  I may refer to it if I use pillow for future projects, but it's not intended for further development at this time.