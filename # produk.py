# produk.py

class produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
        
    def diskon(self, persen):
        potongan = self.harga * (persen/100)
        harga_setelah_diskon = self.harga - potongan
        return harga_setelah_diskon
    
    
# testing
if __name__=="__main__":
    p1 = produk("Kemeja", 150000)
    p2 = produk("sepatu", 300000)
    
    print(f"produk: {p1.nama}, Harga: Rp{p1.harga} ")
    print(f"Harga setelah diskon 20%: Rp{p1.diskon(20)} ")
    
    print(f"\nproduk: {p2.nama}, Harga: Rp{p2.harga} ")
    print(f"Harga setelah diskon 10%: Rp{p2.diskon(10)} ")