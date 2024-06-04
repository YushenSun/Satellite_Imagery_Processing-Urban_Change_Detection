import os
import shutil
from glob import glob

def list_tifs_by_size(folder):
    # Define possible folder names
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

    return tifs

def move_tifs_to_folder(tifs, dest_folder):
    # check whether the destination folder exists already, if not, create it
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # move tifs to the destination folder
    for tif in tifs:
        shutil.move(tif, os.path.join(dest_folder, os.path.basename(tif)))

if __name__ == "__main__":
    src_folder = "imagery/patch_size_128_patch_overlap_16/patches"
    parent_folder = "imagery/patch_size_128_patch_overlap_16/"
    dest_folder = "imagery/all_tifs"

    print("Listing TIFF files by size...")
    tifs = list_tifs_by_size(src_folder)

    print("\nMoving TIFF files to 'all_tifs' folder...")
    move_tifs_to_folder(tifs, dest_folder)

    print("\nRemoving the old 'imagery' folder...")
    shutil.rmtree(parent_folder)