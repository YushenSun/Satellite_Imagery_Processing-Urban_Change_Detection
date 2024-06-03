import os
from glob import glob

def list_tifs_by_size(folder):
    tifs = glob(os.path.join(folder, "*.tif"))
    tifs.sort(key=os.path.getsize)
    for tif in tifs:
        print(f"{os.path.basename(tif)}: {os.path.getsize(tif)} bytes")

if __name__ == "__main__":
    folder = "imagery"
    list_tifs_by_size(folder)
