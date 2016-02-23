#!/usr/bin/env python

import sys

from PIL import Image, ImageFilter

def main():
    if len(sys.argv) != 3:
        sys.exit('usage: %s <image1> <image2>' % sys.argv[0])

    im1 = Image.open(sys.argv[1])
    im1 = im1.resize((32, 32), resample=Image.LANCZOS)

    im2 = Image.open(sys.argv[2])
    im2 = im2.resize((32, 32), resample=Image.LANCZOS)

    for i in xrange(5, 100, 5):
        alpha = float(i) / 100
        out = Image.blend(im1, im2, alpha)
        out.save('blend-' + '{:4.2f}'.format(alpha) + '.jpg') # FIXME

if __name__ == "__main__":
    main()
