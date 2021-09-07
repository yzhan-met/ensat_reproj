# ENSAT Reprojection

Provides a sample code to reproject satellite images generated by ENSAT to another proj4 projection.

## Run
In order to run the scripts, you will need to have the following python libs installed properly:

+ h5py
+ PIL
+ pyresample

Additionally, you need to copy `loopy_latlon.h5` file to **etc** folder.

Finally, run the following cmd and you can find the reprojected ENSAT image next to the original one.

```
python main.py /home/yzhan/gits/ensat_reproj/test/AHI-true_color_ahi_202109020200_loopy.png
```