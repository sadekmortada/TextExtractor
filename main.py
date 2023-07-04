
#extracting horizontal text with some noise and different background colors
########

from PIL import Image
from pytesseract import pytesseract
import os

#Path to tesseract.exe
path_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#Path to the current image
image_path = r"C:\pics\image.jpg"

#Path to folder containing set of images to extract text from.
#Can use absolute path or relative path
images_path = r"C:\pics\images\\"

#Point tesseract_cmd to the path of the exe file
pytesseract.tesseract_cmd = path_tesseract

#Open image
img = Image.open(image_path)

#Extract text
txt = pytesseract.image_to_string(img)

#Print text on screen and save in text.txt file
print(image_path+":\n"+txt)
file = open("text.txt","w")
file.write(image_path+":\n"+txt)
file.close()

#Iterate throw the images of the destination directory then save in texts.file
file=open("texts.txt","w")
for root,drs,fs in os.walk(images_path):
    for f in fs:
        img = Image.open(images_path+f)
        txt = pytesseract.image_to_string(img)
        print(images_path+f+":\n"+txt+"\n\n")
        file.write(images_path+f+":\n"+txt+"\n\n")
file.close()