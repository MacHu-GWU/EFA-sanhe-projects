import Image
img = Image.open("Lisa.jpg")
print img.format, img.size, img.mode
img.show()