# Final Project API — GRAD-101 POST /beneficiaries

Yeni alıcı əlavə etmək. Hər ssenari öz boş sandbox-unda işləyir.

Hər ssenaridən əvvəl kontekst addımı user1 üçün yeni, boş sandbox açır (yeni login) — ssenarilər bir-birindən asılı deyil və istənilən ardıcıllıqla işləyir.

* FP user1 ilə yeni sandbox aç

## TC_API_BEN_001 — Bütün sahələrlə etibarlı alıcı yaradılır (201, Location)
tags: smoke, regression, api, grad-101

* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"fullName\":\"Nigar Əliyeva\",\"iban\":\"AZ77AIIB40060019440123456789\",\"currency\":\"AZN\",\"nickname\":\"Anam\"}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyeri "^ben_[a-z0-9]{8}$" regex-ine uyğun olmalıdır
* Json cavabında "fullName" deyeri "Nigar Əliyeva" beraberdir
* Json cavabında "iban" deyeri "AZ77AIIB40060019440123456789" beraberdir
* Json cavabında "currency" deyeri "AZN" beraberdir
* Json cavabında "nickname" deyeri "Anam" beraberdir
* Json cavabında "createdAt" deyeri boş olmamalıdır
* Save value of "id" as "benId"
* Header "Location" deyerinde "/beneficiaries/${benId}" olmalıdır

## TC_API_BEN_002 — Alıcı cavabı JSON Schema-ya uyğundur
tags: regression, api, grad-101, contract

* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"fullName\":\"Rauf Məmmədov\",\"iban\":\"AZ12NABZ00000000000000000001\",\"currency\":\"USD\"}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Cavab "fp-beneficiary-schema.json" JSON schema-sına uyğun olmalıdır

## TC_API_BEN_003 — Boşluqlu və kiçik hərfli IBAN normallaşdırılır
tags: regression, api, grad-101

* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"fullName\":\"Nigar Əliyeva\",\"iban\":\"az77 aiib 4006 0019 4401 2345 6789\",\"currency\":\"AZN\"}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "iban" deyeri "AZ77AIIB40060019440123456789" beraberdir
* Json cavabında "ibanMasked" deyeri "AZ77 **** **** **** **** 6789" beraberdir

## TC_API_BEN_004 — nickname göndərilmədikdə null qaytarılır
tags: regression, api, grad-101

* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"fullName\":\"Elvin Quliyev\",\"iban\":\"AZ12NABZ00000000000000000002\",\"currency\":\"EUR\"}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "nickname" açarı mövcud olmalıdır
* Json cavabında "nickname" deyeri null olmalıdır

## TC_API_BEN_005 — Bir neçə səhv sahə details-də ayrıca göstərilir
tags: regression, api, grad-101, negative

* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"fullName\":\"A\",\"iban\":\"123\",\"currency\":\"GBP\"}"
* Post request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "fullName" olmalıdır
* Json cavabında "details.field" deyerinde "iban" olmalıdır
* Json cavabında "details.field" deyerinde "currency" olmalıdır
* Json cavabında "details" massivinin ölçüsü "3" olmalıdır

## TC_API_BEN_006 — fullName 1 simvol (min−1) rədd edilir
tags: regression, api, grad-101, bva

* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"fullName\":\"A\",\"iban\":\"AZ12NABZ00000000000000000003\",\"currency\":\"AZN\"}"
* Post request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "fullName" olmalıdır

## TC_API_BEN_007 — fullName 2 simvol (min) qəbul edilir
tags: regression, api, grad-101, bva

* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"fullName\":\"Al\",\"iban\":\"AZ12NABZ00000000000000000004\",\"currency\":\"AZN\"}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "fullName" deyeri "Al" beraberdir

## TC_API_BEN_008 — fullName 50 simvol (max) qəbul edilir
tags: regression, api, grad-101, bva

* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"fullName\":\"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\",\"iban\":\"AZ12NABZ00000000000000000005\",\"currency\":\"AZN\"}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "fullName" deyeri "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" beraberdir

## TC_API_BEN_009 — fullName 51 simvol (max+1) rədd edilir
tags: regression, api, grad-101, bva

* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"fullName\":\"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\",\"iban\":\"AZ12NABZ00000000000000000006\",\"currency\":\"AZN\"}"
* Post request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "fullName" olmalıdır

