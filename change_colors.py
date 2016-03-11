#!/usr/bin/env python3
from PIL import Image
from math import floor
import sys

# [token, outfile-prefix, description]
modes = [["-gs","greyscale_","Converts the image to greyscale"],
        ["-bw","blackandwhite_","Black and white filter."],
        ["-px","pixels_","Turns the image into pixels"]]

for token in sys.argv[1:]:
    if token == "-help":
        print("Change colors will read the arguments and can apply the following filters:")
        for m in modes:
            print("\t"+m[0]+"\t"+m[2])
    elif token[0] == "-":
        for m in modes:
            if token == m[0]:
                mode = m[1]
    else:
        org_img = Image.open(token)
        width, height = org_img.size
        new_img = Image.new('RGB', (width, height))

        org_pix = org_img.load()
        new_pix = new_img.load()

        if mode=="blackandwhite_":
            average_sum = 0
            for i in range(0,width):
                for j in range(0,height):
                    average_sum += int(sum(org_pix[i,j])/3)
            average_value = average_sum / (width*height)
            for i in range(0,width):
                for j in range(0,height):
                    n = int(sum(org_pix[i,j])/3)
                    if n < average_value:
                        n = 0
                    else:
                        n = 255
                    new_pix[i,j] = (n,n,n)

        elif mode=="greyscale_":
            for i in range(0,width):
                for j in range(0,height):
                    n = int(sum(org_pix[i,j])/3)
                    v = [n,n,n]
                    new_pix[i,j] = (v[0], v[1], v[2])

        elif mode=="pixels_":
            for i in range(0,width):
                for j in range(0,height):
                    d_w = 10
                    d_h = 10
                    p_w = (floor(i / d_w)) * d_w
                    p_h = (floor(j / d_h)) * d_h
                    v = org_pix[p_w,p_h]
                    new_pix[i,j] = (v[0], v[1], v[2])

        new_img.save(mode+token)
