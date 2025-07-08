import os
import shutil

from PIL import Image

from args import args

def change_background(img: Image, hl: str):
    img = img.resize((15 * 256, 7 * 256))

    if args.addon:
        po = os.path.join(hl, "valve", "resource", "background")
        p = os.path.join(os.path.join(hl, "valve_addon") if args.output is None else args.output, "resource", "background")

        if not os.path.exists(p):
            os.makedirs(p)

        for file in os.listdir(po):
            shutil.copy(os.path.join(po, file), p)
    else:
        p = os.path.join(hl, "valve", "resource", "background")

    for i in range(7):
        for j in range(15):
            c = img.crop((j*256, i*256, (j*256)+256, (i*256)+256))

            fname = f"21_9_{i+1}_{chr(97+j)}_loading.tga"
            fp = os.path.join(p, fname)

            c.save(fp)
