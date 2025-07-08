import os
from pathlib import Path

DEFAULT_PATH = os.path.join(Path.home(), ".steam/steam/steamapps/common/Half-Life")

def detect_half_life():
    if os.path.exists(DEFAULT_PATH):
        return DEFAULT_PATH
    else:
        h = os.environ.get("HALF_LIFE")
        if h is not None:
            return h
        else:
            return None
