import os
from PIL import Image
import shutil
import sys
from userconfig import *


# check if argument was given
if len(sys.argv) == 2:
    if sys.argv[1] in supported_apps:
        app = sys.argv[1]

output_path = os.path.join(source_images_path, app)


# check if input path exists, and make output path
if not os.path.isdir(output_path):
    print("couldnt find source path")
if not os.path.isdir(output_path):
    os.mkdir(output_path)


# get list of files
filelist = os.listdir(source_images_path)


# if file is an image, check if its an app ss
count = 0
for file in filelist:
    count += 1
    print(count, end='\r')
    filepath = os.path.join(source_images_path, file)
    extension = os.path.splitext(filepath)[1]
    if extension in supported_extensions:
        
        # check if file is tinderss
        with Image.open(filepath) as img:
            
            # select one column to scan
            column = img.width - 120 
            try:
                rowcolors = set()
                min, max = heightrange(img)
                for i in range(min, max):
                    rowcolors.add(img.getpixel((column, i)))

                if checkifappss(rowcolors, img):
                    print("\t", file)
                    destination = os.path.join(output_path, file)
                    shutil.move(filepath, destination)
            except:
                print(f"========Invalid {file=}========")