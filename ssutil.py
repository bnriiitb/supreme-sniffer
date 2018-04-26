import os
class ssutil:
#This is a utility class contains the some functions that assists in data preparation
    def rename_files_in_directory():
        path = '/Users/panda/GitHub/supreme-sniffer/dataset/test'
        files = os.listdir(path)
        i = 1
        for file in files:
            os.rename(os.path.join(path, file), os.path.join(path, "image{}".format(i)+'.jpg'))
            #os.rename(os.path.join(path, file), os.path.join(path, "image{:0>3d}".format(i)+'.jpg'))
            i = i+1

if __name__ == '__main__':
    ssutil.rename_files_in_directory()
