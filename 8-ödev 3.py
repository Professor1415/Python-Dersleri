sayilar = [3, 5, 7, 2, 12, 32, 45]


# 1- "sayilar" listesindeki her bir elemanı yazdırınız.

print("Sayılar listesindeki elemanlar:")
for i in sayilar:
    print(i, end = " ")


# 2- "sayilar" listesinde hangi sayılar 3' ün katıdır?

print("\nSayılar listesinde üçe bölünen elemanlar: ")
for x in sayilar:
    if x % 3 == 0:
        print(x)


# 3- "sayilar" listesinde tüm sayıların toplamı nedir?

print("Sayılar listesindeki elemanların toplamı: "+str(sum(sayilar)))




urunler=["iPhone 13","Samsung S24","Samsung S22","iPhone 15","iPhone 14"]


# 4- "urunler" listesindeki tüm iPhone marka ürünleri listeleyiniz. (index() ve find() komutlarından yararlanınız.)

SamsungUrunleri = iPhoneUrunleri = []

print("Ürünler listesindeki iPhone ürünleri: ")
for u in urunler:
    if u.find("iPhone") != -1:
        iPhoneUrunleri.append(u)
print(", ".join(iPhoneUrunleri))


# 5- "urunler" listesinde kaç adet Samsung ürünü vardır? (find metodu)

print("Ürünler listesindeki Samsung ürünlerinin sayısı: "+str(len(SamsungUrunleri)))
