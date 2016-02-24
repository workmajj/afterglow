#!/usr/bin/env python

import os.path
import sys

from PIL import Image, ImageFilter

SIZE = (32, 32)

def open_and_resize(path):
    im = Image.open(path)
    return im.resize(SIZE, resample=Image.LANCZOS)

def strip_ext(path):
    ext = os.path.splitext(path)[1]
    name = os.path.basename(path)
    return name[:name.rfind(ext)]

def main():
    if len(sys.argv) != 4:
        sys.exit('usage: %s <dir> <im1> <im2>' % sys.argv[0])

    if not os.path.isdir(sys.argv[1]):
        sys.exit('%s is not a directory' % sys.argv[1])
    if not os.path.isfile(sys.argv[2]):
        sys.exit('%s is not a regular file' % sys.argv[2])
    if not os.path.isfile(sys.argv[3]):
        sys.exit('%s is not a regular file' % sys.argv[3])
    if os.path.samefile(sys.argv[2], sys.argv[3]):
        sys.exit('files are the same')

    im1 = open_and_resize(sys.argv[2])
    im2 = open_and_resize(sys.argv[3])

    prefix = os.path.normpath(sys.argv[1]) + '/' + \
        strip_ext(sys.argv[2]) + '-' + strip_ext(sys.argv[3]) + '-'

    for i in xrange(1, 100):
        alpha = float(i) / 100
        out = Image.blend(im1, im2, alpha)
        out.save(prefix + '{:0>2d}'.format(i) + '.jpg') # e.g., one-two-26.jpg

if __name__ == '__main__':
    main()
