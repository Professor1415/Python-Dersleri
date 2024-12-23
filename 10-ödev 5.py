# Bankamatik Uygulaması

# Hesap bilgileri tutulacak. (dictionary)
# menu, paraCekme, bakiyeSorgula, paraYatirma fonksiyonları tanımlanacak.
# çekilmek istenen tutar hesapta yoksa ek hesabın kullanılmak istendiği sorulacak.


hesap={
    'bakiye':30000,
    'ek_bakiye':25000
}

def menu():
    print("-----Bankamatik-----")
    print("1) Bakiye Sorgulama")
    print("2) Para Çekme")
    print("3) Para Yatırma")
    print("4) Çıkış")

    secim=input("Lütfen yapmak istediğiniz işlemi seçiniz(1/2/3/4):")
    if secim == "1":
        bakiyeSorgulama()
    elif secim == "2":
        paraCekme()
    elif secim == "3":
        paraYatirma()
    elif secim == "4":
        print("Hesabınızdan çıkış yapılıyor, lütfen bekleyiniz.")
        print("Hesabınızdan çıkış yapılmıştır. İyi günler dileriz.")
        exit()
    else:
        print("Geçersiz bir işlem seçtiniz. Lütfen başka bir işlem seçiniz.")
        menu()

def bakiyeSorgulama():
    print(f"Hesabınızda {hesap['bakiye']} TL, ek hesabınızda {hesap['ek_bakiye']} TL vardır.")
    menu()

def paraCekme():
    cekilecekPara = float(input("Çekmek istediğiniz miktarı giriniz:"))
    if cekilecekPara <= hesap["bakiye"]:
        hesap["bakiye"] -= cekilecekPara
        print(f"{cekilecekPara} T hesabınızdan başarıyla çekilmiştir. Güncel bakiye: {hesap['bakiye']}")
        menu()
    elif cekilecekPara <= hesap['bakiye'] + hesap['ek_bakiye']:
        onay1 = input("Ek hesabınızdan para kullanılacaktır. Bu işlemi onaylıyor musunuz?(e/h):")
        if onay1 == "e":
            toplam_hesap = hesap["bakiye"] + hesap["ek_bakiye"]
            hesap["ek_bakiye"] = (toplam_hesap-cekilecekPara)
            hesap["bakiye"] = 0
            print(f"{cekilecekPara} TL hesabınızdan başarıyla çekilmiştir. Ek hesabınızda kalan para: {hesap['ek_bakiye']}")
            menu()
        elif onay1 == "h":
            print("İşleminiz iptal ediliyor, lütfen bekleyiniz.")
            print("İşleminiz iptal edilmiştir.")
            menu()
    else:
        onay2 = input(print("Hesabınızda yeterli miktarda para yoktur. İşleminize devam etmek istiyor musunuz?(e/h):"))
        if onay2 == "e":
            menu()
        elif onay2 == "h":
            print("Hesabınızdan çıkış yapılıyor, lütfen bekleyiniz.")
            print("Hesabınızdan çıkış yapılmıştır. İyi günler dileriz.")
            exit()

def paraYatirma():
    yatirilacakPara=float(input("Yatırmak istediğiniz miktar:"))
    hesap['bakiye']+=yatirilacakPara
    print(f"Para yatırma işlemi başarıyla tamamlandı. Güncel bakiye: {hesap['bakiye']}")
    menu()

menu()