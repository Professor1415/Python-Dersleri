# 1- "Toyota, Bmw, Renault, Mercedes" elemanlarına sahip markalar isimli bir liste oluşturunuz.
markalar=["Toyota", "Bmw", "Renault", "Mercedes"]

# 2- Liste kaç elemanlıdır?
print(len(markalar))

# 3- Listenin ilk ve son elemanı nedir?
print(markalar[0], " ve ", markalar[-1])

# 4- "Renault" markasını "Togg" ile güncelleyiniz.
markalar[2]="Togg"
print(markalar)

# 5- "Togg" listenin bir elemanı mıdır?
sonuc="Togg" in markalar
print(sonuc)

# 6- Listenin sonuna "Ford" ve "Citroen" markalarını ekleyiniz.
markalar = markalar + ["Ford","Citroen"]
print(markalar)

# 7- Listenin son elemanını siliniz.
del markalar[-1]
print(markalar)

# 8- Aşağıdaki verileri liste içerisinde saklayınız (Liste içinde liste mümkündür.).

    # öğrenci1: Yiğit Bilgi 2010 [70,80,90]
    # öğrenci2: Ada Bilgi   2011 [70,70,80]
    # öğrenci3: Çınar Turan 2017 [60,60,90]
ogrenci1 = ["Yiğit", "Bilgi", 2010, [70, 80, 90]]
ogrenci2 = ["Ada", "Bilgi", 2011, [70, 70, 80]]
ogrenci3 = ["Çınar", "Turan", 2017, [60, 60, 90]]

# 9- Öğrencilerin yaşlarını hesaplayınız.
yasOgr1=2024-ogrenci1[2]
yasOgr2=2024-ogrenci2[2]
yasOgr3=2024-ogrenci3[2]

print(yasOgr1)
print(yasOgr2)
print(yasOgr3)

# 11- Öğrencilerin not ortalamalarını hesaplayınız.
ortOgr1=(ogrenci1[3][0]+ogrenci1[3][1]+ogrenci1[3][2])/3
ortOgr2=(ogrenci2[3][0]+ogrenci2[3][1]+ogrenci2[3][2])/3
ortOgr3=(ogrenci3[3][0]+ogrenci3[3][1]+ogrenci3[3][2])/3

print(ortOgr1)
print(ortOgr2)
print(ortOgr3)
