# tools/coordinate_calc.py
import tools.spatial_utils.geometry as geom

note = "Module tools.coordinate_calc berisi fungsi geospasial"

def calc_distance(lat1, lon1, lat2, lon2):
    return geom.sqrt(geom.square(lat2 - lat1) + geom.square(lon2 - lon1))