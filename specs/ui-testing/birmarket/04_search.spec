# Axtarış

## TC_SRCH_POS_001 - Mövcud açar sözle (iphone) axtarış neticeleri qaytarılır
tags: smoke, regression, search

* Birmarket ana sehifesini aç
* Axtarış sahesine "iphone" yaz ve Axtar düymesine bas
* URL "/tags/iphone" içermelidir
* "Search Result Product Card" görsensin deye maksimum "20" saniye gözle
* "Products Found Count" elementin içinde "Tapılan məhsul" yazısı var
* "Search Result Product Title" siyahısının ilk "5" elementinde "iphone" yazısı olmalıdır
* Brauzeri bağla

## TC_SRCH_POS_002 - Axtarış böyük/kiçik herfe hessas deyil
tags: regression, search

* Birmarket ana sehifesini aç
* Axtarış sahesine "iphone" yaz ve Axtar düymesine bas
* "Products Found Count" görsensin deye maksimum "20" saniye gözle
* "Products Found Count" elementinin metnini "lowerCount" olaraq yadda saxla
* Axtarış sahesine "IPHONE" yaz ve Axtar düymesine bas
* "Products Found Count" görsensin deye maksimum "20" saniye gözle
* "Products Found Count" elementinin metni "${lowerCount}" olmalıdır
* Brauzeri bağla

## TC_SRCH_POS_008 - Axtarış Enter düymesi ile de icra olunur
tags: regression, search

* Birmarket ana sehifesini aç
* "Search Input" elementine "iphone" yaz ve Enter düymesine bas
* Sehifenin tam yüklenmesini gözle
* URL "/tags/iphone" içermelidir
* "Search Result Product Card" görsensin deye maksimum "20" saniye gözle
* Brauzeri bağla

## TC_SRCH_POS_009 - Axtarış neticesindeki karta klik PDP-ni açır
tags: regression, search

* Birmarket ana sehifesini aç
* Axtarış sahesine "iphone" yaz ve Axtar düymesine bas
* "First Product Link" görsensin deye maksimum "20" saniye gözle
* "First Product Link" elementine klik et
* Yeni açılan taba keç
* "PDP Title" görsensin deye maksimum "20" saniye gözle
* URL "/product/" içermelidir
* Brauzeri bağla

## TC_SRCH_NEG_003 - Mövcud olmayan açar sözle axtarışda boş netice mesajı gösterilir
tags: smoke, regression, search

* Birmarket ana sehifesini aç
* Axtarış sahesine "qwxzqwxz123" yaz ve Axtar düymesine bas
* "No Result Container" görsensin deye maksimum "20" saniye gözle
* "No Result Title" elementin içinde "Sorğuya uyğun məhsul tapılmadı" yazısı var
* "No Result Hint" görünür olmalıdır
* "Search Result Product Card" sehifede mövcud olmamalıdır
* "Search Input" input deyeri "qwxzqwxz123" olmalıdır
* Brauzeri bağla

## TC_SRCH_NEG_004 - Boş axtarış sahesi ile Axtar düymesi axtarışı icra etmir
tags: regression, search

* Birmarket ana sehifesini aç
* "Search Button" elementine klik et
* "2" saniye gözle
* URL "https://birmarket.az/" olmalıdır
* Brauzeri bağla
