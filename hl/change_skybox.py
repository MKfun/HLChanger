import os
import shutil

from PIL import Image

from args import args

def change_skybox(img: Image, hl: str):
    img = img.resize((256, 256))

    if args.addon:
        po = os.path.join(os.path.join(hl, "valve_addon") if args.output is None else args.output, "gfx", "env")
        if not os.path.exists(po):
            os.makedirs(po)
    else:
        po = os.path.join(hl, "valve", "gfx", "env")

    p = os.path.join(hl, "valve", "gfx", "env")

    if args.skybox == "all":
        for entry in os.listdir(p):
            img.save(os.path.join(po, entry))
    else:
        if "." in args.skybox or "/" in args.skybox:
            print("Please specify only skybox name (without file extension and / or path).")
            return

        for entry in filter(lambda x: args.skybox in x, os.listdir(p)):
            img.save(os.path.join(po, entry))
