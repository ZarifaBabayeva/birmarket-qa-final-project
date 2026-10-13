# Bitirmə Layihəsi — UI və API Test Avtomatlaşdırması

Bu repo iki hissədən ibarətdir:

| Hissə | Test obyekti | Nə var |
|---|---|---|
| **UI** | https://birmarket.az (Production, public) | Test sənədləri + 43 avtomat regression testi (Gauge + Selenium) |
| **API** | https://api.anarabbas.com — Final Project backlog (3 epic, 10 task) | Test sənədləri + CallMan collection + 123 avtomat regression testi (Gauge + RestAssured) |

Avtomatlaşdırma kurs tərəfindən verilmiş **Gauge** arxitekturası üzərində qurulub. Arxitekturanın mövcud fayllarında heç bir dəyişiklik edilməyib, yalnız onun qaydalarına uyğun yeni fayllar əlavə olunub. Yeganə konfiqurasiya dəyişikliyi: `env/default/app.properties` faylında `ui_base_url = https://birmarket.az` (test olunan saytın ünvanı).

RestAssured + JUnit 5 + Allure API layihəsi ayrıca repodadır: https://github.com/ZarifaBabayeva/final-project-api-restassured

---

## Nəticə

| Hissə | Run | Ssenari | Nəticə |
|---|---|---|---|
| UI | Smoke (`-Dtags=smoke`) | 15 | 15/15 PASS |
| UI | Full regression | 43 | 43/43 PASS (ardıcıl 3 run, ~11 dəq) |
| API | Smoke (`-Dtags=smoke`) | 10 | 10/10 PASS (~40 san) |
| API | Full regression | 123 | 123/123 PASS (~3–4 dəq) |
| API | Manual (CallMan) | 168 TC | 168/168 PASS (3 zaman-asılı test ayrıca icra olunub) |
| API | RestAssured + JUnit 5 | 166 test | 166/166 PASS (Allure report: `docs/API_Allure_Report.html`) |

---

## Tələblər

| Alət | Versiya |
|---|---|
| Java | 25 |
| Maven | 3.9+ |
| Gauge | 1.6+ (java plugin ilə: `gauge install java`) |
| Google Chrome | son stabil versiya (yalnız UI üçün) |

---

## İşə salma

Repo-nu klonladıqdan sonra proyektin əsas qovluğunda:

```bash
# ---------- UI ----------
# Bütün UI regression testləri (43 ssenari)
mvn test "-Dgauge.specs.dir=specs/ui-testing/birmarket"

# Yalnız UI smoke testlər (15 ssenari)
mvn test "-Dgauge.specs.dir=specs/ui-testing/birmarket" "-Dtags=smoke"

# Tək bir modul, məsələn axtarış
mvn test "-Dgauge.specs.dir=specs/ui-testing/birmarket/04_search.spec"

# ---------- API ----------
# Bütün API regression testləri (123 ssenari)
mvn test "-Dgauge.specs.dir=specs/api-testing/final-project"

# Yalnız API smoke testlər (10 ssenari)
mvn test "-Dgauge.specs.dir=specs/api-testing/final-project" "-Dtags=smoke"

# Tək bir task, məsələn kommunal ödənişlər (GRAD-302)
mvn test "-Dgauge.specs.dir=specs/api-testing/final-project/fp_10_bill_payments.spec"
```

HTML hesabat: `reports/html-report/index.html`. Faylı brauzerdə birbaşa açın, IDE-nin daxili serveri ilə yox.

- UI run zamanı Chrome pəncərələrinə klik etməyin. Terminaldakı `Unable to find CDP implementation` xəbərdarlığı Chrome versiyası ilə bağlıdır və testlərə təsir etmir.
- API ödəniş və tarixçə spec-lərini **Bakı vaxtı 23:30–00:30 arasında işlətməyin**: kartın gündəlik xərci (`spentToday`) gecə yarısı sıfırlanır.
- PowerShell terminalında Azərbaycan hərfləri `?` kimi görünə bilər — bu, yalnız konsolun kodlaşdırmasıdır; testlər və HTML hesabat düzgün işləyir.

