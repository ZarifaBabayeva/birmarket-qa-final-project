package helper;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import utils.ScenarioContext;

import java.time.LocalDate;
import java.time.ZoneId;
import java.util.LinkedHashMap;
import java.util.Map;

// Final Project (api.anarabbas.com) üçün əlavə yoxlamalar və body qurulması.
// Mövcud ApiAssertHelper-in imkanlarını genişləndirir, onu dəyişmir.
public class FinalProjectApiHelper extends ApiAssertHelper {

    private static final ObjectMapper JSON = new ObjectMapper();
    private static final ZoneId BAKU = ZoneId.of("Asia/Baku");

    // DELETE 204 kimi cavablarda body boş olmalıdır
    public void bodyShouldBeEmpty() {
        String body = response().asString();
        if (body != null && !body.isBlank()) {
            throw new AssertionError("Cavab body-si boş olmalı idi, faktiki: " + body);
        }
    }

    // Kartın expiry dəyəri "MM/YY" formatında, bu gündən (Bakı vaxtı) 3 il sonra olmalıdır
    public void expiryShouldBeThreeYearsFromToday(String path) {
        LocalDate today = LocalDate.now(BAKU);
        String expected = String.format("%02d/%02d", today.getMonthValue(), (today.getYear() + 3) % 100);
        String actual = String.valueOf(value(path));
        if (!expected.equals(actual)) {
            throw new AssertionError("\"" + path + "\" gözlənilən: \"" + expected + "\", faktiki: \"" + actual + "\"");
        }
    }

    // fpFullName, fpIban, fpCurrency, fpNickname dəyişənlərindən alıcı body-si qurur.
    // nickname "-" olarsa body-yə əlavə edilmir (opsional sahə).
    public void buildBeneficiaryBody() {
        Map<String, Object> body = new LinkedHashMap<>();
        body.put("fullName", ScenarioContext.getString("fpFullName"));
        body.put("iban", ScenarioContext.getString("fpIban"));
        body.put("currency", ScenarioContext.getString("fpCurrency"));
        String nickname = ScenarioContext.getString("fpNickname");
        if (!"-".equals(nickname)) body.put("nickname", nickname);
        try {
            ApiHelper.getInstance().addBodyAsJson(JSON.writeValueAsString(body));
        } catch (JsonProcessingException e) {
            throw new IllegalStateException("Alıcı body-si qurula bilmədi", e);
        }
    }
}
