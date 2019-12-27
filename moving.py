#mport os.path
#from os import path
import os
import shutil
from pathlib import Path

# file_path=Path("")
count=0
for i in range(18000):
    pos=str(i)
    if len(pos)<5:
        pos="0"*(5-len(pos))+pos
    text_original="/home/linx3/Desktop/part1-20191103T005658Z-001/part1/scene"+pos+".txt"
    file=Path(text_original)
    if file.is_file():
        image_original="/home/linx3/Desktop/part1-20191103T005658Z-001/part1/scene"+pos+".png"
        text_new="/home/linx3/Desktop/full_data/scene"+pos+".txt"
        image_new="/home/linx3/Desktop/full_data/scene"+pos+".png"
        os.rename(text_original,text_new)
        os.rename(image_original,image_new)
        # shutil.move(text_original,text_new)
        # shutil.move(image_original,image_new)
    # if path.exists("scene"+pos+".txt"):
        count+=1
print(count)
