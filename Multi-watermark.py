import os, sys, time
from PIL import Image, ImageDraw, ImageFont
# finding a file in the current directory that is a jpeg
files = os.listdir('.')
for index, item in enumerate(files):
    if ".jpg" in item:
        img_location = index
# Setting up progress bar
toolbar_width = 50
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1))
# setting up all variables
# sets opacity of the water mark
opacity = 1
amount = 50
# Change this variable to adjust the amount that the watermark steps
# accross the image
step = 50
# selecting the file that is a jpeg amoung other files
img_file = files[img_location]
# Splitting the file into file name and extension name
name, extension = img_file.split(".")
# opens image file
base = Image.open(img_file).convert('RGBA')
# make a blank image for the text, initialized to transparent text color
txt = Image.new('RGBA', base.size, (255,255,255,0))

# get a font
fnt = ImageFont.truetype('arial.ttf', 60)
# new drawing object
d = ImageDraw.Draw(txt)

# Loop that creates each unique photo
position = 0
for i in range(amount):
    position += step
    d.text((position,10), "SaveMyServer", font=fnt, fill=(0,0,0,opacity))
    out = Image.alpha_composite(base, txt)
    out.save(name + "-watermarked-" + str(i + 1)+ "." + extension)
    txt = Image.new('RGBA', base.size, (255,255,255,0))
    d = ImageDraw.Draw(txt)
    sys.stdout.write("#")
    sys.stdout.flush()

sys.stdout.write("\n")
