import os

ANNOTATIONS_DIR = "labels"

def read_file(file_path):
    os.rename(r'' + ANNOTATIONS_DIR + "/" + file_path, r'' + ANNOTATIONS_DIR + "/" + file_path[5:])

def start():
    for filename in os.listdir(ANNOTATIONS_DIR):
        read_file(filename)

if __name__ == "__main__":
    start()
