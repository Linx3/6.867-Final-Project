import os

ANNOTATIONS_DIR = "labels"
DESTINATION_DIR = "labels_2"

def read_file(file_path):
    with open(ANNOTATIONS_DIR+"/"+file_path, 'r') as file:
        line = file.readlines()[0]
        line = '0' + line[1:]
    with open(DESTINATION_DIR + "/" + file_path, 'a') as file:
        file.write(line)

def start():
    if not os.path.exists(DESTINATION_DIR):
        os.makedirs(DESTINATION_DIR)
    for filename in os.listdir(ANNOTATIONS_DIR):
        if filename.endswith('txt'):
            read_file(filename)
        else:
            print("Skipping file: {}".format(filename))


if __name__ == "__main__":
    start()
