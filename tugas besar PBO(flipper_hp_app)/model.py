class HP:
    def __init__(self, id_hp, merek, ram, storage, kondisi):
        self.id_hp = id_hp
        self.merek = merek
        self.ram = ram
        self.storage = storage
        self.kondisi = kondisi

class Transaksi:
    def __init__(self, id_hp, harga_beli, harga_jual, tanggal):
        self.id_hp = id_hp
        self.harga_beli = harga_beli
        self.harga_jual = harga_jual
        self.tanggal = tanggal

class Kerusakan:
    def __init__(self, id_hp, deskripsi, tingkat, biaya):
        self.id_hp = id_hp
        self.deskripsi = deskripsi
        self.tingkat = tingkat
        self.biaya = biaya

class Pembeli:
    def __init__(self, nama, kontak):
        self.nama = nama
        self.kontak = kontak

class Sumber:
    def __init__(self, nama, alamat, kode_pos):
        self.nama = nama
        self.alamat = alamat
        self.kode_pos = kode_pos
