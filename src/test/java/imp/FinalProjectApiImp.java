package imp;

import com.thoughtworks.gauge.Step;
import helper.FinalProjectApiHelper;

// Final Project API step-ləri. Məntiq helper/FinalProjectApiHelper-dədir.
public class FinalProjectApiImp extends FinalProjectApiHelper {

    @Step("Cavab body-si boş olmalıdır")
    public void responseBodyShouldBeEmpty() {
        bodyShouldBeEmpty();
    }

    @Step("Json cavabında <key> deyeri bu gündən 3 il sonranın ay/il dəyəri olmalıdır")
    public void expiryThreeYearsAhead(String key) {
        expiryShouldBeThreeYearsFromToday(key);
    }

    @Step("FP alıcı body-sini qur")
    public void beneficiaryBody() {
        buildBeneficiaryBody();
    }
}
