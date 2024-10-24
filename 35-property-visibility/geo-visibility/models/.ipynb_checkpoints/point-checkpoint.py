# Class Point merepresentasikan koordinat titik dengan properti latitude dan longitude
class Point:
    def __init__(self, latitude, longitude):
        # Properti latitude dan longitude bersifat publik
        self.latitude = latitude
        self.longitude = longitude
        # Properti __elevation ditandai sebagai privat menggunakan dua underscore
        self.__elevation = 0.0

    # Method untuk mengatur nilai ketinggian (elevation)
    def set_elevation(self, elevation):
        self.__elevation = elevation

    # Method untuk mendapatkan nilai ketinggian
    def get_elevation(self):
        return self.__elevation