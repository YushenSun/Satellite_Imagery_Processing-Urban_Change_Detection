import subprocess

from osgeo import gdal


def get_raster_properties(tif_file):
    try:
        result = subprocess.run(['gdalinfo', tif_file], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running gdalinfo: {e}")
        return None


def export_raster_meta(tif_file, output_file):
    info = get_raster_properties(tif_file)
    if info:
        with open(output_file, 'w') as f:
            f.write(info)


def get_raster_details(tif_file):
    dataset = gdal.Open(tif_file)
    if dataset is None:
        print(f"Failed to open the raster file: {tif_file}")
        return None, None, None

    projection = dataset.GetProjection()
    geotransform = dataset.GetGeoTransform()
    pixel_width = geotransform[1]
    pixel_height = geotransform[5]
    return projection, pixel_width, pixel_height


if __name__ == "__main__":
    # Define the path to the arbitrary .tif file
    tif_file = "imagery/all_tifs/B02/patched_sentinel_2_2019-10-15_B02_10m_33_N578_W06_1000cm_roff_0_coff_0.tif"

    # Export the raster's properties to raster_meta.json
    print("Exporting raster properties to raster_meta.json...")
    export_raster_meta(tif_file, "raster_meta.json")

    # Get and print the raster details
    projection, pixel_width, pixel_height = get_raster_details(tif_file)
    if projection and pixel_width and pixel_height:
        print(f"Spatial Reference System: {projection}")
        print(f"Pixel Resolution: {pixel_width} x {pixel_height}")
    else:
        print("Failed to retrieve raster details.")
