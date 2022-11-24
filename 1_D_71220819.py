print("Kalkulator Sederhana Python\n")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

pil = int(input("\nMasukan Pilihan Operasi : "))

x= int(input("Bilangan 1 : "))
y= int(input("Bilangan 2 : "))

if pil == 1:
   hasil = x+y
elif pil == 2:
   hasil = x-y
elif pil == 3:
   hasil = x*y
elif pil == 4:
   hasil = x/y

print("\nHasil : %d" %hasil)

print('=' * 25)
print('Operasi Matematika')
print('  1. Jumlah \t [+]')
print('  2. Kurang \t [-]')
print('  3. Kali \t [*]')
print('  4. Bagi \t [/]')
print('=' * 25)

operasi = input('Pilih operasi (1/2/3/4): ')
bilangan_1 = eval(input('5: '))
bilangan_2 = eval(input('3: '))

=========================
Operasi Matematika
  1. Jumlah      [+]
  2. Kurang      [-]
  3. Kali        [*]
  4. Bagi        [/]
=========================
Pilih operasi (1/2/3/4): 3
Masukkan bilangan pertama: 10
Masukkan bilangan kedua: 5













ahun = input("2000: ")

if (tahun % 4) == 0:
    if (tahun % 100) == 0:
        if (tahun % 400) == 0:
            print "Tahun Kabisat"
        else:
            print "Bukan Tahun Kabisat"
    else:
        print "Tahun Kabisat"
else:
    print "Bukan Tahun Kabisat"

