from PIL import Image
import glob
import numpy as np
from tensorflow import keras
import re
# from keras.models import load_model

imgpath = '/home/linx3/Desktop/randomraptorsgamelabel/'
model_path = '/home/linx3/Desktop/testing/model4.h5'
outpath1 = '/home/linx3/Desktop/testing/output_draw/'
outpath2 = '/home/linx3/Desktop/testing/model4_randomgame/'

def make_image_dataset(imgpath: str, outpath: str):

	all_file_names = glob.glob(imgpath + '*.txt')
	i = 1
	all_test_images = []
	print("length of total number of images is {}".format(len(all_file_names)))
	for fil in all_file_names:
		fil = fil[:-4]
		if i % (len(all_file_names) // 10) == 0:
			print("{}%".format(i / len(all_file_names)))
		i += 1

		txt_file = fil + '.txt'
		# try:
		with open(txt_file, 'r') as f:
			content = f.read()

		nums = [float(x) for x in re.findall(r'[0-9\.]+', content)]

		x1=nums[0]*(1280/416.)
		y1=nums[1]*(720/416.)
		x2=nums[2]*(1280/416.)
		y2=nums[3]*(720/416.)

		dx=x2-x1
		dy=y2-y1
		x1 += dx/2
		y1 += dy/2

		image = Image.open(fil)
		# width, height = image.size
		width, height = 1,1
		image = image.crop((int(width * (x1 - dx/2)), int(height * (y1-dy/2)), int(width * (x1 + dx/2)), int(height * (y1+dy/2))))
		image = image.resize((32, 32))

		fi = fil.split("/")[-1]

		# save images
		# im2 = image.save(outpath + fi)
		image = np.array(image)
		image = image[:,:,:3]/255.
		all_test_images.append(image)
		# except:
			# continue

	print("final length is {}".format(len(all_test_images)))
	all_test_images = np.array(all_test_images)
	print(all_test_images.shape)
	return (all_file_names, all_test_images)


def predict(model_path: str, input_images):
	print("predicting images...")
	# model = load_model(model_path)
	model=keras.models.load_model(model_path)
	p = model.predict(input_images)
	predictions = [round(i[0]) for i in p]
	return predictions


'''
Code for drawing a border
'''
def draw_images(all_file_names, predictions, outpath):
	print("drawing images...")
	for index, fil in enumerate(all_file_names):
		fil = fil[:-4]
		if (index+1) % (len(all_file_names) // 10) == 0:
			print("{}%".format((index+1) / len(all_file_names)))

		old_im = Image.open(fil)
		old_size = old_im.size
		if predictions[index] == 1:
			c = 'green'
		else:
			c = 'red'
		new_size = (old_size[0]+100, old_size[1]+100)
		new_im = Image.new("RGB", new_size, color=c)   ## luckily, this is already black!
		new_im.paste(old_im, ((new_size[0]-old_size[0])//2,
		                      (new_size[1]-old_size[1])//2))

		new_im.save(outpath + fil.split("/")[-1])

all_file_names, all_test_images = make_image_dataset(imgpath, outpath1)
predictions = predict(model_path, all_test_images)
draw_images(all_file_names, predictions, outpath2)
