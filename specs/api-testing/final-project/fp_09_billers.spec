# Final Project API — GRAD-301 GET /billers

Xidmət təchizatçıları kataloqu.

Hər ssenaridən əvvəl kontekst addımı user1 üçün yeni, boş sandbox açır (yeni login) — ssenarilər bir-birindən asılı deyil və istənilən ardıcıllıqla işləyir.

* FP user1 ilə yeni sandbox aç

## TC_API_BIL_001 — Parametrsiz kataloq 6 təchizatçı qaytarır
tags: smoke, regression, api, grad-301

* Initalize request specification
* Add Endpoint "/billers"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "6" beraberdir
* Json cavabında "items" massivinin ölçüsü "6" olmalıdır
* Json cavabında "items.subscriberPattern" massivinin ölçüsü "6" olmalıdır
* Json cavabında "items.minAmount" massivinin ölçüsü "6" olmalıdır
* Json cavabında "items.maxAmount" massivinin ölçüsü "6" olmalıdır
* Json cavabında "items.fee" massivinin ölçüsü "6" olmalıdır

## TC_API_BIL_002 — Kataloq datası sənədlə üst-üstə düşür (min/max)
tags: regression, api, grad-301

* Initalize request specification
* Add Endpoint "/billers"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "items.find { it.id == 'azerisiq' }.minAmount" deyeri "1" beraberdir
* Json cavabında "items.find { it.id == 'azerisiq' }.maxAmount" deyeri "500" beraberdir
* Json cavabında "items.find { it.id == 'azersu' }.minAmount" deyeri "1" beraberdir
* Json cavabında "items.find { it.id == 'azersu' }.maxAmount" deyeri "300" beraberdir
* Json cavabında "items.find { it.id == 'azercell' }.minAmount" deyeri "0.5" beraberdir
* Json cavabında "items.find { it.id == 'azercell' }.maxAmount" deyeri "200" beraberdir
* Json cavabında "items.find { it.id == 'bakcell' }.minAmount" deyeri "0.5" beraberdir
* Json cavabında "items.find { it.id == 'bakcell' }.maxAmount" deyeri "200" beraberdir
* Json cavabında "items.find { it.id == 'citynet' }.minAmount" deyeri "5" beraberdir
* Json cavabında "items.find { it.id == 'citynet' }.maxAmount" deyeri "150" beraberdir
* Json cavabında "items.find { it.id == 'aztelekom' }.minAmount" deyeri "2" beraberdir
* Json cavabında "items.find { it.id == 'aztelekom' }.maxAmount" deyeri "100" beraberdir

## TC_API_BIL_003 — Komissiya qaydaları düzgündür
tags: regression, api, grad-301

* Initalize request specification
* Add Endpoint "/billers"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "items.find { it.id == 'citynet' }.fee.type" deyeri "PERCENT" beraberdir
* Json cavabında "items.find { it.id == 'citynet' }.fee.value" deyeri "1" beraberdir
* Json cavabında "items.find { it.id == 'citynet' }.fee.min" deyeri "0.2" beraberdir
* Json cavabında "items.find { it.id == 'citynet' }.fee.max" deyeri "2" beraberdir
* Json cavabında "items.find { it.id == 'aztelekom' }.fee" deyerinde "0.5" olmalıdır

## TC_API_BIL_004 — category=MOBILE yalnız Azercell və Bakcell qaytarır
tags: regression, api, grad-301

* Initalize request specification
* Add Endpoint "/billers"
* Add as a header "Authorization" = "token"
* Query parametri elave et "category" = "MOBILE"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "2" beraberdir
* Json cavabında "items.id" deyerinde "azercell" olmalıdır
* Json cavabında "items.id" deyerinde "bakcell" olmalıdır
* Json cavabında "items.category" siyahısındakı bütün deyerler "MOBILE" olmalıdır

## TC_API_BIL_007 — Etibarsız category (GAS) rədd edilir
tags: regression, api, grad-301, negative

* Initalize request specification
* Add Endpoint "/billers"
* Add as a header "Authorization" = "token"
* Query parametri elave et "category" = "GAS"
* Get request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir

## TC_API_BIL_009 — Kataloq cavabı JSON Schema-ya uyğundur
tags: regression, api, grad-301, contract

* Initalize request specification
* Add Endpoint "/billers"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Cavab "fp-biller-list-schema.json" JSON schema-sına uyğun olmalıdır
