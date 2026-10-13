# Final Project API — GRAD-302 POST /bill-payments

Kommunal ödəniş: komissiya, balans, idempotency, limitlər. Bakı vaxtı 23:30–00:30 arasında işlətməyin (spentToday sıfırlanır).

Hər ssenaridən əvvəl kontekst addımı user1 üçün yeni, boş sandbox açır (yeni login) — ssenarilər bir-birindən asılı deyil və istənilən ardıcıllıqla işləyir.

* FP user1 ilə yeni sandbox aç

## TC_API_PAY_001 — CityNet-ə etibarlı ödəniş — komissiya və balans düzgün
tags: smoke, regression, api, grad-302

* FP kart buraxılır "1000" ve id-ni "P" olaraq saxla
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"citynet\",\"subscriberNo\":\"CN123456\",\"amount\":50}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "SUCCESS" beraberdir
* Json cavabında "amount" deyeri "50" beraberdir
* Json cavabında "fee" deyeri "0.5" beraberdir
* Json cavabında "total" deyeri "50.5" beraberdir
* Json cavabında "balanceAfter" deyeri "949.5" beraberdir
* Json cavabında "currency" deyeri "AZN" beraberdir
* Json cavabında "biller.id" deyeri "citynet" beraberdir
* Json cavabında "biller.category" deyeri "INTERNET" beraberdir
* Save value of "id" as "payId"
* Header "Location" deyerinde "/bill-payments/${payId}" olmalıdır

## TC_API_PAY_002 — Ödəniş cavabı JSON Schema-ya uyğundur
tags: regression, api, grad-302, contract

* FP kart buraxılır "1000" ve id-ni "P" olaraq saxla
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"azercell\",\"subscriberNo\":\"501234567\",\"amount\":5}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Cavab "fp-payment-schema.json" JSON schema-sına uyğun olmalıdır

## TC_API_PAY_003 — Ödənişdən sonra kart balansı və spentToday total qədər dəyişir
tags: regression, api, grad-302

* FP kart buraxılır "1000" ve id-ni "P" olaraq saxla
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"citynet\",\"subscriberNo\":\"CN123456\",\"amount\":20}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Initalize request specification
* Add Endpoint "/cards/${P}"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "availableBalance" deyeri "979.8" beraberdir
* Json cavabında "spentToday" deyeri "20.2" beraberdir

## TC_API_PAY_004 — receiptNo formatı və ardıcıl artımı
tags: regression, api, grad-302

* FP kart buraxılır "1000" ve id-ni "P" olaraq saxla
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"azercell\",\"subscriberNo\":\"501234567\",\"amount\":1}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "receiptNo" deyeri "^RCP-[0-9]{8}-000001$" regex-ine uyğun olmalıdır
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"azercell\",\"subscriberNo\":\"501234567\",\"amount\":1}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "receiptNo" deyeri "^RCP-[0-9]{8}-000002$" regex-ine uyğun olmalıdır

## TC_API_PAY_005 — Eyni Idempotency-Key + eyni body təkrarı pul çıxarmır
tags: smoke, regression, api, grad-302, idempotency

* FP kart buraxılır "1000" ve id-ni "P" olaraq saxla
* "k1" deyişenine "${random.uuid}" deyerini ver
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${k1}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"citynet\",\"subscriberNo\":\"CN123456\",\"amount\":50}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Save value of "id" as "firstId"
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${k1}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"citynet\",\"subscriberNo\":\"CN123456\",\"amount\":50}"
* Post request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "id" deyeri "firstId" ile eynidir
* Header "Idempotent-Replay" deyerinde "true" olmalıdır
* Initalize request specification
* Add Endpoint "/cards/${P}"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "availableBalance" deyeri "949.5" beraberdir

## TC_API_PAY_006 — Eyni Idempotency-Key fərqli məbləğlə → 409
tags: regression, api, grad-302, idempotency

* FP kart buraxılır "1000" ve id-ni "P" olaraq saxla
* "k1" deyişenine "${random.uuid}" deyerini ver
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${k1}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"citynet\",\"subscriberNo\":\"CN123456\",\"amount\":50}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${k1}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"citynet\",\"subscriberNo\":\"CN123456\",\"amount\":60}"
* Post request and display respons
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "IDEMPOTENCY_CONFLICT" beraberdir
* Initalize request specification
* Add Endpoint "/cards/${P}"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "availableBalance" deyeri "949.5" beraberdir

