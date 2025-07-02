import database

def setup_database():
    sql_hp = """
    CREATE TABLE IF NOT EXISTS hp (
        id_hp TEXT PRIMARY KEY,
        merek TEXT,
        ram INTEGER,
        storage INTEGER,
        kondisi TEXT,
        minus TEXT
    )"""

    sql_trx = """
    CREATE TABLE IF NOT EXISTS transaksi (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_hp TEXT,
        harga_beli REAL,
        harga_jual REAL,
        tanggal TEXT,
        FOREIGN KEY(id_hp) REFERENCES hp(id_hp)
    )"""

    sql_kerusakan = """
    CREATE TABLE IF NOT EXISTS kerusakan (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_hp TEXT,
        deskripsi TEXT,
        tingkat TEXT,
        biaya REAL,
        FOREIGN KEY(id_hp) REFERENCES hp(id_hp)
    )"""

    sql_pembeli = """
    CREATE TABLE IF NOT EXISTS pembeli (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT,
        kontak TEXT
    )"""

    sql_sumber = """
    CREATE TABLE IF NOT EXISTS sumber (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT,
        alamat TEXT,
        kode_pos TEXT
    )"""

    database.execute_query(sql_hp)
    database.execute_query(sql_trx)
    database.execute_query(sql_kerusakan)
    database.execute_query(sql_pembeli)
    database.execute_query(sql_sumber)

if __name__ == "__main__":
    setup_database()
    print("Database siap.")