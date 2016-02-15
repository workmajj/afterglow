#!/usr/bin/env python

from PIL import Image, ImageFilter

for i in xrange(1, 37):
    im = Image.open('img/glow' + str(i) + '.jpg')
    im = im.resize((32, 32), resample=Image.LANCZOS)
    im = im.filter(ImageFilter.GaussianBlur(radius=2))
    im.save('img/glow' + str(i) + '-32.jpg', 'jpeg')
