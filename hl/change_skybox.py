import os
from PIL import Image

from args import args

def change_skybox(img: Image, hl: str):
    img = img.resize((256, 256))

    p = os.path.join(hl, "valve", "gfx", "env")
    if args.skybox == "all":
        for entry in os.listdir(p):
            img.save(os.path.join(p, entry))
    else:
        if "." in args.skybox or "/" in args.skybox:
            print("Please specify only skybox name (without file extension and / or path).")
            return

        for entry in filter(lambda x: args.skybox in x, os.listdir(p)):
            img.save(os.path.join(p, entry))
