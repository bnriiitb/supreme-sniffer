from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
import os
from PIL import Image

class ssutil:
#This is a utility class contains the some functions that assists in data preparation
    def rename_files_in_directory(path):
        files = os.listdir(path)
        i = 1
        for file in files:
            os.rename(os.path.join(path, file), os.path.join(path, "image{}".format(i)+'.jpg'))
            #os.rename(os.path.join(path, file), os.path.join(path, "image{:0>3d}".format(i)+'.jpg'))
            i = i+1

    def resize_images_in_directory(image_dir):
        for f in os.listdir(image_dir):
            filename = os.fsdecode(f)
            image = Image.open(image_dir + '/' + filename)
            print(image_dir + '/' + filename)
            height, width = image.size
            if width > 600:
                resize_amt = 600 / width
                new_height = int(round(height * resize_amt))
                image = image.resize((new_height, 600))
                image.save(os.getcwd() + "/" + image_dir + "/" + filename)

if __name__ == '__main__':
    #ssutil.rename_files_in_directory('/Users/panda/GitHub/supreme-sniffer/dataset/test')
    ssutil.resize_images_in_directory('dataset/test')
