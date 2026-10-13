# Şeher seçimi

## TC_CITY_POS_001 - Şeher siyahısından Gence seçildikde header-de gösterilir
tags: regression, city

* Birmarket ana sehifesini aç
* "City Picker Block" elementine klik et
* "City Popup" görsensin deye maksimum "10" saniye gözle
* "City Popup Title" elementin içinde "Şəhərinizi seçin" yazısı var
* "City Item Ganja" elementine scroll et ve klik et
* "Current City" elementin içinde "Gəncə" yazısı var
* Brauzeri bağla

## TC_CITY_POS_002 - Seçilmiş şeher sehife yenilendikden sonra saxlanılır
tags: regression, city

* Birmarket ana sehifesini aç
* "City Picker Block" elementine klik et
* "City Popup" görsensin deye maksimum "10" saniye gözle
* "City Item Ganja" elementine scroll et ve klik et
* "Current City" elementin içinde "Gəncə" yazısı var
* Sehifeni yenile
* Sehifenin tam yüklenmesini gözle
* "Current City" elementin içinde "Gəncə" yazısı var
* Brauzeri bağla

## TC_CITY_NEG_007 - Şeher penceresi X ile bağlandıqda şeher deyişmir
tags: regression, city

* Birmarket ana sehifesini aç
* "Current City" elementin içinde "Bakı" yazısı var
* "City Picker Block" elementine klik et
* "City Popup" görsensin deye maksimum "10" saniye gözle
* "City Popup Close" elementine klik et
* "City Popup" görünmemelidir
* "Current City" elementin içinde "Bakı" yazısı var
* Brauzeri bağla
