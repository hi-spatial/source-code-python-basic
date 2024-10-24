from math import sqrt

def calc_jarak(lat1, lon1, lat2, lon2):
    return sqrt((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2)