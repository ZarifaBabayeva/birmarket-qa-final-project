# Final Project API — GRAD-103 DELETE /beneficiaries/{id}

Alıcını silmək.

Hər ssenaridən əvvəl kontekst addımı user1 üçün yeni, boş sandbox açır (yeni login) — ssenarilər bir-birindən asılı deyil və istənilən ardıcıllıqla işləyir.

* FP user1 ilə yeni sandbox aç

## TC_API_BEND_001 — Mövcud alıcı silinir — 204, body boş
tags: regression, api, grad-103

* FP alıcı yarat "Nigar Əliyeva" "AZ77AIIB40060019440123456789" "AZN" "-" ve id-ni "benA" olaraq saxla
* Initalize request specification
* Add Endpoint "/beneficiaries/${benA}"
* Add as a header "Authorization" = "token"
* Delete request and display response
* Status kodunun "204" olmalıdır
* Cavab body-si boş olmalıdır

## TC_API_BEND_002 — Silinmiş alıcı siyahıda görünmür, total 1 azalır
tags: regression, api, grad-103

* FP alıcı yarat "Nigar Əliyeva" "AZ77AIIB40060019440123456789" "AZN" "-" ve id-ni "benA" olaraq saxla
* FP alıcı yarat "Cavid Həsənov" "AZ12NABZ00000000000000000102" "USD" "-" ve id-ni "benB" olaraq saxla
* Initalize request specification
* Add Endpoint "/beneficiaries/${benA}"
* Add as a header "Authorization" = "token"
* Delete request and display response
* Status kodunun "204" olmalıdır
* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "1" beraberdir
* Json cavabında "items[0].id" deyeri "${benB}" beraberdir

## TC_API_BEND_003 — Eyni alıcı ikinci dəfə silindikdə 404
tags: regression, api, grad-103, negative

* FP alıcı yarat "Nigar Əliyeva" "AZ77AIIB40060019440123456789" "AZN" "-" ve id-ni "benA" olaraq saxla
* Initalize request specification
* Add Endpoint "/beneficiaries/${benA}"
* Add as a header "Authorization" = "token"
* Delete request and display response
* Status kodunun "204" olmalıdır
* Initalize request specification
* Add Endpoint "/beneficiaries/${benA}"
* Add as a header "Authorization" = "token"
* Delete request and display response
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "NOT_FOUND" beraberdir

## TC_API_BEND_004 — Başqa istifadəçinin alıcısı silinə bilmir — 404
tags: regression, api, grad-103, security

* FP user2 tokenini al ve user1 üçün yeni sandbox aç
* FP alıcı yarat "Nigar Əliyeva" "AZ77AIIB40060019440123456789" "AZN" "-" ve id-ni "benA" olaraq saxla
* Initalize request specification
* Add Endpoint "/beneficiaries/${benA}"
* Add as a header "Authorization" = "${user2Token}"
* Delete request and display response
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "NOT_FOUND" beraberdir
* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "items[0].id" deyeri "${benA}" beraberdir