---

## Əlavə olunan fayllar

```
specs/ui-testing/birmarket/
├── birmarket.cpt              # Ortaq addımlar (concept-lər)
├── 01_home_header.spec        # Ana səhifə və header        (2)
├── 02_language.spec           # AZ / RU dil dəyişimi         (3)
├── 03_city.spec               # Şəhər seçimi                 (3)
├── 04_search.spec             # Axtarış                      (6)
├── 05_category_plp.spec       # Kateqoriya, sort, filtr      (14)
├── 06_pdp.spec                # Məhsul səhifəsi, kredit      (4)
├── 07_cart.spec               # Boş səbət                    (1)
├── 08_favorites.spec          # Seçilmişlər (guest)          (3)
├── 09_auth.spec               # Giriş — OTP-yə qədər         (4)
└── 10_account_access.spec     # Kabinet girişi, data-driven  (1 × 3 URL)

specs/api-testing/final-project/
├── fp.cpt                            # Login (user1/user2), alıcı/kart/ödəniş concept-ləri
├── fp_01_auth_security.spec          # 401 qaydaları, sandbox izolyasiyası, PAN/CVV  (7)
├── fp_02_beneficiaries_create.spec   # GRAD-101 POST /beneficiaries              (24)
├── fp_03_beneficiaries_list.spec     # GRAD-102 GET /beneficiaries               (9)
├── fp_04_beneficiaries_delete.spec   # GRAD-103 DELETE /beneficiaries/{id}       (4)
├── fp_05_cards_create.spec           # GRAD-201 POST /cards                      (17)
├── fp_06_card_get.spec               # GRAD-202 GET /cards/{id}                  (3)
├── fp_07_card_block.spec             # GRAD-203 block — state transition         (12)
├── fp_08_card_unblock.spec           # GRAD-204 unblock                          (5)
├── fp_09_billers.spec                # GRAD-301 GET /billers                     (6)
├── fp_10_bill_payments.spec          # GRAD-302 POST /bill-payments              (25)
└── fp_11_payment_history.spec        # GRAD-303 GET /bill-payments               (11)

src/test/resources/
├── locator/birmarket-*.json       # UI: 7 locator faylı
├── body/fp-login-user1.json       # API: login body-ləri
├── body/fp-login-user2.json
└── schema/fp-*.json               # API: 6 JSON Schema (contract testləri)

src/test/java/
├── helper/BirmarketHelper.java        # UI məntiqi: qiymət sıralaması, aralıq, rəqəm müqayisəsi
├── helper/FinalProjectApiHelper.java  # API: boş body, kart expiry, alıcı body-si
├── imp/BirmarketImp.java              # UI step-ləri
└── imp/FinalProjectApiImp.java        # API step-ləri

docs/
├── Birmarket_Test_Documentation.xlsx  # UI + API test sənədləri (test plan, TC, traceability, bug report)
├── API_Allure_Report.html             # RestAssured Allure report (tək fayl, brauzerdə açılır)
└── Callman/                           # CallMan collection (assertion-larla) + environment (export)
```

Arxitektura qaydası qorunub: **spec → imp (step) → helper (məntiq) → locator JSON / body / schema**.

---

## Dizayn qərarları — UI

**Guest scope.** Login yalnız telefon + SMS OTP (BirID) ilə mümkündür. Production-da OTP bypass yoxdur, ona görə avtomatlaşdırma guest vəziyyətində aparılır. Login tələb edən ssenarilər manual test olunur.

**Hər test təmiz sessiya ilə başlayır.** `Birmarket <url> sehifesini aç` concept-i cookie və storage-i təmizləyir, pəncərə ölçüsünü 1920×1080 edir. Beləliklə bir testin vəziyyəti digərinə keçmir.

**Şəhər və bildiriş pəncərələri.** Təmiz sessiyada sayt "Şəhərinizi seçin" pəncərəsini avtomatik açır; bəzən brauzer bildirişi sorğusu da çıxır. Hər ikisi `Şeher penceresi açılarsa bağla` concept-i ilə idarə olunur: pəncərə çıxsa bağlanır, çıxmasa test davam edir.