## TC_API_BEN_011 — fullName yalnız defislərdən ibarət olduqda rədd edilir
tags: regression, api, grad-101, negative

* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"fullName\":\"---\",\"iban\":\"AZ12NABZ00000000000000000008\",\"currency\":\"AZN\"}"
* Post request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "fullName" olmalıdır

## TC_API_BEN_012 — fullName rəqəm ehtiva etdikdə rədd edilir
tags: regression, api, grad-101, negative

* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"fullName\":\"Ali2\",\"iban\":\"AZ12NABZ00000000000000000009\",\"currency\":\"AZN\"}"
* Post request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "fullName" olmalıdır

## TC_API_BEN_013 — fullName-də Azərbaycan hərfləri, defis, apostrof qəbul edilir
tags: regression, api, grad-101, positive

* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"fullName\":\"Şəhla Güləliyeva-O'Neil\",\"iban\":\"AZ12NABZ00000000000000000010\",\"currency\":\"AZN\"}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "fullName" deyeri "Şəhla Güləliyeva-O'Neil" beraberdir

## TC_API_BEN_014 — IBAN 27 simvol rədd edilir
tags: regression, api, grad-101, negative

* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"fullName\":\"Test Bir\",\"iban\":\"AZ77AIIB4006001944012345678\",\"currency\":\"AZN\"}"
* Post request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "iban" olmalıdır

## TC_API_BEN_015 — IBAN 29 simvol rədd edilir
tags: regression, api, grad-101, negative

* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"fullName\":\"Test Bir\",\"iban\":\"AZ77AIIB400600194401234567890\",\"currency\":\"AZN\"}"
* Post request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "iban" olmalıdır

## TC_API_BEN_016 — Başqa ölkə prefiksli IBAN (TR) rədd edilir
tags: regression, api, grad-101, negative

* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"fullName\":\"Test Bir\",\"iban\":\"TR77AIIB40060019440123456789\",\"currency\":\"AZN\"}"
* Post request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "iban" olmalıdır

## TC_API_BEN_018 — Siyahıda olmayan valyuta (GBP) rədd edilir
tags: regression, api, grad-101, negative

* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"fullName\":\"Test Bir\",\"iban\":\"AZ12NABZ00000000000000000011\",\"currency\":\"GBP\"}"
* Post request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "currency" olmalıdır

## TC_API_BEN_021 — Məcburi iban sahəsi olmadan rədd edilir
tags: regression, api, grad-101, negative

* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"fullName\":\"Test Bir\",\"currency\":\"AZN\"}"
* Post request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "iban" olmalıdır

## TC_API_BEN_023 — Etibarsız JSON body INVALID_JSON qaytarır
tags: regression, api, grad-101, negative

* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"fullName\": \"Test\","
* Post request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "INVALID_JSON" beraberdir

## TC_API_BEN_024 — Eyni IBAN ikinci dəfə əlavə edilə bilmir
tags: regression, api, grad-101, negative

* FP alıcı yarat "Nigar Əliyeva" "AZ77AIIB40060019440123456789" "AZN" "-" ve id-ni "benA" olaraq saxla
* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"fullName\":\"Başqa Ad\",\"iban\":\"AZ77AIIB40060019440123456789\",\"currency\":\"AZN\"}"
* Post request and display respons
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "BENEFICIARY_EXISTS" beraberdir

## TC_API_BEN_025 — Eyni IBAN fərqli formatda da dublikat sayılır
tags: regression, api, grad-101, negative

* FP alıcı yarat "Nigar Əliyeva" "AZ77AIIB40060019440123456789" "AZN" "-" ve id-ni "benA" olaraq saxla
* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"fullName\":\"Başqa Ad\",\"iban\":\"az77 aiib 4006 0019 4401 2345 6789\",\"currency\":\"AZN\"}"
* Post request and display respons
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "BENEFICIARY_EXISTS" beraberdir

## TC_API_BEN_026 — Ləqəb böyük-kiçik hərf fərqi ilə təkrarlana bilmir
tags: regression, api, grad-101, negative

* FP alıcı yarat "Nigar Əliyeva" "AZ77AIIB40060019440123456789" "AZN" "Anam" ve id-ni "benA" olaraq saxla
* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"fullName\":\"Başqa Ad\",\"iban\":\"AZ12NABZ00000000000000000016\",\"currency\":\"AZN\",\"nickname\":\"ANAM\"}"
* Post request and display respons
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "NICKNAME_TAKEN" beraberdir

