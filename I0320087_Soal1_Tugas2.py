import math

#menampilkan informasi program

print("Menghitung Luas Persegi Panjang")
print("Contoh menghitung Luas Persegi Panjang ")
p = 10
print("Panjang = 10")
l = 5
print("Lebar = 5")
print("Luas Persegi panjang = P x L =", p * l)

#input sisi panjang
P = float(input("Masukkan nilai panjang: "))

#input sisi lebar
L = float(input("Masukkan nilai lebar: "))

#menghitung luas persegi panjang
Luas_Persegi_Panjang = P * L

#menampilkan hasil perhitungan ke layar
print("Luas Persegi Panjang: ", Luas_Persegi_Panjang)

#menampilkan informasi program

print("Menghitung Luas Lingkaran")
print("Contoh Menghitung Luas Lingkaran")
R = 7
print("Luas Lingkaran = 3.14 x r x r: ", 3.14 * (R ** 2))
print("Misal r = 7")
#input nilai jari-jari
r = float(input("Masukkan nilai jari-jari: "))

#menghitung luas lingkaran
Luas_Lingkaran = 3.14 * (r ** 2)

#menampilkan hasil perhitungan ke layar
print("Luas Lingkaran: ", Luas_Lingkaran)



#menampikan informasi program
print("Contoh Cara Menghitung Luas Permukaan Kubus")
print("Menghitung Luas Permukaan Kubus")
S = 10
print("Luas Permukaan Kubus = 6 x s x s: ", 6 * (S ** 2))

#input nilai sisi
s = float(input("Masukkan Nilai Sisi"))

#menghitung luas permukaan kubus
Luas_Permukaan_Kubus = 6 * (s ** 2)

#menampilkan hasil perhitungan ke layar
print("Luas Permukaan Kubus: ", Luas_Permukaan_Kubus)


#menampilkan informasi program
print("Menghitung Konversi Suhu Celcius ke Fahrenheit")
print("Contoh Cara Mengonversi Celcius ke Fahrenheit")
c = 25
print("Konversi Celcius ke Fahrenheit = (9 x C / 5) + 32: ",(9 * c / 5) + 32 )

#input suhu dalam celcius
C = float(input("Masukkan nilai suhu dalam Celcius"))

#melakukan konversi ke fahrenheit
F = (9 * C / 5) + 32

#menampilkan hasil konversi ke layar
print("Celcius: ", C)
print("Fahrenheit: ", F)


print("Menghitung Konversi Reamur ke Kelvin")

#input suhu dalam reamur
R = float(input("Masukkan nilai suhu dalam Reamur"))

#melakukan konversi suhu ke kelvin
K = (5 * R / 4) + 273

#menampilkan hasil konversi ke layar
print("Reamur: ", R)
print("Kelvin: ", K)




