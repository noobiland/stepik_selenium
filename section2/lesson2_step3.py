import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def main():
    # link = "http://suninjuly.github.io/selects1.html"
    link = "http://suninjuly.github.io/selects2.html"

    try:
        browser = webdriver.Chrome()
        browser.get(link)

        num1 = browser.find_element(By.ID, "num1").text
        num2 = browser.find_element(By.ID, "num2").text
        x = int(num1) + int(num2)
        select = Select(browser.find_element(By.TAG_NAME, "select"))
        select.select_by_value(str(x))

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == "__main__":
    main()
