# Final Project API — GRAD-202 GET /cards/{id}

Kart məlumatı.

Hər ssenaridən əvvəl kontekst addımı user1 üçün yeni, boş sandbox açır (yeni login) — ssenarilər bir-birindən asılı deyil və istənilən ardıcıllıqla işləyir.

* FP user1 ilə yeni sandbox aç

## TC_API_CARDG_001 — Yeni kartın GET cavabı POST cavabı ilə eynidir
tags: regression, api, grad-202

* Initalize request specification
* Add Endpoint "/cards"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"accountId\":\"acc_002\",\"initialAmount\":100}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Save value of "id" as "cardA"
* Save value of "maskedPan" as "panA"
* Save value of "expiry" as "expA"
* Initalize request specification
* Add Endpoint "/cards/${cardA}"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "id" deyeri "cardA" ile eynidir
* Json cavabında "maskedPan" deyeri "panA" ile eynidir
* Json cavabında "expiry" deyeri "expA" ile eynidir
* Json cavabında "status" deyeri "ACTIVE" beraberdir
* Json cavabında "availableBalance" deyeri "100" beraberdir
* Json cavabında "spentToday" deyeri "0" beraberdir
* Json cavabında "limits.dailyOnline" deyeri "500" beraberdir

## TC_API_CARDG_002 — Ödənişdən sonra availableBalance azalır, spentToday artır
tags: regression, api, grad-202

* FP kart buraxılır "100" ve id-ni "cardA" olaraq saxla
* FP ödəniş et "${cardA}" "azercell" "501234567" "50.50"
* Initalize request specification
* Add Endpoint "/cards/${cardA}"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "availableBalance" deyeri "49.5" beraberdir
* Json cavabında "spentToday" deyeri "50.5" beraberdir

## TC_API_CARDG_003 — Başqa istifadəçinin kartı görünmür — 404
tags: regression, api, grad-202, security

* FP user2 tokenini al ve user1 üçün yeni sandbox aç
* FP kart buraxılır "100" ve id-ni "cardA" olaraq saxla
* Initalize request specification
* Add Endpoint "/cards/${cardA}"
* Add as a header "Authorization" = "${user2Token}"
* Get request and display respons
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "NOT_FOUND" beraberdir
