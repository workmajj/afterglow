#!/usr/bin/env python

import os.path
import sys
import time

from PIL import Image
from rgbmatrix import Adafruit_RGBmatrix

MATRIX_SIZE = 32
MATRIX_CHAIN = 1

JPEG = '.jpg'
SLEEP = 0.2

def list_files_with_ext(dir_src, ext): # FIXME: common func
    files = [os.path.join(dir_src, f) for f in os.listdir(dir_src)]
    return [f for f in files if os.path.splitext(f)[1] == ext]

def main():
    if len(sys.argv) != 2:
        sys.exit('usage: {} <src_dir>'.format(sys.argv[0]))

    if not os.path.isdir(sys.argv[1]):
        sys.exit('{} is not a directory'.format(sys.argv[1]))

    dir_src = os.path.normpath(sys.argv[1])
    images = sorted(list_files_with_ext(dir_src, JPEG))

    matrix = Adafruit_RGBmatrix(MATRIX_SIZE, MATRIX_CHAIN)

    try:
        while True:
            for image in images:
                im = Image.open(image)
                im.load()
                matrix.SetImage(im.im.id, 0, 0)
                time.sleep(SLEEP)
    except KeyboardInterrupt:
        pass

    matrix.Clear()

if __name__ == '__main__':
    main()
