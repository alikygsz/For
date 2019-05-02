sayi = int(input("başlangıç sayısını giriniz:")) #burada kullanıcının sayaca başlamak istediği sayıyı istiyorsun
bitis = int (input("bitiş sayısını giriniz:")) #burada kullanıcının sayacı bitirmek istediği sayıyı istiyorsun
artis = int (input("artış miktarını giriniz:")) #burada kullanıcının sayaca arttırmak istediği değeri istiyorsun

For i in range(sayi, bitis, artis) :
    print(i) 

