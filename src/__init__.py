from os.path import dirname, abspath, join


etc_dir = join(dirname(dirname(abspath(__file__))), "etc")
proj_yaml = join(etc_dir, "areas.yaml")
latlon_h5 = join(etc_dir, "loopy_latlon.h5")