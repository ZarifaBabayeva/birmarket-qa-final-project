# Seçilmişler (guest)

## TC_FAV_POS_001 - Guest mehsulu login olmadan seçilmişlere elave edir
tags: smoke, regression, favorites

* Kateqoriya sehifesini aç ve mehsulların yüklenmesini gözle
* "First Product Title" elementinin metnini "favTitle" olaraq yadda saxla
* "First Product Favorite Icon" elementine klik et
* "Header Favorites Count" görsensin deye maksimum "10" saniye gözle
* "Header Favorites Count" elementinin metni "1" olmalıdır
* "Header Favorites Link" elementine klik et
* "Favorites Product Card" görsensin deye maksimum "15" saniye gözle
* "Favorites Page Title" elementin içinde "Seçilmişlər" yazısı var
* "Favorites Product Card" elementlerinin sayı "1" olmalıdır
* "Favorites First Product Title" elementinin metni "${favTitle}" olmalıdır
* Brauzeri bağla

## TC_FAV_POS_003 - Guest-in seçilmişleri sehife yenilendikden sonra saxlanılır
tags: regression, favorites

* Kateqoriya sehifesini aç ve mehsulların yüklenmesini gözle
* "First Product Favorite Icon" elementine klik et
* "Header Favorites Count" görsensin deye maksimum "10" saniye gözle
* "Header Favorites Link" elementine klik et
* "Favorites Product Card" görsensin deye maksimum "15" saniye gözle
* Sehifeni yenile
* Sehifenin tam yüklenmesini gözle
* "Favorites Product Card" görsensin deye maksimum "15" saniye gözle
* "Favorites Product Card" elementlerinin sayı "1" olmalıdır
* Brauzeri bağla

## TC_FAV_POS_008 - Guest mehsulu seçilmişlerden sildikde siyahıdan çıxır
tags: regression, favorites

* Kateqoriya sehifesini aç ve mehsulların yüklenmesini gözle
* "First Product Favorite Icon" elementine klik et
* "Header Favorites Count" görsensin deye maksimum "10" saniye gözle
* "Header Favorites Link" elementine klik et
* "Favorites Product Card" görsensin deye maksimum "15" saniye gözle
* "Favorites Remove Icon" elementine klik et
* "Favorites Product Card" sehifede mövcud olmamalıdır
* Brauzeri bağla
