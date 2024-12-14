# 1) Bir aracın yakıt tipine göre (benzin,dizel,lpg) belirtilen bir mesafede ne kadar yakıt masrafı olduğunu hesaplayan uygulamayı yapınız.
# benzin    : 39.35
# dizel     : 41.71
# lpg       : 20.28

benzin = 39.35
dizel = 41.71
lpg = 20.28

mesafe = int(input("gidilen yol:"))

benzinMasrafi = (mesafe*benzin)
print("Benzin masrafı: " + benzinMasrafi)

dizelMasrafi = (mesafe*dizel)
print("Dizel masrafı: " + dizelMasrafi)

lpgMasrafi = (mesafe*lpg)
print("Lpg masrafı: " + lpgMasrafi)


# 2) Bir öğrencinin 2 vize 1 final notunu alarak ortalama hesaplayınız ve hesaplanan ortalamaya göre not aralığına karşılık gelen harf notunu yazdırınız.
#    90-100 => AA
#    80-89  => BA
#    70-79  => BB
#    60-69  => CB
#    50-59  => CC
#    40-49  => DC

vizeNotu1 = int(input("1. vize notunuz: "))
vizeNotu2 = int(input("2. vize notunuz: "))
finalNotu = int(input("Final notunuz: "))

ortalama = (vizeNotu1 + vizeNotu2 + finalNotu)/3
if(90<=ortalama<=100):
    print("Dönem sonu notunuz: AA")
elif(80<=ortalama<=89):
    print("Dönem sonu notunuz: BA")
elif(70<=ortalama<=79):
    print("Dönem sonu notunuz: BB")
elif(60<=ortalama<=69):
    print("Dönem sonu notunuz: CB")
elif(50<=ortalama<=59):
    print("Dönem sonu notunuz: CC")
elif(40<=ortalama<=49):
    print("Dönem sonu notunuz: DC")
else:
    print("Kaldınız")
