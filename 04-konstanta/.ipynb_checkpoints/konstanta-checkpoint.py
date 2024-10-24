from typing import Final

GRAVITASI: Final = 9.81  # Gravitasi dalam m/s²
print("Gravitasi: %f" % (GRAVITASI))

# Tipe konstanta GRAVITASI tidak ditentukan secara eksplisit,
# melainkan didapat dari tipe data nilai
GRAVITASI: Final = 9.81

# Tipe konstanta TOTAL_PROVINSI ditentukan secara eksplisit yaitu `int`
TOTAL_PROVINSI: Final[int] = 38  # Total provinsi di Indonesiaprint("total provinsi: %f" % (TOTAL_PROVINSI))