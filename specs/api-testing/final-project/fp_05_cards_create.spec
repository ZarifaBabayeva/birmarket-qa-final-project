# Final Project API — GRAD-201 POST /cards

Virtual kart buraxmaq.

Hər ssenaridən əvvəl kontekst addımı user1 üçün yeni, boş sandbox açır (yeni login) — ssenarilər bir-birindən asılı deyil və istənilən ardıcıllıqla işləyir.

* FP user1 ilə yeni sandbox aç

## TC_API_CARD_001 — Etibarlı sorğu ilə virtual kart buraxılır
tags: smoke, regression, api, grad-201

* Initalize request specification
* Add Endpoint "/cards"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"accountId\":\"acc_002\",\"initialAmount\":100,\"label\":\"Kommunal\"}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyeri "^vcd_[a-z0-9]{8}$" regex-ine uyğun olmalıdır
* Json cavabında "status" deyeri "ACTIVE" beraberdir
* Json cavabında "availableBalance" deyeri "100" beraberdir
* Json cavabında "currency" deyeri "AZN" beraberdir
* Json cavabında "limits.dailyOnline" deyeri "500" beraberdir
* Json cavabında "limits.perTransaction" deyeri "300" beraberdir
* Json cavabında "spentToday" deyeri "0" beraberdir
* Json cavabında "blockReason" deyeri null olmalıdır
* Json cavabında "blockedAt" deyeri null olmalıdır
* Json cavabında "label" deyeri "Kommunal" beraberdir
* Save value of "id" as "cardA"
* Header "Location" deyerinde "/cards/${cardA}" olmalıdır

## TC_API_CARD_002 — maskedPan və expiry formatı düzgündür
tags: regression, api, grad-201

* Initalize request specification
* Add Endpoint "/cards"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"accountId\":\"acc_002\",\"initialAmount\":50}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "maskedPan" deyeri "^4169 73[*]{2} [*]{4} [0-9]{4}$" regex-ine uyğun olmalıdır
* Json cavabında "expiry" deyeri "^[0-9]{2}/[0-9]{2}$" regex-ine uyğun olmalıdır
* Json cavabında "expiry" deyeri bu gündən 3 il sonranın ay/il dəyəri olmalıdır

## TC_API_CARD_003 — Kart cavabı JSON Schema-ya uyğundur
tags: regression, api, grad-201, contract

* Initalize request specification
* Add Endpoint "/cards"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"accountId\":\"acc_002\",\"initialAmount\":20}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Cavab "fp-card-schema.json" JSON schema-sına uyğun olmalıdır

## TC_API_CARD_005 — initialAmount 0.99 rədd edilir
tags: regression, api, grad-201, bva

* Initalize request specification
* Add Endpoint "/cards"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"accountId\":\"acc_002\",\"initialAmount\":0.99}"
* Post request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "initialAmount" olmalıdır

## TC_API_CARD_006 — initialAmount 1.00 qəbul edilir
tags: regression, api, grad-201, bva

* Initalize request specification
* Add Endpoint "/cards"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"accountId\":\"acc_002\",\"initialAmount\":1.00}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "availableBalance" deyeri "1" beraberdir

## TC_API_CARD_007 — initialAmount 1000.00 qəbul edilir
tags: regression, api, grad-201, bva

* Initalize request specification
* Add Endpoint "/cards"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"accountId\":\"acc_002\",\"initialAmount\":1000.00}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "availableBalance" deyeri "1000" beraberdir

## TC_API_CARD_008 — initialAmount 1000.01 rədd edilir
tags: regression, api, grad-201, bva

* Initalize request specification
* Add Endpoint "/cards"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"accountId\":\"acc_002\",\"initialAmount\":1000.01}"
* Post request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "initialAmount" olmalıdır

## TC_API_CARD_009 — initialAmount mətn kimi ("50") rədd edilir
tags: regression, api, grad-201, negative

* Initalize request specification
* Add Endpoint "/cards"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"accountId\":\"acc_002\",\"initialAmount\":\"50\"}"
* Post request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "initialAmount" olmalıdır

## TC_API_CARD_010 — initialAmount 3 onluqlu (10.555) rədd edilir
tags: regression, api, grad-201, negative

