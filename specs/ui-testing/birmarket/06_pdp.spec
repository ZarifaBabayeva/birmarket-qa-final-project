# Mehsul sehifesi (PDP)

## TC_PDP_POS_001 - PDP-de ad ve qiymet kartdakı ile eynidir
tags: smoke, regression, pdp

* Birmarket "https://birmarket.az/categories/129-yag-qizdiricilari" sehifesini aç
* "First Product Card" görsensin deye maksimum "20" saniye gözle
* "First Product Title" elementinin metnini "cardTitle" olaraq yadda saxla
* "First Product Price" elementinin metnini "cardPrice" olaraq yadda saxla
* "First Product Link" elementine klik et
* Yeni açılan taba keç
* "PDP Title" görsensin deye maksimum "20" saniye gözle
* "PDP Title" elementin içinde "${cardTitle}" yazısı var
* "PDP Price" elementinin metni "${cardPrice}" olmalıdır
* Brauzeri bağla

## TC_PDP_POS_002 - PDP-de esas elementler gösterilir
tags: regression, pdp

* Kateqoriyadan ilk mehsulun PDP sehifesini aç
* "PDP Title" görünür olmalıdır
* "PDP Product Code" elementin içinde "Məhsulun kodu" yazısı var
* "PDP Main Image" görünür olmalıdır
* "PDP Price" elementin içinde "₼" yazısı var
* "PDP Add To Cart Button" görünür olmalıdır
* "PDP Favorite Button" görünür olmalıdır
* "Credit Calculator" görünür olmalıdır
* Brauzeri bağla

## TC_PDP_POS_015 - Kredit müddeti artdıqca aylıq ödeniş azalır
tags: regression, pdp, credit

* Kateqoriyadan ilk mehsulun PDP sehifesini aç
* "Credit Calculator" elementine scroll et
* "Credit Option 6 Months" elementine klik et
* "PDP Credit Info" elementin içinde "x 6" yazısı var
* "PDP Credit Info" elementinin metnini "monthly6" olaraq yadda saxla
* "Credit Option 24 Months" elementine klik et
* "PDP Credit Info" elementin içinde "x 24" yazısı var
* "PDP Credit Info" elementinin metnini "monthly24" olaraq yadda saxla
* "monthly6" deyişenindeki eded "monthly24" deyişenindeki ededden böyük olmalıdır
* Brauzeri bağla

## TC_PDP_NEG_005 - Mövcud olmayan mehsul URL-i 404 sehifesi gösterir
tags: regression, pdp

* Birmarket "https://birmarket.az/product/999999999-not-exist" sehifesini aç
* Sehifede "Səhifə tapılmadı" yazısı olmalıdır
* Brauzeri bağla