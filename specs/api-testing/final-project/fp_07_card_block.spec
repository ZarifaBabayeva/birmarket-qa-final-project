# Final Project API — GRAD-203 POST /cards/{id}/block

Kartı bloklamaq / dondurmaq — state transition cədvəli.

Hər ssenaridən əvvəl kontekst addımı user1 üçün yeni, boş sandbox açır (yeni login) — ssenarilər bir-birindən asılı deyil və istənilən ardıcıllıqla işləyir.

* FP user1 ilə yeni sandbox aç

## TC_API_BLK_001 — ACTIVE + TEMPORARY → FROZEN
tags: smoke, regression, api, grad-203, state-transition

* FP kart buraxılır "100" ve id-ni "x" olaraq saxla
* Initalize request specification
* Add Endpoint "/cards/${x}/block"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"reason\":\"TEMPORARY\"}"
* Post request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "FROZEN" beraberdir
* Json cavabında "blockReason" deyeri "TEMPORARY" beraberdir
* Json cavabında "blockedAt" deyeri boş olmamalıdır

## TC_API_BLK_002 — ACTIVE + LOST → BLOCKED
tags: regression, api, grad-203, state-transition

* FP kart buraxılır "10" ve id-ni "x" olaraq saxla
* Initalize request specification
* Add Endpoint "/cards/${x}/block"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"reason\":\"LOST\"}"
* Post request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "BLOCKED" beraberdir
* Json cavabında "blockReason" deyeri "LOST" beraberdir

## TC_API_BLK_003 — ACTIVE + STOLEN → BLOCKED
tags: regression, api, grad-203, state-transition

* FP kart buraxılır "10" ve id-ni "x" olaraq saxla
* Initalize request specification
* Add Endpoint "/cards/${x}/block"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"reason\":\"STOLEN\"}"
* Post request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "BLOCKED" beraberdir
* Json cavabında "blockReason" deyeri "STOLEN" beraberdir

## TC_API_BLK_004 — FROZEN + TEMPORARY → 409 ALREADY_FROZEN
tags: regression, api, grad-203, state-transition

* FP kart buraxılır "10" ve id-ni "x" olaraq saxla
* FP kartın statusunu dəyiş "${x}" "TEMPORARY"
* Initalize request specification
* Add Endpoint "/cards/${x}/block"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"reason\":\"TEMPORARY\"}"
* Post request and display respons
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "ALREADY_FROZEN" beraberdir
* Initalize request specification
* Add Endpoint "/cards/${x}"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "FROZEN" beraberdir

## TC_API_BLK_005 — FROZEN + LOST → BLOCKED (eskalasiya)
tags: regression, api, grad-203, state-transition

* FP kart buraxılır "10" ve id-ni "x" olaraq saxla
* FP kartın statusunu dəyiş "${x}" "TEMPORARY"
* Initalize request specification
* Add Endpoint "/cards/${x}/block"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"reason\":\"LOST\"}"
* Post request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "BLOCKED" beraberdir
* Json cavabında "blockReason" deyeri "LOST" beraberdir

## TC_API_BLK_006 — FROZEN + STOLEN → BLOCKED (eskalasiya)
tags: regression, api, grad-203, state-transition

* FP kart buraxılır "10" ve id-ni "x" olaraq saxla
* FP kartın statusunu dəyiş "${x}" "TEMPORARY"
* Initalize request specification
* Add Endpoint "/cards/${x}/block"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"reason\":\"STOLEN\"}"
* Post request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "BLOCKED" beraberdir
* Json cavabında "blockReason" deyeri "STOLEN" beraberdir

## TC_API_BLK_007 — BLOCKED + TEMPORARY → 409 CARD_BLOCKED
tags: regression, api, grad-203, state-transition

* FP kart buraxılır "10" ve id-ni "x" olaraq saxla
* FP kartın statusunu dəyiş "${x}" "LOST"
* Initalize request specification
* Add Endpoint "/cards/${x}/block"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"reason\":\"TEMPORARY\"}"
* Post request and display respons
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "CARD_BLOCKED" beraberdir

## TC_API_BLK_010 — Etibarsız reason (BROKEN) rədd edilir, kart ACTIVE qalır
tags: regression, api, grad-203, negative

* FP kart buraxılır "10" ve id-ni "x" olaraq saxla
* Initalize request specification
* Add Endpoint "/cards/${x}/block"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"reason\":\"BROKEN\"}"
* Post request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "reason" olmalıdır
* Initalize request specification
* Add Endpoint "/cards/${x}"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "ACTIVE" beraberdir

## TC_API_BLK_011 — reason sahəsi olmadan rədd edilir
tags: regression, api, grad-203, negative

* FP kart buraxılır "10" ve id-ni "x" olaraq saxla
* Initalize request specification
* Add Endpoint "/cards/${x}/block"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{}"
* Post request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "reason" olmalıdır

## TC_API_BLK_016 — Başqa istifadəçinin kartı bloklana bilmir — 404
tags: regression, api, grad-203, security

* FP user2 tokenini al ve user1 üçün yeni sandbox aç
* FP kart buraxılır "10" ve id-ni "x" olaraq saxla
* Initalize request specification
* Add Endpoint "/cards/${x}/block"
* Add as a header "Authorization" = "${user2Token}"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"reason\":\"LOST\"}"
* Post request and display respons
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "NOT_FOUND" beraberdir
* Initalize request specification
* Add Endpoint "/cards/${x}"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "ACTIVE" beraberdir

## TC_API_BLK_017 — FROZEN kartla ödəniş rədd edilir
tags: regression, api, grad-203, state-transition

* FP kart buraxılır "100" ve id-ni "x" olaraq saxla
* FP kartın statusunu dəyiş "${x}" "TEMPORARY"
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${x}\",\"billerId\":\"azercell\",\"subscriberNo\":\"501234567\",\"amount\":10}"
* Post request and display respons
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "CARD_NOT_ACTIVE" beraberdir
* Initalize request specification
* Add Endpoint "/cards/${x}"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "availableBalance" deyeri "100" beraberdir

## TC_API_BLK_018 — BLOCKED kartla ödəniş rədd edilir
tags: regression, api, grad-203, state-transition

* FP kart buraxılır "100" ve id-ni "x" olaraq saxla
* FP kartın statusunu dəyiş "${x}" "LOST"
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${x}\",\"billerId\":\"azercell\",\"subscriberNo\":\"501234567\",\"amount\":10}"
* Post request and display respons
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "CARD_NOT_ACTIVE" beraberdir
