import tkinter as tk 
from PIL import Image, ImageTk
import crop
import OctoGenFrontend
import prod

root = tk.Tk()

#Make canvas
w = tk.Canvas(root, width = 530, height = 530)
w.pack()

#Add image
file = "fake_samples_epoch_106.png"
img = Image.open(file)
img = ImageTk.PhotoImage(img)
w.create_image(0,0, image = img, anchor = "nw")

x,y = 0,0
def getorigin(eventorigin):
	global x,y
	x = eventorigin.x
	y = eventorigin.y
	crop.individual_crop(file,x,y)
	OctoGenFrontend.send_tweet("choice_octocat.png")
	root.destroy()

root.bind("<Button 1>", getorigin)
root.mainloop()