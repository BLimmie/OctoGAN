from glob import glob
from PIL import Image

def turnwhite(picture):
	img = Image.open(picture)
	img = img.convert("RGBA")
	datas = img.getdata()

	newData = []
	for item in datas:
		if item[3] == 0:
			newData.append((255,255,255,255))
		else:
			newData.append(item)
	img.putdata(newData)
	img.save(picture, "PNG")

for picture in glob('images/*'):
	print(picture)
	turnwhite(picture)

