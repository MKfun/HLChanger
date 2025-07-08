import os
from PIL import Image

from args import args

def change_logo(img: Image, hl: str):
    img = img.resize((64, 64))

    p = os.path.join(hl, "valve", "logos")

    if "." in args.logo or "/" in args.logo:
        print("Please specify only logo name (without file extension and / or path)")
        return

    if args.logo == "all":
        for logo in os.listdir(p):
            img.save(os.path.join(p, logo))
    else:
        for logo in filter(lambda x: args.logo in x, os.listdir(p)):
            img.save(os.path.join(p, logo))
