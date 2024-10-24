# Class Region merepresentasikan wilayah geospasial dengan nama dan boundary points
class Region:
    def __init__(self, name, boundary_points):
        # Properti name bersifat publik
        self.name = name
        # Properti boundary_points menyimpan titik-titik koordinat sebagai batas wilayah
        self.boundary_points = boundary_points
        # Properti __area bersifat privat untuk menyimpan luas wilayah
        self.__area = 0.0

    # Method privat untuk menghitung luas wilayah
    def __compute_area(self):
        # Contoh penghitungan area
        self.__area = 123.45

    # Method untuk menampilkan informasi wilayah
    def info(self):
        # Menghitung luas wilayah sebelum menampilkan
        self.__compute_area()
        print(f"Region: {self.name}")
        print(f"Area: {self.__area} km²")