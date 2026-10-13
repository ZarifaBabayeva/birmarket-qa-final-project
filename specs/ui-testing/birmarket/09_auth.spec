# Giriş (Bir ID) – OTP-ye qeder olan hisse

OTP real SMS teleb etdiyi üçün yalnız telefon addımı avtomatlaşdırılıb.

## TC_AUTH_POS_001 - "Qeydiyyat | Giriş" linki telefon nömresi ile giriş ekranını açır
tags: smoke, regression, auth

* Telefon ile giriş sehifesini aç
* URL "birid.kapitalbank.az" içermelidir
* "Auth Page Title" elementin içinde "Birmarket" yazısı var
* "Send Code Button" elementin içinde "Kodu göndər" yazısı var
* Brauzeri bağla

## TC_AUTH_NEG_002 - Telefon sahesi boş olduqda xeta gösterilir
tags: smoke, regression, auth

* Telefon ile giriş sehifesini aç
* "Send Code Button" elementine klik et
* "Phone Error Message" görsensin deye maksimum "5" saniye gözle
* "Phone Error Message" elementin içinde "Telefon nömrəsi yanlışdır" yazısı var
* "OTP Input" sehifede mövcud olmamalıdır
* Brauzeri bağla

## TC_AUTH_BVA_003 - 8 reqemli nömre ile "Telefon nömrəsi yanlışdır" xetası gösterilir
tags: smoke, regression, auth

* Telefon ile giriş sehifesini aç
* "Phone Number Input" elementine klik et
* "Phone Number Input" elementine "50123456" yaz ve Tab düymesine bas
* "Send Code Button" elementine klik et
* Sehifenin tam yüklenmesini gözle
* "Phone Error Message" görsensin deye maksimum "15" saniye gözle
* "Phone Error Message" elementin içinde "Telefon nömrəsi yanlışdır" yazısı var
* "OTP Input" sehifede mövcud olmamalıdır
* Brauzeri bağla

## TC_AUTH_NEG_006 - Telefon sahesine herf ve xüsusi simvollar daxil edile bilmir
tags: regression, auth

* Telefon ile giriş sehifesini aç
* "Phone Number Input" elementine klik et
* "Phone Number Input" elementine "abc!@#" yaz ve Tab düymesine bas
* "Phone Number Input" input deyeri "abc!@#" olmamalıdır
* Brauzeri bağla