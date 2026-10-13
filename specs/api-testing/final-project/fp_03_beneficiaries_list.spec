# Final Project API — GRAD-102 GET /beneficiaries

Alıcılar siyahısı: sıralama, filtr, axtarış.

Hər ssenaridən əvvəl kontekst addımı user1 üçün yeni, boş sandbox açır (yeni login) — ssenarilər bir-birindən asılı deyil və istənilən ardıcıllıqla işləyir.

* FP user1 ilə yeni sandbox aç

## TC_API_BENL_001 — Parametrsiz siyahı: total = items sayı, ən yeni birinci
tags: smoke, regression, api, grad-102

* FP siyahı testləri üçün 5 alıcı yarat
* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "5" beraberdir
* Json cavabında "items" massivinin ölçüsü "5" olmalıdır
* Json cavabında "items[0].fullName" deyeri "Elvin Quliyev" beraberdir
* Json cavabında "items.createdAt" siyahısı azalan sırada olmalıdır

## TC_API_BENL_002 — Siyahı cavabı JSON Schema-ya uyğundur
tags: regression, api, grad-102, contract

* FP siyahı testləri üçün 5 alıcı yarat
* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Cavab "fp-beneficiary-list-schema.json" JSON schema-sına uyğun olmalıdır

## TC_API_BENL_003 — sort=fullName&order=asc Azərbaycan əlifbası ilə sıralayır
tags: regression, api, grad-102

* FP siyahı testləri üçün 5 alıcı yarat
* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Query parametri elave et "sort" = "fullName"
* Query parametri elave et "order" = "asc"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "items.fullName" deyeri "[Cavid Həsənov, Çingiz Abbasov, Elvin Quliyev, Əli Rzayev, Nigar Əliyeva]" beraberdir

## TC_API_BENL_006 — currency=USD yalnız USD alıcıları qaytarır
tags: regression, api, grad-102

* FP siyahı testləri üçün 5 alıcı yarat
* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Query parametri elave et "currency" = "USD"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "2" beraberdir
* Json cavabında "items.currency" siyahısındakı bütün deyerler "USD" olmalıdır

## TC_API_BENL_008 — q=NİGAR (nöqtəli İ) ilə axtarış tapır
tags: regression, api, grad-102

* FP siyahı testləri üçün 5 alıcı yarat
* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Query parametri elave et "q" = "NİGAR"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "1" beraberdir
* Json cavabında "items[0].fullName" deyeri "Nigar Əliyeva" beraberdir

## TC_API_BENL_009 — q=NIGAR (nöqtəsiz I) ilə axtarış tapır
tags: regression, api, grad-102

* FP siyahı testləri üçün 5 alıcı yarat
* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Query parametri elave et "q" = "NIGAR"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "1" beraberdir
* Json cavabında "items[0].fullName" deyeri "Nigar Əliyeva" beraberdir

## TC_API_BENL_011 — q ləqəbin bir hissəsi ilə ləqəbə görə tapır
tags: regression, api, grad-102

* FP siyahı testləri üçün 5 alıcı yarat
* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Query parametri elave et "q" = "ana"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "items.nickname" deyerinde "Anam" olmalıdır

## TC_API_BENL_013 — q=1 simvol rədd edilir
tags: regression, api, grad-102, bva

* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Query parametri elave et "q" = "a"
* Get request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "q" olmalıdır

## TC_API_BENL_014 — Heç nə tapılmadıqda boş siyahı qaytarılır
tags: regression, api, grad-102

* FP siyahı testləri üçün 5 alıcı yarat
* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Query parametri elave et "q" = "zzzz"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "0" beraberdir
* Json cavabında "items" massivinin ölçüsü "0" olmalıdır
