# Ana sehife ve Header

Test mühiti: https://birmarket.az (Production, guest)

## TC_HOME_POS_001 - Guest ana sehifeni açdıqda esas header elementleri gösterilir
tags: smoke, regression, home

* Birmarket ana sehifesini aç
* "Header Logo" görünür olmalıdır
* "Search Input" görünür olmalıdır
* "Search Button" görünür olmalıdır
* "Catalog Button" görünür olmalıdır
* "City Picker Block" görünür olmalıdır
* "Auth Link" görünür olmalıdır
* "Header Favorites Link" görünür olmalıdır
* "Header Cart Link" görünür olmalıdır
* Brauzeri bağla

## TC_HOME_POS_002 - Daxili sehifeden logoya klik ana sehifeye qaytarır
tags: regression, home

* Birmarket "https://birmarket.az/cart" sehifesini aç
* "Header Logo" elementine klik et
* Sehifenin tam yüklenmesini gözle
* URL "https://birmarket.az/" olmalıdır
* Brauzeri bağla
