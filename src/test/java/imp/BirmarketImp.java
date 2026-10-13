package imp;

import com.thoughtworks.gauge.Step;
import helper.BirmarketHelper;

// Birmarket layihəsi üçün əlavə step-lər. Məntiq BirmarketHelper-dədir.
public class BirmarketImp extends BirmarketHelper {

    @Step("<element> elementlerindeki qiymetler artan sırada olmalıdır")
    public void pricesAscending(String element) {
        verifyNumbersSorted(element, true);
    }

    @Step("<element> elementlerindeki qiymetler azalan sırada olmalıdır")
    public void pricesDescending(String element) {
        verifyNumbersSorted(element, false);
    }

    @Step("<element> elementlerindeki qiymetler <min> ile <max> arasında olmalıdır")
    public void pricesBetween(String element, String min, String max) {
        verifyNumbersBetween(element, min, max);
    }

    @Step("<element> siyahısının ilk <count> elementinde <text> yazısı olmalıdır")
    public void firstItemsContain(String element, int count, String text) {
        verifyFirstItemsContainText(element, count, text);
    }

    @Step("<element> input deyeri <value> olmamalıdır")
    public void inputValueShouldNotBe(String element, String value) {
        verifyInputValueNotEquals(element, value);
    }

    @Step("<element> elementinin metni <text> olmamalıdır")
    public void textShouldNotBe(String element, String text) {
        verifyTextNotEquals(element, text);
    }

    @Step("<first> elementlerinin sayı <second> elementlerinin sayına beraber olmalıdır")
    public void countsShouldBeEqual(String first, String second) {
        verifyCountsEqual(first, second);
    }

    @Step("<first> deyişenindeki eded <second> deyişenindeki ededden böyük olmalıdır")
    public void variableShouldBeGreater(String first, String second) {
        verifyVariableGreater(first, second);
    }

    @Step("<button> elementine klik et ve <expected> görünene qeder <attempts> defe tekrarla")
    public void clickUntil(String button, String expected, int attempts) {
        clickUntilVisible(button, expected, attempts);
    }
}
