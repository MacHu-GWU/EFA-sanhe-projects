from tesseract import *

fname1 = 'example.png'
fname2 = 'phototest.tif'
fname3 = 'fonts_test.png'
fname4 = 'example2.png'

im = Image.open(fname4)
text = image_to_string(im)
print text