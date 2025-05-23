import os
from os.path import join, getsize
def sizeFinder(minFileSize):
    total = 0
    for root, dirs, files in os.walk("C:\\"):
        try:
            current_directory_size = 0
            for name in files:
                path = join(root, name)
                current_directory_size += getsize(path) 
            gigs = current_directory_size //1000000000
            if gigs > minFileSize:
                total+=gigs
                print(root, "consumes ", gigs, " gigabytes in", len(files), "non-directory files")
                if '__pycache__' in dirs:
                    dirs.remove('__pycache__') 
        except OSError as error :
            #print(f"Error accessing directory or file in {root}: {error}")
            continue
    print("These folders above ",minFileSize," gigs take up ", total, " gigabytes")
sizeFinder(10)