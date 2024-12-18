# 1- Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız. 


def Goster(kelime, tekrar_sayısı):

    for i in range(tekrar_sayısı):
        print(kelime)

Goster("Merhaba", 4)

# 2- Dikdörgenin alan ve çevresini hesaplayan fonksiyonu yazınız.


def Hesapla(a,b):
    alan=a*b
    cevre=2*(a+b)
    return alan, cevre

print(Hesapla(10,2))


# 3- Yazı tura uygulamasını fonksiyon kullanarak yapınız. (Random modülü)


import random
def Yazıtura():
    sonuc=["yazı","tura"]
    secim=random.choice(sonuc)
    return secim

print(Yazıtura())

# 4- Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız.


def hangileri_asal(bas,son):
     asal_sayilar=[]

     for sayi in range(bas,son+1):
         if sayi>1:
             for x in range(2,int(sayi**0.5)+1):
                 if sayi % x == 0:
                     break
             else:
                     asal_sayilar.append(sayi)
     return asal_sayilar

bas=5
son=50
print(f"{bas} ve {son} arasındaki asal sayılar:{hangileri_asal(bas,son)}")


# 5- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız.


def tam_bolenler(sayi):
    bolenler=[]

    for x in range(1,int(sayi)+1):
        if sayi%x==0:
            bolenler.append(x)
        
        
    
    return bolenler

sayi=50
print(f"{sayi} sayısının tam bölenleri:{tam_bolenler(sayi)}")