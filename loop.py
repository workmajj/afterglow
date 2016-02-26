#!/usr/bin/env python

import time

from PIL import Image, ImageDraw
from rgbmatrix import Adafruit_RGBmatrix

SLEEP = 0.05

def show(num):
    f = 'glow12-glow33-{:0>2d}.jpg'.format(num) # FIXME
    print f
    im = Image.open('img/blend/' + f) # FIXME
    im.load()
    matrix.SetImage(im.im.id, 0, 0)
    time.sleep(SLEEP)

def main():
    matrix = Adafruit_RGBmatrix(32, 1)

    for i in xrange(10):
        for j in xrange(1, 99):
            show(j)
        for j in xrange(99, 1, -1):
            show(j)

    matrix.Clear()

if __name__ == '__main__':
    main()
