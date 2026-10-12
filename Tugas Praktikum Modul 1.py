class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        return self.panjang * self.lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)


# Membuat objek
pp1 = PersegiPanjang(10, 5)

# Menampilkan hasil
print("Panjang:", pp1.panjang)
print("Lebar:", pp1.lebar)
print("Luas:", pp1.hitung_luas())
print("Keliling:", pp1.hitung_keliling())