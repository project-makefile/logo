# This Python file uses the following encoding: utf-8

# Via https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html#

# Fonts via https://github.com/python-pillow/Pillow/tree/master/Tests/fonts

import os
import sys

from PIL import Image, ImageDraw, ImageFont

# create an image
def create_image(filename):
    """
    Create image
    """
    x = 1400
    y = 1400

    # bg white
    # out = Image.new("RGB", (x, y), (255, 255, 255))

    # bg black
    out = Image.new("RGB", (x, y), (0, 0, 0))

    # get a font
    fontsize = int(x/2)
    fnt = ImageFont.truetype(filename, fontsize)
    print(filename)
    # get a drawing context
    d = ImageDraw.Draw(out)

    # draw multiline text
    xoffset = (x/8) + (x/16)
    yoffset = y/8

    # text black
    #d.multiline_text((xoffset, yoffset), "$ make …", font=fnt, fill=(0, 0, 0))

    # text white
    d.multiline_text((xoffset, yoffset), "$ make …", font=fnt, fill=(255, 255, 255))

    fontname = filename.split(".")[0]  # Remove file extension
    out.save("logo_%s.png" % fontname, "PNG")


if __name__ == "__main__":

    # files = [f for f in os.listdir(".") if f.endswith("ttf")]
    # for filename in files:

    create_image("NotoSans-Regular.ttf")
