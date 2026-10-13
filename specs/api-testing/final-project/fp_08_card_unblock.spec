# Final Project API — GRAD-204 POST /cards/{id}/unblock

Dondurulmuş kartı açmaq.

Hər ssenaridən əvvəl kontekst addımı user1 üçün yeni, boş sandbox açır (yeni login) — ssenarilər bir-birindən asılı deyil və istənilən ardıcıllıqla işləyir.

* FP user1 ilə yeni sandbox aç

## TC_API_UNB_001 — FROZEN kart açılır → ACTIVE
tags: regression, api, grad-204, state-transition

* FP kart buraxılır "10" ve id-ni "x" olaraq saxla
* FP kartın statusunu dəyiş "${x}" "TEMPORARY"
* Initalize request specification
* Add Endpoint "/cards/${x}/unblock"
* Add as a header "Authorization" = "token"
* Post request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "ACTIVE" beraberdir
* Json cavabında "blockReason" deyeri null olmalıdır
* Json cavabında "blockedAt" deyeri null olmalıdır

## TC_API_UNB_002 — ACTIVE kart açılmağa çalışılır → 409 NOT_FROZEN
tags: regression, api, grad-204, state-transition

* FP kart buraxılır "10" ve id-ni "x" olaraq saxla
* Initalize request specification
* Add Endpoint "/cards/${x}/unblock"
* Add as a header "Authorization" = "token"
* Post request and display respons
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "NOT_FROZEN" beraberdir

## TC_API_UNB_003 — LOST ilə bloklanmış kart açılmır → 409 PERMANENTLY_BLOCKED
tags: regression, api, grad-204, state-transition

* FP kart buraxılır "10" ve id-ni "x" olaraq saxla
* FP kartın statusunu dəyiş "${x}" "LOST"
* Initalize request specification
* Add Endpoint "/cards/${x}/unblock"
* Add as a header "Authorization" = "token"
* Post request and display respons
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "PERMANENTLY_BLOCKED" beraberdir
* Initalize request specification
* Add Endpoint "/cards/${x}"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "BLOCKED" beraberdir

## TC_API_UNB_004 — STOLEN ilə bloklanmış kart açılmır → 409 PERMANENTLY_BLOCKED
tags: regression, api, grad-204, state-transition

* FP kart buraxılır "10" ve id-ni "x" olaraq saxla
* FP kartın statusunu dəyiş "${x}" "STOLEN"
* Initalize request specification
* Add Endpoint "/cards/${x}/unblock"
* Add as a header "Authorization" = "token"
* Post request and display respons
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "PERMANENTLY_BLOCKED" beraberdir

## TC_API_UNB_005 — Açılmış kartla ödəniş uğurla keçir
tags: regression, api, grad-204, state-transition

* FP kart buraxılır "100" ve id-ni "x" olaraq saxla
* FP kartın statusunu dəyiş "${x}" "TEMPORARY"
* Initalize request specification
* Add Endpoint "/cards/${x}/unblock"
* Add as a header "Authorization" = "token"
* Post request and display respons
* Status kodunun "200" olmalıdır
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${x}\",\"billerId\":\"azercell\",\"subscriberNo\":\"501234567\",\"amount\":10}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "SUCCESS" beraberdir
* Json cavabında "balanceAfter" deyeri "90" beraberdir
