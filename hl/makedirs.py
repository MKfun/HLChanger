import os

from args import args

def hl_makedirs(hl: str):
    addon = os.path.join(hl, "valve_addon")
    if not os.path.exists(addon) and not (args.addon and args.output):
        os.makedirs(addon)
