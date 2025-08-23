try: 
    with open("transaksi_kotor.txt", "r") as file_input:
        with open("laporan_bersih.txt", "w") as file_output:
            # tulis header
            file_output.write("LAPORAN TRANSAKSI BERSIH\n")
            file_output.write("=========================\n\n")

            grand_total = 0  

            for baris in file_input:
                baris = baris.strip()
                if not baris:  
                    continue

                data_potongan = baris.split(",")
                id_bersih = data_potongan[0].strip().upper()
                nama_bersih = data_potongan[1].strip().title()
                jumlah_bersih = int(data_potongan[2].strip())
                harga_bersih = float(data_potongan[3].strip())

                total_harga = jumlah_bersih * harga_bersih

                
                if total_harga > 500000:
                    string_output = f"ID: {id_bersih} | Produk: {nama_bersih} | Jumlah: {jumlah_bersih} | Total Harga: Rp {total_harga}\n"
                    file_output.write(string_output)
                    grand_total += total_harga

            
            file_output.write("\n--- ANALISIS SELESAI ---\n")
            file_output.write(f"TOTAL KESELURUHAN: Rp {grand_total}\n")

    print("Proses pembersihan data selesai. Laporan disimpan di laporan_bersih.txt")

except FileNotFoundError:
    print("File 'transaksi_kotor.txt' tidak ditemukan.")
