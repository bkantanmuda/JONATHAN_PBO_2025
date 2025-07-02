import database
from model import HP, Transaksi, Kerusakan, Pembeli, Sumber

class ManajerFlipper:
    def tambah_hp(self, hp: HP, minus=""):
        sql = "INSERT INTO hp (id_hp, merek, ram, storage, kondisi, minus) VALUES (?, ?, ?, ?, ?, ?)"
        return database.execute_query(sql, (hp.id_hp, hp.merek, hp.ram, hp.storage, hp.kondisi, minus))

    def tambah_transaksi(self, trx: Transaksi):
        sql = "INSERT INTO transaksi (id_hp, harga_beli, harga_jual, tanggal) VALUES (?, ?, ?, ?)"
        return database.execute_query(sql, (trx.id_hp, trx.harga_beli, trx.harga_jual, trx.tanggal))

    def tambah_kerusakan(self, ker: Kerusakan):
        sql = "INSERT INTO kerusakan (id_hp, deskripsi, tingkat, biaya) VALUES (?, ?, ?, ?)"
        return database.execute_query(sql, (ker.id_hp, ker.deskripsi, ker.tingkat, ker.biaya))

    def tambah_pembeli(self, pb: Pembeli):
        sql = "INSERT INTO pembeli (nama, kontak) VALUES (?, ?)"
        return database.execute_query(sql, (pb.nama, pb.kontak))

    def tambah_sumber(self, src: Sumber):
        sql = "INSERT INTO sumber (nama, alamat, kode_pos) VALUES (?, ?, ?)"
        return database.execute_query(sql, (src.nama, src.alamat, src.kode_pos))

    def get_dataframe_transaksi(self):
        sql = """
        SELECT t.tanggal, t.id_hp, h.merek, t.harga_beli, t.harga_jual,
               (t.harga_jual - t.harga_beli) AS untung
        FROM transaksi t
        JOIN hp h ON t.id_hp = h.id_hp
        ORDER BY t.tanggal DESC
        """
        return database.get_dataframe(sql)

    def total_untung(self):
        sql = "SELECT SUM(harga_jual - harga_beli) FROM transaksi"
        result = database.fetch_query(sql, fetch_all=False)
        return result[0] if result and result[0] else 0

    def get_dataframe_hp(self):
        sql = "SELECT * FROM hp ORDER BY id_hp"
        return database.get_dataframe(sql)