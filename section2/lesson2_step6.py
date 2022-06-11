import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    try:
        browser = webdriver.Chrome()
        link = "http://SunInJuly.github.io/execute_script.html"
        browser.get(link)
        x = browser.find_element(By.ID, "input_value").text

        browser.execute_script("window.scrollBy(0, 100);")

        input_field = browser.find_element(By.ID, "answer")
        input_field.send_keys(calc(x))

        robot_checkbox = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
        robot_checkbox.click()
        robot_radio = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
        robot_radio.click()
        button = browser.find_element(By.TAG_NAME, "button")
        button.click()

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


if __name__ == "__main__":
    main()
