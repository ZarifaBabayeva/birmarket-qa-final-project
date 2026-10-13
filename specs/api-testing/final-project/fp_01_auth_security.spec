# Final Project API — Auth və ümumi qaydalar

Login, 401 qaydaları, sandbox izolyasiyası, həssas məlumatın sızmaması.

Hər ssenaridən əvvəl kontekst addımı user1 üçün yeni, boş sandbox açır (yeni login) — ssenarilər bir-birindən asılı deyil və istənilən ardıcıllıqla işləyir.

* FP user1 ilə yeni sandbox aç

## TC_API_AUTH_001 — Etibarlı login token qaytarır, şifrə cavabda yoxdur
tags: smoke, regression, api, auth

* Initalize request specification
* Add Endpoint "/auth/login"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"email\":\"user1@test.com\",\"password\":\"User1234\"}"
* Post request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "token" deyeri boş olmamalıdır
* Json cavabında "user.email" deyeri "user1@test.com" beraberdir
* Json cavabında "user.password" açarı olmamalıdır

## TC_API_AUTH_002 — Yanlış şifrə ilə login 401 qaytarır və sahəni açıqlamır
tags: regression, api, auth, negative

* Initalize request specification
* Add Endpoint "/auth/login"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"email\":\"user1@test.com\",\"password\":\"Wrong999\"}"
* Post request and display respons
* Status kodunun "401" olmalıdır
* Json cavabında "token" açarı olmamalıdır
* Json cavabında "error" deyeri "Email və ya şifrə yanlışdır" beraberdir

## TC_API_SEC_001 — Token olmadan 10 qorunan endpoint 401 qaytarır
tags: smoke, regression, api, security

* Initalize request specification
* Add Endpoint "/beneficiaries"
* Get request and display respons
* Status kodunun "401" olmalıdır
* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"fullName\":\"Test\",\"iban\":\"AZ77AIIB40060019440123456789\",\"currency\":\"AZN\"}"
* Post request and display respons
* Status kodunun "401" olmalıdır
* Initalize request specification
* Add Endpoint "/beneficiaries/ben_00000000"
* Delete request and display response
* Status kodunun "401" olmalıdır
* Initalize request specification
* Add Endpoint "/cards"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"accountId\":\"acc_002\",\"initialAmount\":10}"
* Post request and display respons
* Status kodunun "401" olmalıdır
* Initalize request specification
* Add Endpoint "/cards/vcd_00000000"
* Get request and display respons
* Status kodunun "401" olmalıdır
* Initalize request specification
* Add Endpoint "/cards/vcd_00000000/block"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"reason\":\"TEMPORARY\"}"
* Post request and display respons
* Status kodunun "401" olmalıdır
* Initalize request specification
* Add Endpoint "/cards/vcd_00000000/unblock"
* Post request and display respons
* Status kodunun "401" olmalıdır
* Initalize request specification
* Add Endpoint "/billers"
* Get request and display respons
* Status kodunun "401" olmalıdır
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "${random.uuid}"
* Add body as text "{\"cardId\":\"vcd_00000000\",\"billerId\":\"azercell\",\"subscriberNo\":\"501234567\",\"amount\":1}"
* Post request and display respons
* Status kodunun "401" olmalıdır
* Initalize request specification
* Add Endpoint "/bill-payments"
* Get request and display respons
* Status kodunun "401" olmalıdır

## TC_API_SEC_002 — Saxta token ilə sorğu 401 qaytarır
tags: regression, api, security

* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "Bearer abc.invalid.token"
* Get request and display respons
* Status kodunun "401" olmalıdır

## TC_API_SEC_003 — Bearer prefiksi olmadan token 401 qaytarır
tags: regression, api, security

* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "${rawToken}"
* Get request and display respons
* Status kodunun "401" olmalıdır

## TC_API_SEC_005 — Yeni login yeni, boş sandbox açır (data izolyasiyası)
tags: regression, api, security

* FP alıcı yarat "İzolyasiya Test" "AZ12NABZ00000000000000000900" "AZN" "-" ve id-ni "benA" olaraq saxla
* FP user1 ilə yeni sandbox aç
* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "0" beraberdir
* Json cavabında "items" massivinin ölçüsü "0" olmalıdır

## TC_API_SEC_007 — Kart cavabında tam PAN və CVV qaytarılmır
tags: regression, api, security

* Initalize request specification
* Add Endpoint "/cards"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"accountId\":\"acc_002\",\"initialAmount\":10}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "maskedPan" deyeri "^4169 73[*]{2} [*]{4} [0-9]{4}$" regex-ine uyğun olmalıdır
* Json cavabında "pan" açarı olmamalıdır
* Json cavabında "cardNumber" açarı olmamalıdır
* Json cavabında "cvv" açarı olmamalıdır
* Json cavabında "cvc" açarı olmamalıdır
