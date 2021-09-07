"""Projection function shared within the project."""

from . import proj_yaml, latlon_h5

from PIL import Image
import h5py
import numpy as np
import pyresample


def swath2area(
    data: np.array, orig_swath_latlon: tuple, targ_area_name: str
) -> np.array:
    """Resample a swath data to an area.
    Args:
        data (np.array): 1-D or 2-D swath data.
        orig_swath_latlon (tuple): (lat, lon) of swath data with the same shape.
        targ_area_name (str): name of predefined area definition in `areas.yaml` file.
    Returns:
        np.array: resampled data.
    """

    orig_def = pyresample.geometry.SwathDefinition(
        lons=orig_swath_latlon[1], lats=orig_swath_latlon[0]
    )
    targ_def = pyresample.load_area(proj_yaml, targ_area_name)

    resampled_data = pyresample.kd_tree.resample_nearest(
        orig_def, data, targ_def, radius_of_influence=20000, fill_value=None, nprocs=4
    )

    return resampled_data, targ_def


def load_latlon() -> tuple:
    h5f = h5py.File(latlon_h5)
    lats = h5f["NZ/500m/latitude"][:]
    lons = h5f["NZ/500m/longitude"][:]

    return (lats, lons)


def load_ensat_image(img_path: str) -> np.array:
    img = Image.open(img_path).convert("RGB")
    img_data = np.array(img)

    return img_data


def save_image(img_data: np.array, img_path: str) -> None:
    img = Image.fromarray(img_data)
    img.save(img_path)
