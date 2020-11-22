# To install 
# pip3 install pillow
# Doc = https://pypi.org/project/Pillow/

from PIL import Image

myFile = 'cat.jpg'
outputName = 'output'
extention = '.webp'

img = Image.open(myFile).convert("RGB")

img.save(outputName + extention,'webp')
