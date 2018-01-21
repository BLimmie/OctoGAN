from PIL import Image
coords = []

for pixel1 in range (2, 530, 66):
	for pixel2 in range(2, 530, 66):
		coords.append((pixel1, pixel2, pixel1+64, pixel2+64))
print(coords)

def cut(filename):
	img = Image.open(filename)
	for i in range(64):
		cropped = img.crop(coords[i])
		cropped.save(filename[:-4] + "_" + str(i+1) + ".png")

def individual_crop(filename,x,y):
	img = Image.open(filename)
	x_img = int((x-2)/66)*66 + 2
	y_img = int((y-2)/66)*66 + 2
	cropped = img.crop((x_img, y_img, x_img+64, y_img+64))
	cropped.save("choice_octocat.png")