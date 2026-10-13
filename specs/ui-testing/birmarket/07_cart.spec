# Sebet

"Səbətə əlavə et" asılı ssenarilər production-da qeyri-deterministik olduğu (qonaq səbəti, rate-limit) üçün Manual regression-dadır.

## TC_CART_POS_011 - Boş sebet sehifesi birbaşa açıldıqda boş veziyyet gösterilir
tags: smoke, regression, cart

* Birmarket "https://birmarket.az/cart" sehifesini aç
* "Empty Cart Title" görsensin deye maksimum "15" saniye gözle
* "Empty Cart Title" elementin içinde "Səbət boşdur" yazısı var
* "Empty Cart Hint" elementin içinde "məhsul kataloquna" yazısı var
* "Empty Cart Catalog Link" görünür olmalıdır
* Brauzeri bağla