**Hardcode data yoxdur.** Production-da qiymət, stok və sıralama daim dəyişir. Ona görə testlər sabit dəyər yox, invariant yoxlayır:
- qiymətlər artan/azalan sıradadır;
- bütün qiymətlər 100–200 ₼ aralığındadır;
- kartdakı ad və qiymət PDP ilə eynidir;
- "iphone" və "IPHONE" eyni sayda nəticə qaytarır.

**Data-driven test.** Kabinet səhifələrinin girişi (`/account`, `/account/orders`, `/account/id-card`) bir ssenari və Gauge data cədvəli ilə yoxlanılır.

**Səbətə əlavə edilən ssenarilər manual regression-dadır.** Bu ssenarilər avtomatlaşdırılıb və keçib, lakin ardıcıl run-larda production-da qonaq səbətinə əlavə qeyri-deterministik nəticə verdi (flaky). Flaky test qəbul olunmadığı üçün onlar əsaslandırılaraq manual regression-a keçirilib. Boş səbət testi avtomatda qalır.

---

## Dizayn qərarları — API

**Hər ssenari öz sandbox-unda.** Backlog-a görə hər login yeni, boş mühit açır. Spec-in kontekst addımı hər ssenaridən əvvəl yeni login edir, ssenari lazım olan datanı (alıcı, kart, ödəniş) özü yaradır. Nəticədə testlər bir-birindən asılı deyil, istənilən ardıcıllıqla və təkrar-təkrar eyni nəticəni verir; 10 alıcı / 3 kart limitləri və `receiptNo` ardıcıllığı deterministikdir.

**Assert-lər mətnə yox, `code`-a yazılır** (backlog qaydası). Hər testdə status kodu + cavabın məzmunu yoxlanılır; 6 endpoint üçün JSON Schema ilə contract yoxlaması var.

**İki istifadəçi.** IDOR testləri (başqasının resursu → 404) üçün user2 token-i ayrıca dəyişəndə saxlanılır.

**Idempotency.** `Idempotency-Key` hər sorğuda `${random.uuid}` ilə unikal yaranır; replay testlərində sabit açar dəyişəndə saxlanılır və balansın bir dəfə azaldığı ayrıca yoxlanılır.

**Manual qalan testlər.** P3/P4 testlər və zamandan asılı 3 test (24 saatlıq token, rate limit, gecə yarısı sıfırlanma) CallMan collection-unda icra olunur — avtomat regression-da flaky olmasın deyə.

**Mühit qeydi.** 08.10.2026-da bir run zamanı server bir neçə dəqiqə ərzində etibarlı sorğulara `500 "Network connection lost"` qaytardı (BUG_API_004). Framework-də 500 üçün retry açılmadı ki, real problem gizlənməsin; təkrar run 123/123 keçdi.

---

## Test sənədləri

`docs/Birmarket_Test_Documentation.xlsx`:

**UI:** Test Scope, 29 ssenari, 228 test case, Automation Strategy, RTM, Summary, Grooming Questions, Assumptions & Risks, Actual Result və icra statusu.

**API:** Test Plan, 11 ssenari, 168 test case (pozitiv, neqativ, BVA, state transition, schema, auth), Coverage matrisi, Traceability (69 AC — hamısı əhatə olunub), Grooming Questions.

**Bug Reports:** UI — 3 bug, API — 4 bug.

---

## Saxlanma qeydləri

- **UI locator dəyişərsə:** yalnız `src/test/resources/locator/birmarket-*.json` faylında dəyər yenilənir, spec-lərə toxunmaq lazım deyil.
- **Kateqoriya URL-i dəyişərsə:** `birmarket.cpt` faylında bir sətir dəyişdirilir.
- **API cavab strukturu dəyişərsə:** əvvəlcə `src/test/resources/schema/fp-*.json` yenilənir — contract testləri dəyişikliyi ilk tutacaq.
- **API ünvanı dəyişərsə:** `fp.cpt` faylında `Set base Url to` sətri dəyişdirilir.
