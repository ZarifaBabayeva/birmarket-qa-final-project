# Kateqoriya ve mehsul siyahısı (PLP)

## TC_CAT_POS_002 - Kateqoriya sehifesi mehsullarla açılır
tags: smoke, regression, category

* Kateqoriya sehifesini aç ve mehsulların yüklenmesini gözle
* "Page Heading" görünür olmalıdır
* "Breadcrumb" görünür olmalıdır
* "Product Card" elementlerinin sayı en az "1" olmalıdır
* Brauzeri bağla

## TC_CAT_POS_003 - Breadcrumb-da Birmarket linki ana sehifeye aparır
tags: regression, category

* Kateqoriya sehifesini aç ve mehsulların yüklenmesini gözle
* "Breadcrumb Home Link" elementine klik et
* Sehifenin tam yüklenmesini gözle
* URL "https://birmarket.az/" olmalıdır
* Brauzeri bağla

## TC_CAT_NEG_006 - Mövcud olmayan kateqoriya URL-i 404 sehifesi gösterir
tags: regression, category

* Birmarket "https://birmarket.az/categories/999999999-not-exist" sehifesini aç
* Sehifede "Səhifə tapılmadı" yazısı olmalıdır
* Brauzeri bağla

## TC_PLP_POS_022 - Sıralama seçicisinde 5 seçim gösterilir
tags: regression, plp, sort

* Kateqoriya sehifesini aç ve mehsulların yüklenmesini gözle
* "Sort Box" elementine scroll et ve klik et
* "Sort Dropdown" görsensin deye maksimum "5" saniye gözle
* "Sort Option Item" elementlerinin sayı "5" olmalıdır
* Brauzeri bağla

## TC_PLP_POS_001 - "Ən ucuz" sıralamada qiymetler artan sırada gösterilir
tags: smoke, regression, plp, sort

* Kateqoriya sehifesini aç ve mehsulların yüklenmesini gözle
* "Sort Box" elementine scroll et ve klik et
* "Sort Option Cheapest" elementine klik et
* Sehifenin tam yüklenmesini gözle
* "Sort Selected Label" elementin içinde "Ən ucuz" yazısı var
* "Product Prices" elementlerindeki qiymetler artan sırada olmalıdır
* Brauzeri bağla

## TC_PLP_POS_002 - "Ən bahalı" sıralamada qiymetler azalan sırada gösterilir
tags: regression, plp, sort

* Kateqoriya sehifesini aç ve mehsulların yüklenmesini gözle
* "Sort Box" elementine scroll et ve klik et
* "Sort Option Most Expensive" elementine klik et
* Sehifenin tam yüklenmesini gözle
* "Sort Selected Label" elementin içinde "Ən bahalı" yazısı var
* "Product Prices" elementlerindeki qiymetler azalan sırada olmalıdır
* Brauzeri bağla

## TC_PLP_POS_023 - "Ən böyük endirimli" sıralamada endirim faizleri azalan sırada gösterilir
tags: regression, plp, sort

* Kateqoriya sehifesini aç ve mehsulların yüklenmesini gözle
* "Sort Box" elementine scroll et ve klik et
* "Sort Option Biggest Discount" elementine klik et
* Sehifenin tam yüklenmesini gözle
* "Product Discount Badge" elementlerindeki qiymetler azalan sırada olmalıdır
* Brauzeri bağla

## TC_PLP_POS_024 - "Ən ucuz" sıralama 2-ci sehifede de davam edir
tags: regression, plp, sort

* Kateqoriya sehifesini aç ve mehsulların yüklenmesini gözle
* "Sort Box" elementine scroll et ve klik et
* "Sort Option Cheapest" elementine klik et
* Sehifenin tam yüklenmesini gözle
* "Sort Selected Label" elementin içinde "Ən ucuz" yazısı var
* "Product Prices" elementlerindeki qiymetler artan sırada olmalıdır
* "Next Page Button" elementine scroll et
* "Next Page Button" elementine JavaScript ile klik et
* Sehifenin tam yüklenmesini gözle
* "Sort Selected Label" elementin içinde "Ən ucuz" yazısı var
* "Product Prices" elementlerindeki qiymetler artan sırada olmalıdır
* Brauzeri bağla

## TC_PLP_POS_006 - 2-ci sehifeye keçid ferqli mehsullar gösterir
tags: regression, plp, pagination

* Kateqoriya sehifesini aç ve mehsulların yüklenmesini gözle
* "First Product Title" elementinin metnini "page1Title" olaraq yadda saxla
* "Next Page Button" elementine scroll et ve klik et
* Sehifenin tam yüklenmesini gözle
* "First Product Card" görsensin deye maksimum "20" saniye gözle
* "First Product Title" elementinin metni "${page1Title}" olmamalıdır
* Brauzeri bağla

## TC_PLP_POS_003 - Qiymet filtri (100–200) yalnız hemin aralıqda mehsulları gösterir
tags: smoke, regression, plp, filter

* Birmarket "https://birmarket.az/categories/2?price_from=100&price_to=200" sehifesini aç
* "First Product Card" görsensin deye maksimum "20" saniye gözle
* "Price Min Input" input deyeri "100" olmalıdır
* "Price Max Input" input deyeri "200" olmalıdır
* "Product Prices" elementlerindeki qiymetler "100" ile "200" arasında olmalıdır
* Brauzeri bağla

## TC_PLP_POS_017 - "Endirimli" filtri yalnız endirimli mehsulları gösterir
tags: regression, plp, filter

* Kateqoriya sehifesini aç ve mehsulların yüklenmesini gözle
* "Discount Filter Checkbox" elementine scroll et ve klik et
* Sehifenin tam yüklenmesini gözle
* "3" saniye gözle
* "Product Card" elementlerinin sayı "Product Old Prices" elementlerinin sayına beraber olmalıdır
* Brauzeri bağla


## TC_PLP_BVA_005 - Qiymet filtrine menfi deyer (-1) qebul edilmir
tags: regression, plp, filter

* Kateqoriya sehifesini aç ve mehsulların yüklenmesini gözle
* "Price Min Input" elementine scroll et
* "Price Min Input" elementine klik et
* "Price Min Input" elementine "-1" yaz ve Tab düymesine bas
* "Price Min Input" input deyeri "-1" olmamalıdır
* Brauzeri bağla

## TC_PLP_NEG_013 - Qiymet filtrine herf daxil edildikde qebul edilmir
tags: regression, plp, filter

* Kateqoriya sehifesini aç ve mehsulların yüklenmesini gözle
* "Price Min Input" elementine scroll et
* "Price Min Input" elementine "abc" yaz ve Tab düymesine bas
* "Price Min Input" input deyeri "abc" olmamalıdır
* Brauzeri bağla

## TC_PLP_NEG_014 - Mövcud olmayan sehife nömresi (page=99999) xetasız idare olunur
tags: regression, plp, pagination

* Birmarket "https://birmarket.az/categories/2?page=99999" sehifesini aç
* "Search Input" görsensin deye maksimum "20" saniye gözle
* "Header Logo" görünür olmalıdır
* Brauzeri bağla
