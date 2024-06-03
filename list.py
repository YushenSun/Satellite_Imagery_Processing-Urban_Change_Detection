import os
from glob import glob

def list_tifs_by_size(folder):
    # Define possible folder names based on provided patterns
    row_offsets = [0, 104, 216]
    column_offsets = [0, 104, 216, 328, 440, 552, 664, 882]

    # Construct the full paths for all possible subfolders
    subfolders = [f"row_offset_{row}_column_offset_{col}" for row in row_offsets for col in column_offsets]

    # Recursively find all .tif files in the subfolders
    tifs = []
    for subfolder in subfolders:
        path = os.path.join(folder, subfolder, '*.tif')
        tifs.extend(glob(path))

    # Sort files by size
    tifs.sort(key=os.path.getsize)

    # Print sorted files with their sizes
    for tif in tifs:
        print(f"{os.path.basename(tif)}: {os.path.getsize(tif)} bytes")

if __name__ == "__main__":
    folder = "imagery\patch_size_128_patch_overlap_16\patches"
    list_tifs_by_size(folder)
