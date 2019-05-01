sayi = int(input("başlangıç sayısını giriniz:")) #burada kullanıcının sayaca başlamak istediği sayıyı istiyorsun
bitis = int (input("bitiş sayısını giriniz:")) #burada kullanıcının sayacı bitirmek istediği sayıyı istiyorsun
artis = int (input("artış miktarını giriniz:")) #burada kullanıcının sayaca arttırmak istediği değeri istiyorsun

while(True):#burada döngüyü başlatıyorsun true döngü tamamlanana kadar sonsuz işlem yap demek
    print(sayi) #burada döngüde o an geçerli olan sayıyı yazdırıyorsun sayı arttıkça döngü tekrarlanıp büyüyen sayı yeniden yazılacak
    sayi = sayi + artis #sayının döngü içinde artış miktarı kadar artmasını istediğini belirtiyorsun
    if(sayi>=bitis): #son saayı bitiş sayısına ulaşırsa bitirmesini sağlayan komut
        break #programı bitirir
