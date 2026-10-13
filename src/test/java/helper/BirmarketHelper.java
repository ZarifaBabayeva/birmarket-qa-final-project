package helper;

import org.openqa.selenium.WebElement;
import utils.ScenarioContext;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

// Birmarket layihəsi üçün əlavə yoxlamalar: qiymət sıralaması, qiymət aralığı, rəqəm müqayisəsi.
// Bütün yoxlamalar assertEventually ilə işləyir — sort/filter-dən sonra siyahı asinxron yenilənsə belə gözləyir.
public class BirmarketHelper extends BaseHelper {

    private static final Pattern NUMBER = Pattern.compile("\\d+(?:\\.\\d+)?");

    // "179.90 ₼" → 179.90 | "1 299.00 ₼" → 1299.00 | "11.75 ₼ x 18 ay" → 11.75 | "-18 %" → 18
    protected static double parseNumber(String text) {
        String cleaned = text.replace('\u00A0', ' ').replaceAll("(?<=\\d)[ ,](?=\\d{3}(?!\\d))", "");
        Matcher m = NUMBER.matcher(cleaned);
        if (!m.find()) throw new AssertionError("Mətndə rəqəm tapılmadı: \"" + text + "\"");
        return Double.parseDouble(m.group());
    }

    // Görünən və boş olmayan elementlərin rəqəmləri (gizli dublikatlar nəzərə alınmır)
    protected List<Double> collectNumbers(String elementName) {
        List<Double> result = new ArrayList<>();
        for (WebElement element : all(elementName)) {
            String text = element.getText().trim();
            if (!text.isEmpty()) result.add(parseNumber(text));
        }
        return result;
    }

    private static boolean isSorted(List<Double> values, boolean ascending) {
        if (values.size() < 2) return false;
        for (int i = 1; i < values.size(); i++) {
            int cmp = Double.compare(values.get(i - 1), values.get(i));
            if (ascending ? cmp > 0 : cmp < 0) return false;
        }
        return true;
    }

    public void verifyNumbersSorted(String elementName, boolean ascending) {
        visible(elementName);
        assertEventually(() -> isSorted(collectNumbers(elementName), ascending),
                () -> "\"" + elementName + "\" " + (ascending ? "artan" : "azalan") + " sırada deyil: " + collectNumbers(elementName));
    }

    public void verifyNumbersBetween(String elementName, String min, String max) {
        double from = parseNumber(resolve(min));
        double to = parseNumber(resolve(max));
        visible(elementName);
        assertEventually(() -> {
                    List<Double> values = collectNumbers(elementName);
                    return !values.isEmpty() && values.stream().allMatch(v -> v >= from && v <= to);
                },
                () -> "\"" + elementName + "\" dəyərləri " + from + " – " + to + " aralığında deyil: " + collectNumbers(elementName));
    }

    public void verifyFirstItemsContainText(String elementName, int count, String text) {
        String expected = resolve(text).toLowerCase(Locale.ROOT);
        visible(elementName);
        assertEventually(() -> {
                    List<WebElement> elements = all(elementName);
                    if (elements.isEmpty()) return false;
                    for (int i = 0; i < Math.min(count, elements.size()); i++) {
                        if (!elements.get(i).getText().toLowerCase(Locale.ROOT).contains(expected)) return false;
                    }
                    return true;
                },
                () -> "\"" + elementName + "\" siyahısının ilk " + count + " elementinin hamısında \"" + expected + "\" yoxdur");
    }

    public void verifyInputValueNotEquals(String elementName, String value) {
        String unexpected = resolve(value);
        present(elementName);
        assertEventually(() -> !unexpected.equals(driver().findElement(by(elementName)).getAttribute("value")),
                () -> "\"" + elementName + "\" input dəyəri \"" + unexpected + "\" olmamalı idi");
    }

    public void verifyTextNotEquals(String elementName, String value) {
        String unexpected = resolve(value);
        visible(elementName);
        assertEventually(() -> !unexpected.equals(driver().findElement(by(elementName)).getText().trim()),
                () -> "\"" + elementName + "\" mətni \"" + unexpected + "\" olmamalı idi");
    }

    public void verifyCountsEqual(String firstElement, String secondElement) {
        visible(firstElement);
        assertEventually(() -> {
                    int first = all(firstElement).size();
                    return first > 0 && first == all(secondElement).size();
                },
                () -> "\"" + firstElement + "\" sayı (" + all(firstElement).size() + ") \"" + secondElement
                        + "\" sayına (" + all(secondElement).size() + ") bərabər deyil");
    }

    public void verifyVariableGreater(String firstVariable, String secondVariable) {
        double first = parseNumber(ScenarioContext.getString(firstVariable));
        double second = parseNumber(ScenarioContext.getString(secondVariable));
        if (!(first > second)) {
            throw new AssertionError(firstVariable + " (" + first + ") " + secondVariable + " (" + second + ") dəyərindən böyük olmalı idi");
        }
    }

    // Düyməyə klik edir və gözlənilən element görünənə qədər (maks. attempts dəfə) təkrarlayır.
    // Gözlənilən element artıq görünürsə, yenidən klik edilmir (ikinci klik başqa səhifəyə apara bilər).
    public void clickUntilVisible(String buttonName, String expectedName, int attempts) {
        for (int i = 1; i <= attempts; i++) {
            if (all(expectedName).stream().anyMatch(WebElement::isDisplayed)) return;
            WebElement button = present(buttonName);
            scrollIntoView(button);
            js().executeScript("arguments[0].click();", button);
            try {
                visible(expectedName, 20);
                return;
            } catch (AssertionError e) {
                System.out.println("\"" + expectedName + "\" görünmədi, təkrar cəhd (" + i + "/" + attempts + ")");
            }
        }
        throw new AssertionError("\"" + buttonName + "\" " + attempts + " dəfə kliklənsə də \"" + expectedName + "\" görünmədi");
    }
}
