#!/usr/bin/env python

import os
import sys

from PIL import Image, ImageFilter

SIZE = (32, 32)

def im_open_and_resize(fp):
    im = Image.open(fp)
    return im.resize(SIZE, resample=Image.LANCZOS)

def basename_strip_ext(path):
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

    im1 = im_open_and_resize(sys.argv[2])
    im2 = im_open_and_resize(sys.argv[3])

    f1 = basename_strip_ext(sys.argv[2])
    f2 = basename_strip_ext(sys.argv[3])

    base = os.path.normpath(sys.argv[1]) + '/' + f1 + '-' + f2

    for i in xrange(1, 100):
        alpha = float(i) / 100
        out = Image.blend(im1, im2, alpha)
        out.save(base + '-' + '{:4.2f}'.format(alpha) + '.jpg')

if __name__ == "__main__":
    main()