## TC_API_PAY_007 — Idempotency-Key olmadan ödəniş rədd edilir
tags: regression, api, grad-302, idempotency

* FP kart buraxılır "1000" ve id-ni "P" olaraq saxla
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"azercell\",\"subscriberNo\":\"501234567\",\"amount\":5}"
* Post request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "IDEMPOTENCY_KEY_REQUIRED" beraberdir

## TC_API_PAY_008 — Idempotency-Key uzunluğu BVA: 7 / 8 / 64 / 65 simvol
tags: regression, api, grad-302, bva

* FP kart buraxılır "1000" ve id-ni "P" olaraq saxla
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "kkkkkkk"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"azercell\",\"subscriberNo\":\"501234567\",\"amount\":1}"
* Post request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "IDEMPOTENCY_KEY_INVALID" beraberdir
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "kkkkkkkk"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"azercell\",\"subscriberNo\":\"501234567\",\"amount\":1}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"azercell\",\"subscriberNo\":\"501234567\",\"amount\":1}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"azercell\",\"subscriberNo\":\"501234567\",\"amount\":1}"
* Post request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "IDEMPOTENCY_KEY_INVALID" beraberdir

## TC_API_PAY_009 — Uğursuz sorğunun açarı yenidən istifadə oluna bilər
tags: regression, api, grad-302, idempotency

* FP kart buraxılır "1000" ve id-ni "P" olaraq saxla
* "k2" deyişenine "${random.uuid}" deyerini ver
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${k2}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"azercell\",\"subscriberNo\":\"123\",\"amount\":5}"
* Post request and display respons
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "INVALID_SUBSCRIBER" beraberdir
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${k2}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"azercell\",\"subscriberNo\":\"501234567\",\"amount\":5}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "SUCCESS" beraberdir

## TC_API_PAY_010 — Azercell-ə Bakcell nömrəsi ilə ödəniş rədd edilir
tags: regression, api, grad-302, negative

* FP kart buraxılır "1000" ve id-ni "P" olaraq saxla
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"azercell\",\"subscriberNo\":\"551234567\",\"amount\":10}"
* Post request and display respons
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "INVALID_SUBSCRIBER" beraberdir
* Json cavabında "expected" açarı mövcud olmalıdır

## TC_API_PAY_011 — Hər təchizatçının etibarlı abunəçi formatı qəbul edilir
tags: regression, api, grad-302

* FP kart buraxılır "1000" ve id-ni "P" olaraq saxla
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"azerisiq\",\"subscriberNo\":\"1234567890\",\"amount\":1}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "SUCCESS" beraberdir
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"azersu\",\"subscriberNo\":\"12345678\",\"amount\":1}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "SUCCESS" beraberdir
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"azercell\",\"subscriberNo\":\"501234567\",\"amount\":0.50}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "SUCCESS" beraberdir
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"azercell\",\"subscriberNo\":\"511234567\",\"amount\":0.50}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "SUCCESS" beraberdir
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"azercell\",\"subscriberNo\":\"101234567\",\"amount\":0.50}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "SUCCESS" beraberdir
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"bakcell\",\"subscriberNo\":\"551234567\",\"amount\":0.50}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "SUCCESS" beraberdir
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"bakcell\",\"subscriberNo\":\"991234567\",\"amount\":0.50}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "SUCCESS" beraberdir
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"citynet\",\"subscriberNo\":\"CN123456\",\"amount\":5}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "SUCCESS" beraberdir
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"aztelekom\",\"subscriberNo\":\"1234567\",\"amount\":2}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "SUCCESS" beraberdir

## TC_API_PAY_012 — Hər təchizatçının səhv abunəçi formatı rədd edilir
tags: regression, api, grad-302, negative

