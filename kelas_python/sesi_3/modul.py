class Mahasiswa:
    def __init__(self, nama, smt, ipk):
        self.nama = nama
        self.smt = smt
        self.ipk = ipk

    def tampilkan(self):
        print(f"Nama\t\t: {self.nama}")
        print(f"Semester\t: {self.smt}")
        print(f"IPK\t\t: {self.ipk}")

def cek_angka(angka):
    if angka%2:
        result = "ganjil"
    else:
        result = "genap"

    return result

def sapa(nama):
    print(f"Halo {nama}")