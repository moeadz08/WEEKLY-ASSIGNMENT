"kasir cerdas 2.0"
'''
n = 1
while n <= 7:
    print(f'angka: {n}')
    n += 1
else:
    print("stop"))
'''


def tampilkan_header():
    print("=" * 44)
    print("      SELAMAT DATANG DI TOKO SERBA ADA")
    print("=" * 44)
    print("\n--- Masukkan Detail Barang ---")
    print("(Ketik 'selesai' di nama barang untuk selesai)\n")

def hitung_subtotal(daftar_harga, daftar_jumlah):
    subtotal = 0
    for i in range(len(daftar_harga)):
        subtotal += daftar_harga[i] * daftar_jumlah[i]
    return subtotal

def hitung_diskon(subtotal):
    if subtotal >= 500000:
        persen = 10
    elif subtotal >= 300000:
        persen = 5
    else:
        persen = 0
    jumlah_diskon = subtotal * (persen / 100)
    return jumlah_diskon, persen

def tampilkan_struk(semua_nama, semua_harga, semua_jumlah, subtotal, total_diskon, persen_diskon):
    print("\n" + "=" * 44)
    print("         STRUK PEMBELIAN ANDA")
    print("=" * 44)
    print("Detail Belanja:")

    for i in range(len(semua_nama)):
        total = semua_harga[i] * semua_jumlah[i]
        print(f"{i+1}. {semua_nama[i]:17} ({semua_jumlah[i]} x Rp {semua_harga[i]}) = Rp {total}")

    print("-" * 44)
    print(f"Subtotal            : Rp {subtotal}")
    print(f"Diskon ({persen_diskon}%)        : - Rp {total_diskon}")
    print("-" * 44)
    total_akhir = subtotal - total_diskon
    print(f"Total yang harus dibayar: Rp {total_akhir}")
    print("=" * 44)
    print("     TERIMA KASIH TELAH BERBELANJA!")
    print("=" * 44)

daftar_nama_barang = []
daftar_harga_barang = []
daftar_jumlah_barang = []

tampilkan_header()

while True: # ngulang minta input
    nama_barang = input("Nama Barang: ")
    if nama_barang.lower() == "selesai":
        break

    try:
        harga = float(input("Harga Satuan: Rp "))
        jumlah = int(input("Jumlah: "))
    except ValueError:
        print("Input tidak valid. Coba lagi.\n")
        continue

    daftar_nama_barang.append(nama_barang)
    daftar_harga_barang.append(harga)
    daftar_jumlah_barang.append(jumlah)

    print("--- Barang berhasil ditambahkan! ---\n")

print("\nMenghitung total belanja Anda...") # subtotal
subtotal = hitung_subtotal(daftar_harga_barang, daftar_jumlah_barang)

total_diskon, persen_diskon = hitung_diskon(subtotal) # diskon

tampilkan_struk( # setruk
    daftar_nama_barang,
    daftar_harga_barang,
    daftar_jumlah_barang,
    subtotal,
    total_diskon,
    persen_diskon
)

