* FP kart buraxılır "1000" ve id-ni "P" olaraq saxla
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"azerisiq\",\"subscriberNo\":\"123456789\",\"amount\":5}"
* Post request and display respons
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "INVALID_SUBSCRIBER" beraberdir
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"azersu\",\"subscriberNo\":\"123456789\",\"amount\":5}"
* Post request and display respons
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "INVALID_SUBSCRIBER" beraberdir
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"azercell\",\"subscriberNo\":\"701234567\",\"amount\":5}"
* Post request and display respons
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "INVALID_SUBSCRIBER" beraberdir
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"bakcell\",\"subscriberNo\":\"501234567\",\"amount\":5}"
* Post request and display respons
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "INVALID_SUBSCRIBER" beraberdir
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"citynet\",\"subscriberNo\":\"CN12345\",\"amount\":5}"
* Post request and display respons
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "INVALID_SUBSCRIBER" beraberdir
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"citynet\",\"subscriberNo\":\"cn123456\",\"amount\":5}"
* Post request and display respons
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "INVALID_SUBSCRIBER" beraberdir
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"aztelekom\",\"subscriberNo\":\"123456\",\"amount\":5}"
* Post request and display respons
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "INVALID_SUBSCRIBER" beraberdir

## TC_API_PAY_013 — Azercell məbləğ BVA: 0.49 / 0.50 / 200.00 / 200.01
tags: regression, api, grad-302, bva

* FP kart buraxılır "1000" ve id-ni "P" olaraq saxla
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"azercell\",\"subscriberNo\":\"501234567\",\"amount\":0.49}"
* Post request and display respons
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "AMOUNT_OUT_OF_RANGE" beraberdir
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"azercell\",\"subscriberNo\":\"501234567\",\"amount\":0.50}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"azercell\",\"subscriberNo\":\"501234567\",\"amount\":200.00}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"azercell\",\"subscriberNo\":\"501234567\",\"amount\":200.01}"
* Post request and display respons
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "AMOUNT_OUT_OF_RANGE" beraberdir

## TC_API_PAY_014 — CityNet komissiyası: 5 / 20 / 21 / 150 AZN
tags: regression, api, grad-302, bva

* FP kart buraxılır "1000" ve id-ni "P" olaraq saxla
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"citynet\",\"subscriberNo\":\"CN123456\",\"amount\":5}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "fee" deyeri "0.2" beraberdir
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"citynet\",\"subscriberNo\":\"CN123456\",\"amount\":20}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "fee" deyeri "0.2" beraberdir
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"citynet\",\"subscriberNo\":\"CN123456\",\"amount\":21}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "fee" deyeri "0.21" beraberdir
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"citynet\",\"subscriberNo\":\"CN123456\",\"amount\":150}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "fee" deyeri "1.5" beraberdir

## TC_API_PAY_016 — Aztelekom komissiyası sabit 0.50-dir
tags: regression, api, grad-302

* FP kart buraxılır "1000" ve id-ni "P" olaraq saxla
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"aztelekom\",\"subscriberNo\":\"1234567\",\"amount\":2}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "fee" deyeri "0.5" beraberdir
* Json cavabında "total" deyeri "2.5" beraberdir
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"aztelekom\",\"subscriberNo\":\"1234567\",\"amount\":100}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "fee" deyeri "0.5" beraberdir
* Json cavabında "total" deyeri "100.5" beraberdir

## TC_API_PAY_018 — total 300.00 keçir, 300.01 PER_TRANSACTION_LIMIT
tags: regression, api, grad-302, bva

* FP kart buraxılır "1000" ve id-ni "P" olaraq saxla
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"azerisiq\",\"subscriberNo\":\"1234567890\",\"amount\":300.00}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"azerisiq\",\"subscriberNo\":\"1234567890\",\"amount\":300.01}"
* Post request and display respons
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "PER_TRANSACTION_LIMIT" beraberdir

## TC_API_PAY_019 — Gündəlik limit dolduqda 1 AZN də rədd edilir, remaining = 0
tags: regression, api, grad-302, bva

* FP kart buraxılır "1000" ve id-ni "P" olaraq saxla
* FP ödəniş et "${P}" "azerisiq" "1234567890" "300"
* FP ödəniş et "${P}" "azerisiq" "1234567890" "200"
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"azersu\",\"subscriberNo\":\"12345678\",\"amount\":1}"
* Post request and display respons
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "DAILY_LIMIT_EXCEEDED" beraberdir
* Json cavabında "remaining" deyeri "0" beraberdir

## TC_API_PAY_020 — Gündəlik limitin qalığından çox ödəniş rədd edilir, remaining düzgün
tags: regression, api, grad-302, bva

