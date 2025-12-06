SURVEI = [
    {
    "pertanyaan": "Siapa minuman favoritmu?",
    "opsi": ["Kopi", "Teh", "Air Putih"]
    },
    {
    "pertanyaan": "Apa sosmed favoritmu?",
    "opsi": ["Instagram", "Facebook", "TikTok","X"]
    },
    {
    "pertanyaan": "Apa destinasi favoritmu?",
    "opsi": ["Musium", "Kolam Renang", "Taman Safari"]
    }
]

hasil_polling = {}
for item_survei in SURVEI:
    for opsi in item_survei["opsi"]:
        hasil_polling[opsi] = 0

print(45*"=")
print("     SELAMAT DATANG DI APLIKASI POLLING")
print(45*"=")

for idx, item_survei in enumerate(SURVEI, start=1): # enumerate = biar ada nomornya
    print(f"\nPertanyaan {idx}: {item_survei['pertanyaan']}")
    for opsi in item_survei["opsi"]: # nampilin semua pilihan jawaban
        print(f" - {opsi}")

    while True:
        jawaban = input("Jawaban Anda: ")
        if jawaban in item_survei["opsi"]:
            print(f"> {jawaban}")
            if jawaban == 'Allah':
                print("-- Alhamdulillah --")
            elif jawaban == 'Islam':
                print('-- MasyaAllah --')
            elif jawaban == 'Muhammad':
                print('-- Kerenn --')
            hasil_polling[jawaban] += 1
            break
        else:
            print('???')
            
print('\n')
print(45*"=")
print("                HASIL POLLING")
print(45*"=","\n")
for opsi, jumlah in hasil_polling.items():
    print(f"{opsi} : {jumlah} suara")
print(45*"=")