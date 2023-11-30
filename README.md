# pillow-it-cert-capstone
*Python Imaging Library (pillow) scripts for modifying some test icon images.*

A capstone project for my IT Automation coursework.

## Problem Summary

Given a set of images, use pillow (PIL) to reformat the images so they are ready for upload to a website.

The output images need to be:
- rotated so they are right-side-up
- resized to be 128x128 pixels
- saved as jpegs

Upon inspection, input images are:
- in many different formats or 'modes'
- in black and white or grayscale 
- most must be converted to a different mode before they can be saved as jpegs

The situation is further complicated because the images have some attributes, and even errors, that I've discovered and would like to be able to account for:
- some images include a transparency layer that obscures the image data when it is converted to a non-transparency mode.  Since I will be converting to RGB before I can save the images as jpegs, I need a way to deal with the transparency layer on images that have one.
- some images have errors, such as pixel values inconsistent with their mode.  For example, a 1-bit image should have pixel values of only 0 or 1, but instead has pixel values of 0 and 255.  Unfortunately, pillow does not understand and converts this to a solid color RGB image.

## How to run this code

These are straightforward Python scripts that utilize a few, common Python libraries.  As is, the scripts search for images following a certain naming convention in the relative path of '../images'.


