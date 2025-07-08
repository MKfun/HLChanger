import os
from PIL import Image

from args import args
from hl import *

def main():
    if not os.path.exists(args.input):
        print("Please specify path to a photo as first argument!")
        return

    hl = detect_half_life()
    if hl is None:
        print("Can`t autodetect Half-life root directory, please specify it like 'export HALF_LIFE=path'")
        return

    if not args.sfx:
        img = Image.open(args.input)

        if args.skybox:
            change_skybox(img=img.copy(), hl=hl)

        if args.background:
            change_background(img=img.copy(), hl=hl)
    else:
        change_sfx(args.input, hl=hl)

if __name__ == "__main__":
    main()