* Initalize request specification
* Add Endpoint "/cards"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"accountId\":\"acc_002\",\"initialAmount\":10.555}"
* Post request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "initialAmount" olmalıdır

## TC_API_CARD_011 — initialAmount 0 və mənfi dəyər rədd edilir
tags: regression, api, grad-201, negative

* Initalize request specification
* Add Endpoint "/cards"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"accountId\":\"acc_002\",\"initialAmount\":0}"
* Post request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "initialAmount" olmalıdır
* Initalize request specification
* Add Endpoint "/cards"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"accountId\":\"acc_002\",\"initialAmount\":-10}"
* Post request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "initialAmount" olmalıdır

## TC_API_CARD_013 — Məcburi accountId olmadan rədd edilir
tags: regression, api, grad-201, negative

* Initalize request specification
* Add Endpoint "/cards"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"initialAmount\":100}"
* Post request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "accountId" olmalıdır

## TC_API_CARD_014 — Başqa istifadəçinin hesabı ilə kart açıla bilmir (403)
tags: regression, api, grad-201, security

* Initalize request specification
* Add Endpoint "/cards"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"accountId\":\"acc_003\",\"initialAmount\":100}"
* Post request and display respons
* Status kodunun "403" olmalıdır
* Json cavabında "code" deyeri "FORBIDDEN" beraberdir

## TC_API_CARD_016 — Balansdan çox məbləğ rədd edilir (user2: 891 > 890.50)
tags: regression, api, grad-201, bva

* FP user2 tokenini al ve user1 üçün yeni sandbox aç
* Initalize request specification
* Add Endpoint "/cards"
* Add as a header "Authorization" = "${user2Token}"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"accountId\":\"acc_003\",\"initialAmount\":891}"
* Post request and display respons
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "INSUFFICIENT_FUNDS" beraberdir

## TC_API_CARD_017 — Balansa bərabər məbləğ qəbul edilir, kart USD olur
tags: regression, api, grad-201, bva

* FP user2 tokenini al ve user1 üçün yeni sandbox aç
* Initalize request specification
* Add Endpoint "/cards"
* Add as a header "Authorization" = "${user2Token}"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"accountId\":\"acc_003\",\"initialAmount\":890.50}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "availableBalance" deyeri "890.5" beraberdir
* Json cavabında "currency" deyeri "USD" beraberdir

## TC_API_CARD_018 — 4-cü ACTIVE kart limitə görə rədd edilir
tags: regression, api, grad-201, bva

* FP kart buraxılır "10" ve id-ni "c1" olaraq saxla
* FP kart buraxılır "10" ve id-ni "c2" olaraq saxla
* FP kart buraxılır "10" ve id-ni "c3" olaraq saxla
* Initalize request specification
* Add Endpoint "/cards"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"accountId\":\"acc_002\",\"initialAmount\":10}"
* Post request and display respons
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "CARD_LIMIT_REACHED" beraberdir

## TC_API_CARD_019 — FROZEN kart da limitə sayılır
tags: regression, api, grad-201, state-transition

* FP kart buraxılır "10" ve id-ni "c1" olaraq saxla
* FP kart buraxılır "10" ve id-ni "c2" olaraq saxla
* FP kart buraxılır "10" ve id-ni "c3" olaraq saxla
* FP kartın statusunu dəyiş "${c3}" "TEMPORARY"
* Initalize request specification
* Add Endpoint "/cards"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"accountId\":\"acc_002\",\"initialAmount\":10}"
* Post request and display respons
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "CARD_LIMIT_REACHED" beraberdir

## TC_API_CARD_020 — BLOCKED kart limitə sayılmır — yeni kart açılır
tags: regression, api, grad-201, state-transition

* FP kart buraxılır "10" ve id-ni "c1" olaraq saxla
* FP kart buraxılır "10" ve id-ni "c2" olaraq saxla
* FP kart buraxılır "10" ve id-ni "c3" olaraq saxla
* FP kartın statusunu dəyiş "${c3}" "LOST"
* Initalize request specification
* Add Endpoint "/cards"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"accountId\":\"acc_002\",\"initialAmount\":10}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "ACTIVE" beraberdir
