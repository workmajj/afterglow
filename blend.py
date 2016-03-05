#!/usr/bin/env python

import os.path
import sys

from PIL import Image, ImageFilter

JPEG = '.jpg'
SIZE = (32, 32)

def list_files_with_ext(dir_src, ext):
    files = [os.path.join(dir_src, f) for f in os.listdir(dir_src)]
    return [f for f in files if os.path.splitext(f)[1] == ext]

def open_and_resize(path):
    im = Image.open(path)
    return im.resize(SIZE, resample=Image.LANCZOS)

def strip_ext(path):
    ext = os.path.splitext(path)[1]
    name = os.path.basename(path)
    return name[:name.rfind(ext)]

def blend(path1, path2, dir_tmp):
    im1 = open_and_resize(path1)
    im2 = open_and_resize(path2)

    # format: <im1_no_ext>-<im2_no_ext>-<alpha_as_pct>.<ext>

    prefix = '{}/{}-{}-'.format(dir_tmp, strip_ext(path1), strip_ext(path2))

    for i in xrange(0, 100):
        alpha = float(i) / 100
        out = Image.blend(im1, im2, alpha)
        out.save(prefix + '{:0>2d}{}'.format(i, JPEG))

def main():
    if len(sys.argv) != 3:
        sys.exit('usage: {} <src_dir> <tmp_dir>'.format(sys.argv[0]))

    for i in (1, 2):
        if not os.path.isdir(sys.argv[i]):
            sys.exit('{} is not a directory'.format(sys.argv[i]))

    dir_src = os.path.normpath(sys.argv[1])
    dir_tmp = os.path.normpath(sys.argv[2])

    images = sorted(list_files_with_ext(dir_src, JPEG))

    if not images:
        sys.exit('no {} files in {}'.format(JPEG, dir_src))

    for curr, image in enumerate(images):
        next = curr + 1 if curr + 1 < len(images) else 0
        blend(image, images[next], dir_tmp)

if __name__ == '__main__':
    main()