## TC_API_BEN_027 — İstifadəçi öz hesabının IBAN-ını əlavə edə bilmir
tags: regression, api, grad-101, negative

* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"fullName\":\"Özüm Test\",\"iban\":\"AZ29NABZ00000000137010002855\",\"currency\":\"AZN\"}"
* Post request and display respons
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "OWN_ACCOUNT" beraberdir

## TC_API_BEN_029 — 10-cu alıcı (limit) əlavə olunur
tags: regression, api, grad-101, bva

* FP alıcı yarat "Alıcı Test A" "AZ12NABZ00000000000000000101" "AZN" "-" ve id-ni "b1" olaraq saxla
* FP alıcı yarat "Alıcı Test B" "AZ12NABZ00000000000000000102" "AZN" "-" ve id-ni "b2" olaraq saxla
* FP alıcı yarat "Alıcı Test C" "AZ12NABZ00000000000000000103" "AZN" "-" ve id-ni "b3" olaraq saxla
* FP alıcı yarat "Alıcı Test D" "AZ12NABZ00000000000000000104" "AZN" "-" ve id-ni "b4" olaraq saxla
* FP alıcı yarat "Alıcı Test E" "AZ12NABZ00000000000000000105" "AZN" "-" ve id-ni "b5" olaraq saxla
* FP alıcı yarat "Alıcı Test F" "AZ12NABZ00000000000000000106" "AZN" "-" ve id-ni "b6" olaraq saxla
* FP alıcı yarat "Alıcı Test G" "AZ12NABZ00000000000000000107" "AZN" "-" ve id-ni "b7" olaraq saxla
* FP alıcı yarat "Alıcı Test H" "AZ12NABZ00000000000000000108" "AZN" "-" ve id-ni "b8" olaraq saxla
* FP alıcı yarat "Alıcı Test I" "AZ12NABZ00000000000000000109" "AZN" "-" ve id-ni "b9" olaraq saxla
* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"fullName\":\"Onuncu Alıcı\",\"iban\":\"AZ12NABZ00000000000000000210\",\"currency\":\"AZN\"}"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "10" beraberdir

## TC_API_BEN_030 — 11-ci alıcı limitə görə rədd edilir
tags: regression, api, grad-101, bva

* FP alıcı yarat "Alıcı Test A" "AZ12NABZ00000000000000000101" "AZN" "-" ve id-ni "b1" olaraq saxla
* FP alıcı yarat "Alıcı Test B" "AZ12NABZ00000000000000000102" "AZN" "-" ve id-ni "b2" olaraq saxla
* FP alıcı yarat "Alıcı Test C" "AZ12NABZ00000000000000000103" "AZN" "-" ve id-ni "b3" olaraq saxla
* FP alıcı yarat "Alıcı Test D" "AZ12NABZ00000000000000000104" "AZN" "-" ve id-ni "b4" olaraq saxla
* FP alıcı yarat "Alıcı Test E" "AZ12NABZ00000000000000000105" "AZN" "-" ve id-ni "b5" olaraq saxla
* FP alıcı yarat "Alıcı Test F" "AZ12NABZ00000000000000000106" "AZN" "-" ve id-ni "b6" olaraq saxla
* FP alıcı yarat "Alıcı Test G" "AZ12NABZ00000000000000000107" "AZN" "-" ve id-ni "b7" olaraq saxla
* FP alıcı yarat "Alıcı Test H" "AZ12NABZ00000000000000000108" "AZN" "-" ve id-ni "b8" olaraq saxla
* FP alıcı yarat "Alıcı Test I" "AZ12NABZ00000000000000000109" "AZN" "-" ve id-ni "b9" olaraq saxla
* FP alıcı yarat "Onuncu Alıcı" "AZ12NABZ00000000000000000210" "AZN" "-" ve id-ni "b10" olaraq saxla
* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{\"fullName\":\"On Birinci\",\"iban\":\"AZ12NABZ00000000000000000211\",\"currency\":\"AZN\"}"
* Post request and display respons
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "LIMIT_REACHED" beraberdir
* Json cavabında "limit" deyeri "10" beraberdir
