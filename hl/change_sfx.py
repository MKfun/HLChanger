import os
from pydub import AudioSegment

from args import args

def change_sfx(fname: str, hl: str):
    p = os.path.join(hl, "valve", "sound", args.sfx)

    f = AudioSegment.from_file(fname)
    f.export(p, format="wav")
