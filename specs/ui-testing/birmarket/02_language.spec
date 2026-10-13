# Dil deyişimi

## TC_LANG_POS_001 - Dil AZ-dan RU-ya deyişdirildikde URL /ru prefiksi alır
tags: regression, language

* Birmarket ana sehifesini aç
* "Language Select Button" elementine klik et
* "Language Option Russian" elementine klik et
* Sehifenin tam yüklenmesini gözle
* URL "/ru" içermelidir
* "Html Root" elementinin "lang" atributu "ru" olmalıdır
* Brauzeri bağla

## TC_LANG_POS_002 - Dil RU-dan AZ-a qaytarıldıqda /ru prefiksi silinir
tags: regression, language

* Birmarket "https://birmarket.az/ru" sehifesini aç
* "Language Select Button" elementine klik et
* "Language Option Azerbaijani" elementine klik et
* Sehifenin tam yüklenmesini gözle
* "Html Root" elementinin "lang" atributu "az" olmalıdır
* Brauzeri bağla

## TC_LANG_POS_004 - RU interfeysinde kiril elifbası ile axtarış netice qaytarır
tags: regression, language, search

* Birmarket "https://birmarket.az/ru" sehifesini aç
* "Search Input" görsensin deye maksimum "20" saniye gözle
* Axtarış sahesine "телефон" yaz ve Axtar düymesine bas
* "Search Result Product Card" görsensin deye maksimum "20" saniye gözle
* "Search Result Product Card" elementlerinin sayı en az "1" olmalıdır
* Brauzeri bağla
