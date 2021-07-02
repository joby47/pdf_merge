#!/usr/bin/env python3
#pdf_merge.py
#Writen by: Joel Lowther
#On: 02/07/2021
#Last update: 02/07/2021
#
#A simple utility for combining image files - such as scanned pages - into a single PDF document.

import os
from PIL import Image

def form_pdf(image_filenames, out_filename):
    #Read the images in, combine them into a PDF file and save the result
    #Arguments are:
    #   image_filenames (list of strings): List containing the file paths to the images to be combined in order
    #   out_filename (string): File which the output pdf is to be saved to

    #Load image files into list
    images = []
    for file in image_filenames:
        try:
            im = Image.open(file)
            #Ensure correct colour format
            im.convert('RGB')
            images.append(im)
        except OSError:
            print('Could not open image %s.' % file)
            continue

    #Save images as PDF
    try:
        images[0].save(out_filename, save_all=True, append_images=images[1:], producer='pdf_merge')
    except OSError:
        print('Could not save file %s.' % out_filename)

def list_images(odds_dir, evens_dir):
    #Find the filenames of the images and list them in order
    #Arguments are:
    #   odds_dir (string): path to the directory containing the odd numbered pages. Filenaems when sorted aplanumerically should run from the first page to the last
    #   evens_dir (string): path to the directory containing the even numbered pages. Filenaems when sorted aplanumerically should run from the LAST PAGE TO THE FIRST.
    #Return value is a list of all the images' filenames, sorted in order of page number

    #List files in each directory. Sort odds (evens) in (reverse) order - i.e. in page order
    odds = os.listdir(odds_dir).sort()
    evens = os.listdir(evens_dir).sort(reverse=True)

    #Define a list large enough to hold all pages, then alternate odd and even pages in list
    combined = odds + evens
    combined[::2] = odds
    combined[1::2] = evens

    return combined

def merge_images(odds_dir, evens_dir, out_filename):
    #Merge the images found in the directories odds_dir and evens_dir into a single pdf file and save the result to out_filename
    #Arguments are:
    #   odds_dir (string): path to the directory containing the odd numbered pages. Filenaems when sorted aplanumerically should run from the first page to the last
    #   evens_dir (string): path to the directory containing the even numbered pages. Filenaems when sorted aplanumerically should run from the LAST PAGE TO THE FIRST.
    #   out_filename (string): File to which the output PDF is to be saved 

    images = list_images(odds_dir, evens_dir)
    form_pdf(images, out_filename)

def main():
    #Entry point if this script is executed directly
    #Ask for user to input the directories containing the images as well as the output filename. Then call merge_images()

    odds = input('Directory containig odd-numbered pages: ')
    evens = input('Directory containing even-numbered pages: ')
    out = input('Output (PDF) filename: ')

    #Add file extension if necessary
    if out[-4:] != '.pdf':
        out += '.pdf'

    merge_images(odds, evens, out)

#Set entry point
if __name__ == '__main__':
    main()

