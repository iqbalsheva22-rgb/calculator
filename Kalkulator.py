import math

def jalankan_kalkulator():
    print("=== KALKULATOR ILMIAH SEDERHANA ===")
    print("Pilih operasi:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Pangkat (x^y)")
    print("6. Sinus (sin)")
    print("7. Cosinus (cos)")
    print("8. Tangen (tan)")
    print("9. Keluar")

    while True:
        pilihan = input("\nMasukkan pilihan (1-9): ").strip()

        if pilihan == '9':
            print("Selesai!")
            break

        if pilihan in ['1', '2', '3', '4']:
            try:
                angka1 = float(input("Masukkan angka pertama: "))
                angka2 = float(input("Masukkan angka kedua: "))

                if pilihan == '1':
                    print(f"Hasil: {angka1} + {angka2} = {angka1 + angka2}")
                elif pilihan == '2':
                    print(f"Hasil: {angka1} - {angka2} = {angka1 - angka2}")
                elif pilihan == '3':
                    print(f"Hasil: {angka1} * {angka2} = {angka1 * angka2}")
                elif pilihan == '4':
                    if angka2 == 0:
                        print("Error: Tidak boleh pembagian dengan angka nol!")
                    else:
                        print(f"Hasil: {angka1} / {angka2} = {angka1 / angka2}")
            except ValueError:
                print("Error: Input harus berupa angka!")

        elif pilihan == '5':
            try:
                basis = float(input("Masukkan basis (x): "))
                eksponen = float(input("Masukkan pangkat (y): "))
                hasil = math.pow(basis, eksponen)
                print(f"Hasil {basis} ^ {eksponen} = {hasil}")
            except ValueError:
                print("Error: Input harus angka!")
            except OverflowError:
                print("Error: Hasil terlalu besar!")

        elif pilihan in ['6', '7', '8']:
            try:
                derajat = float(input("Masukkan besar sudut dalam derajat: "))
                radian = math.radians(derajat)
                
                if pilihan == '6':
                    hasil = math.sin(radian)
                    print(f"Hasil sin({derajat}°) = {hasil:.4f}")
                elif pilihan == '7':
                    hasil = math.cos(radian)
                    if abs(hasil) < 1e-9:
                        hasil = 0.0
                    print(f"Hasil cos({derajat}°) = {hasil:.4f}")
                elif pilihan == '8':
                    if derajat % 180 == 90:
                        print(f"Hasil tan({derajat}°) = Tak hingga")
                    else:
                        hasil = math.tan(radian)
                        print(f"Hasil tan({derajat}°) = {hasil:.4f}")
            except ValueError:
                print("Error: Input harus berupa angka!")
                
        else:
            print("Pilihan hanya 1-9.")

if __name__ == "__main__":
    jalankan_kalkulator()
