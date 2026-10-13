# Final Project API — GRAD-303 GET /bill-payments

Ödəniş tarixçəsi: səhifələmə, filtr, tarix. Bakı vaxtı 23:30–00:30 arasında işlətməyin.

Hər ssenaridən əvvəl kontekst addımı user1 üçün yeni, boş sandbox açır (yeni login) — ssenarilər bir-birindən asılı deyil və istənilən ardıcıllıqla işləyir.

* FP user1 ilə yeni sandbox aç

## TC_API_HIS_001 — Parametrsiz tarixçə: page 1, limit 10, ən yeni birinci
tags: smoke, regression, api, grad-303

* FP tarixçə üçün 18 ödəniş et (12 Azercell, 6 CityNet)
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "page" deyeri "1" beraberdir
* Json cavabında "limit" deyeri "10" beraberdir
* Json cavabında "total" deyeri "18" beraberdir
* Json cavabında "totalPages" deyeri "2" beraberdir
* Json cavabında "items" massivinin ölçüsü "10" olmalıdır
* Json cavabında "items.createdAt" siyahısı azalan sırada olmalıdır

## TC_API_HIS_002 — page=2 qalan 8 elementi qaytarır
tags: regression, api, grad-303

* FP tarixçə üçün 18 ödəniş et (12 Azercell, 6 CityNet)
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Query parametri elave et "page" = "2"
* Query parametri elave et "limit" = "10"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "items" massivinin ölçüsü "8" olmalıdır
* Json cavabında "totalPages" deyeri "2" beraberdir

## TC_API_HIS_003 — Mövcud olmayan səhifə boş siyahı qaytarır
tags: regression, api, grad-303, bva

* FP tarixçə üçün 18 ödəniş et (12 Azercell, 6 CityNet)
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Query parametri elave et "page" = "3"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "items" massivinin ölçüsü "0" olmalıdır
* Json cavabında "total" deyeri "18" beraberdir

## TC_API_HIS_004 — limit BVA: 0 / 1 / 50 / 51
tags: regression, api, grad-303, bva

* FP tarixçə üçün 18 ödəniş et (12 Azercell, 6 CityNet)
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Query parametri elave et "limit" = "0"
* Get request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Query parametri elave et "limit" = "1"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "items" massivinin ölçüsü "1" olmalıdır
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Query parametri elave et "limit" = "50"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "items" massivinin ölçüsü "18" olmalıdır
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Query parametri elave et "limit" = "51"
* Get request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir

## TC_API_HIS_005 — page etibarsız dəyərləri: 0 / −1 / abc
tags: regression, api, grad-303, negative

* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Query parametri elave et "page" = "0"
* Get request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "page" olmalıdır
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Query parametri elave et "page" = "-1"
* Get request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "page" olmalıdır
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Query parametri elave et "page" = "abc"
* Get request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "page" olmalıdır

## TC_API_HIS_006 — Mövcud olmayan tarix rədd edilir
tags: regression, api, grad-303, negative

* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Query parametri elave et "from" = "2026-13-01"
* Get request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "from" olmalıdır
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Query parametri elave et "from" = "2026-02-30"
* Get request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "from" olmalıdır

## TC_API_HIS_008 — from > to rədd edilir
tags: regression, api, grad-303, negative

* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Query parametri elave et "from" = "2026-09-30"
* Query parametri elave et "to" = "2026-09-01"
* Get request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir

## TC_API_HIS_009 — from = to = bu gün — günün bütün ödənişləri (inclusive)
tags: regression, api, grad-303, bva

* FP tarixçə üçün 18 ödəniş et (12 Azercell, 6 CityNet)
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Query parametri elave et "from" = "${today}"
* Query parametri elave et "to" = "${today}"
* Query parametri elave et "limit" = "50"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "18" beraberdir

## TC_API_HIS_010 — billerId=citynet — yalnız CityNet ödənişləri
tags: regression, api, grad-303

* FP tarixçə üçün 18 ödəniş et (12 Azercell, 6 CityNet)
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Query parametri elave et "billerId" = "citynet"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "6" beraberdir
* Json cavabında "items.billerId" siyahısındakı bütün deyerler "citynet" olmalıdır

## TC_API_HIS_012 — Filtr + səhifələmə: total filtrdən sonrakı ümumi saydır
tags: regression, api, grad-303

* FP tarixçə üçün 18 ödəniş et (12 Azercell, 6 CityNet)
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Query parametri elave et "billerId" = "azercell"
* Query parametri elave et "limit" = "5"
* Query parametri elave et "page" = "3"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "12" beraberdir
* Json cavabında "totalPages" deyeri "3" beraberdir
* Json cavabında "items" massivinin ölçüsü "2" olmalıdır

## TC_API_HIS_014 — Tarixçə cavabı JSON Schema-ya uyğundur
tags: regression, api, grad-303, contract

* FP tarixçə üçün 18 ödəniş et (12 Azercell, 6 CityNet)
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Cavab "fp-payment-history-schema.json" JSON schema-sına uyğun olmalıdır
