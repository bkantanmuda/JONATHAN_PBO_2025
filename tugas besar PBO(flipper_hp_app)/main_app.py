### File: main_app.py

import streamlit as st

# ⬇️ HARUS di baris paling atas sebelum elemen Streamlit lainnya
st.set_page_config(page_title="Manajemen Flipper HP", layout="wide")

import datetime
from model import HP, Transaksi
from konfigurasi import KONDISI_HP, MEREK_HP
from manajer_flipper import ManajerFlipper
from setup_db_flipper import setup_database

setup_database()  # Inisialisasi DB jika belum ada
flipper = ManajerFlipper()

st.title("Aplikasi Manajemen Flipper HP")
st.caption("Jonathan Edward Sinaga | 4.33.24.0.14")
menu = st.sidebar.radio("Pilih Menu", ["Tambah HP", "Transaksi", "Riwayat", "Data HP"])

if menu == "Tambah HP":
    st.header("Tambah Data HP")
    with st.form("form_hp"):
        id_hp = st.text_input("ID HP", placeholder="wajib diisi dan tidak boleh double")
        merek = st.text_input("Merek HP", placeholder="Contoh: Xiaomi")
        ram = st.number_input("RAM (GB)", min_value=1)
        storage = st.number_input("Storage (GB)", min_value=4)
        kondisi = st.selectbox("Kondisi", KONDISI_HP)
        minus = st.text_area("Minus/Kerusakan", placeholder="Contoh: Layar retak, baterai bocor (opsional)")

        submitted = st.form_submit_button("Simpan")
        if submitted:
            if not id_hp or not merek:
                st.warning("ID HP dan Merek wajib diisi!")
            else:
                if flipper.tambah_hp(HP(id_hp, merek, ram, storage, kondisi), minus):
                    st.success("HP berhasil disimpan!")
                else:
                    st.error("Gagal menyimpan HP. ID mungkin sudah ada.")

elif menu == "Transaksi":
    st.header("Transaksi Jual Beli HP")
    with st.form("form_trx"):
        id_hp = st.text_input("ID HP")
        harga_beli = st.number_input("Harga Beli", min_value=0.0)
        harga_jual = st.number_input("Harga Jual", min_value=0.0)
        tanggal = st.date_input("Tanggal Transaksi", value=datetime.date.today())
        submitted = st.form_submit_button("Simpan Transaksi")
        if submitted:
            if flipper.tambah_transaksi(Transaksi(id_hp, harga_beli, harga_jual, tanggal.strftime("%Y-%m-%d"))):
                st.success("Transaksi berhasil disimpan!")
            else:
                st.error("Gagal menyimpan transaksi")

elif menu == "Riwayat":
    st.header("Riwayat Transaksi Flipper HP")
    df = flipper.get_dataframe_transaksi()
    st.dataframe(df, use_container_width=True)
    st.metric("Total Keuntungan", f"Rp {flipper.total_untung():,.0f}".replace(",", "."))

elif menu == "Data HP":
    st.header("📄 Tabel Data HP Tersimpan")
    df_hp = flipper.get_dataframe_hp()
    st.dataframe(df_hp, use_container_width=True)
