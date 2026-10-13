# Şexsi kabinet – guest girişi

Guest istifadeçi şexsi sehifeleri birbaşa açdıqda giriş teleb olunur (data-driven).

|url                                  |
|-------------------------------------|
|https://birmarket.az/account         |
|https://birmarket.az/account/orders  |
|https://birmarket.az/account/id-card |

## TC_ACC_NEG_005 - Guest şexsi kabinet sehifelerini açdıqda giriş teleb olunur
tags: smoke, regression, account

* Birmarket <url> sehifesini aç
* Sehifede "Davam etmək üçün daxil olun" yazısı olmalıdır
* "Daxil ol" metnli elemente klik et
* "Phone Number Input" görsensin deye maksimum "20" saniye gözle
* URL "birid.kapitalbank.az" içermelidir
* Brauzeri bağla