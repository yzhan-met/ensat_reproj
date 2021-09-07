from src import reproj

import sys


if __name__ == "__main__":
    img_path = sys.argv[1]
    reproj_img_path = img_path.replace(".png", "_reproj.png")

    img_data = reproj.load_ensat_image(img_path)
    img_coord = reproj.load_latlon()
    targ_data, targ_area = reproj.swath2area(img_data, img_coord, "WhiteIsland_500m")
    reproj.save_image(targ_data, reproj_img_path)
