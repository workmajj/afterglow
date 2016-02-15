#!/usr/bin/env python

from PIL import Image, ImageFilter

im = Image.open("img/glow.jpg")
im = im.resize((32, 32), resample=Image.LANCZOS)
im = im.filter(ImageFilter.GaussianBlur(radius=2))
im.show()
