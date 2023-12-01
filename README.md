# pillow-it-cert-capstone
*Python Imaging Library (pillow) scripts for modifying some test icon images.*

A capstone project for my IT Automation coursework.

## Problem Summary

Given a set of Tiff images, use pillow (PIL fork) to reformat the images so they are ready for upload to a website.

The output images need to be:
- rotated so they are right-side-up
- resized to be 128x128 pixels
- saved as jpegs

Upon inspection, input images are:
- in many different 'modes,' such as 'LA' (greyscale with transparency) and 'P' (palette mode)
- in black and white or grayscale 
- most must be converted to a different mode before they can be saved as jpegs

The situation is further complicated because the images have some attributes, and even errors, that I've discovered and would like to be able to account for:
- some images include a transparency layer that obscures the image data when it is converted to a non-transparency mode.  Since I will be converting to RGB before I can save the images as jpegs, I need a way to deal with the transparency layer on images that have one.
- some images have errors, such as pixel values inconsistent with their mode.  For example, a 1-bit image should have pixel values of only 0 or 1, but instead has pixel values of 0 and 255.  Unfortunately, pillow does not understand and converts this to a solid color RGB image.

## How to run this code

These are straightforward Python scripts that utilize a few, common Python libraries.  As is, the scripts search for images following a certain naming convention in the relative path of '../images'.

## Future considerations and fixes

This project was a nice introduction to using pillow.  It was definitely a learning process and I'm not totally satisfied with my solution.  My instinct is that there are some ready-made tools in the pillow library that would fix these issues, but so far I have not been able to find them (or they are currently broken).

Next steps to consider are:
- fix the bug whereby the 'P' mode images I scaled have the black and white reversed.  You can see this on the processed versions of convenience_store_black and movies_black.
- have a more regimented method (script?) for investigating a single image of a given mode type, to keep better track of what needs to be done and what does or doesn't work in pillow.
- A little specific, but why does my transparency masking give a different result from Image.putalpha()?
- Is my transparency masking an adequate solution?
- can't I use the palette on 'P' mode images to convert them correctly?  I did some work on this and was not able to, but that was a few months ago and I've lost track of what I tried.  It's also possible that the palette isn't right and doesn't map the image as expected/desired.
- Is there something like a contrast feature that would work instead of my manual rescaling?  What I found so far has not helped.
