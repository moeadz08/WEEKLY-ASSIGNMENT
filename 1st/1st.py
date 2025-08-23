"kasir cerdas 1.0"

def salam_pembuka():
    print("=" * 32)
    print("         SELAMAT DATANG!")
    print("=" * 32)

salam_pembuka()

# Input Barang 1
print('\n--- Masukkan Detail Barang 1 ---')
nama_barang_1 = input("Nama Barang: ")
harga_1 = float(input('Harga Satuan: Rp '))
jumlah_1 = int(input("Jumlah: "))

# Input Barang 2
print("\n--- Masukkan Detail Barang 2 ---")
nama_barang_2 = input("Nama Barang: ")
harga_2 = float(input("Harga Satuan: Rp "))
jumlah_2 = int(input("Jumlah: "))

print("Menghitung total...")

# Perhitungan dasar
total_1 = harga_1 * jumlah_1
total_2 = harga_2 * jumlah_2
subtotal = total_1 + total_2

# Diskon
diskon = subtotal * 0.10
setelah_diskon = subtotal - diskon

# PPN 11%
ppn = setelah_diskon * 0.11
total_bayar = setelah_diskon + ppn

# Input uang dibayar dan hitung kembalian
uang_dibayar = float(input("\nMasukkan jumlah uang yang dibayarkan: Rp "))
kembalian = uang_dibayar - total_bayar

# setruk
print("\n" + "=" * 32)
print("       STRUK PEMBELIAN ANDA")
print("=" * 32)
print("\nDetail Belanja:")
print(f"1. {nama_barang_1} ({jumlah_1} x Rp {harga_1}) = Rp {total_1}")
print(f"2. {nama_barang_2} ({jumlah_2} x Rp {harga_2}) = Rp {total_2}")
print("-" * 32)
print(f"Subtotal         : Rp {subtotal}")
print(f"Diskon (10%)     : - Rp {diskon}")
print(f"PPN (11%)        : + Rp {ppn}")
print("-" * 32)
print(f"Total Dibayar    : Rp {total_bayar}")
print(f"Uang Dibayar     : Rp {uang_dibayar}")
print(f"Kembalian        : Rp {kembalian}")
print("\n" + "=" * 32)
print(" TERIMA KASIH TELAH BERBELANJA!")
print("=" * 32)