* FP kart buraxılır "1000" ve id-ni "P" olaraq saxla
* FP ödəniş et "${P}" "azerisiq" "1234567890" "300"
* FP ödəniş et "${P}" "azerisiq" "1234567890" "150"
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"azersu\",\"subscriberNo\":\"12345678\",\"amount\":60}"
* Post request and display respons
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "DAILY_LIMIT_EXCEEDED" beraberdir
* Json cavabında "remaining" deyeri "50" beraberdir

## TC_API_PAY_021 — Balans 49.50: 49.51 rədd, 49.50 keçir və balanceAfter = 0
tags: regression, api, grad-302, bva

* FP kart buraxılır "49.50" ve id-ni "P" olaraq saxla
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"azerisiq\",\"subscriberNo\":\"1234567890\",\"amount\":49.51}"
* Post request and display respons
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "INSUFFICIENT_FUNDS" beraberdir
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"azerisiq\",\"subscriberNo\":\"1234567890\",\"amount\":49.50}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "balanceAfter" deyeri "0" beraberdir

## TC_API_PAY_022 — Balans yoxlaması total (amount + fee) üzrə aparılır
tags: regression, api, grad-302, bva

* FP kart buraxılır "50" ve id-ni "P" olaraq saxla
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"citynet\",\"subscriberNo\":\"CN123456\",\"amount\":49.6}"
* Post request and display respons
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "INSUFFICIENT_FUNDS" beraberdir

## TC_API_PAY_023 — USD kartla kommunal ödəniş rədd edilir
tags: regression, api, grad-302, negative

* FP user2 tokenini al ve user1 üçün yeni sandbox aç
* Initalize request specification
* Add Endpoint "/cards"
* Add as a header "Authorization" = "${user2Token}"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"accountId\":\"acc_003\",\"initialAmount\":10}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Save value of "id" as "u2card"
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "${user2Token}"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${u2card}\",\"billerId\":\"azercell\",\"subscriberNo\":\"501234567\",\"amount\":5}"
* Post request and display respons
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "CURRENCY_NOT_SUPPORTED" beraberdir

## TC_API_PAY_024 — Məbləğ mətn kimi ("10") rədd edilir
tags: regression, api, grad-302, negative

* FP kart buraxılır "1000" ve id-ni "P" olaraq saxla
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"azercell\",\"subscriberNo\":\"501234567\",\"amount\":\"10\"}"
* Post request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "amount" olmalıdır

## TC_API_PAY_025 — Məbləğ 0, mənfi və 3 onluqlu dəyərlər rədd edilir
tags: regression, api, grad-302, negative

* FP kart buraxılır "1000" ve id-ni "P" olaraq saxla
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"azercell\",\"subscriberNo\":\"501234567\",\"amount\":0}"
* Post request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "amount" olmalıdır
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"azercell\",\"subscriberNo\":\"501234567\",\"amount\":-5}"
* Post request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "amount" olmalıdır
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${P}\",\"billerId\":\"azercell\",\"subscriberNo\":\"501234567\",\"amount\":10.555}"
* Post request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "amount" olmalıdır

## TC_API_PAY_027 — Mövcud olmayan və ya başqasının kartı ilə ödəniş rədd edilir
tags: regression, api, grad-302, security

* FP user2 tokenini al ve user1 üçün yeni sandbox aç
* Initalize request specification
* Add Endpoint "/cards"
* Add as a header "Authorization" = "${user2Token}"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"accountId\":\"acc_003\",\"initialAmount\":10}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Save value of "id" as "u2card"
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"vcd_00000000\",\"billerId\":\"azercell\",\"subscriberNo\":\"501234567\",\"amount\":5}"
* Post request and display respons
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "CARD_NOT_FOUND" beraberdir
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"${u2card}\",\"billerId\":\"azercell\",\"subscriberNo\":\"501234567\",\"amount\":5}"
* Post request and display respons
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "CARD_NOT_FOUND" beraberdir

## TC_API_PAY_028 — Məcburi sahələr olmadıqda hər biri details-də göstərilir
tags: regression, api, grad-302, negative

* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{}"
* Post request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "cardId" olmalıdır
* Json cavabında "details.field" deyerinde "billerId" olmalıdır
* Json cavabında "details.field" deyerinde "subscriberNo" olmalıdır
* Json cavabında "details.field" deyerinde "amount" olmalıdır
