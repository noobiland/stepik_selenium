import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    link = "http://suninjuly.github.io/math.html"

    try:
        browser = webdriver.Chrome()
        browser.get(link)

        x_element = browser.find_element(By.ID, "input_value")
        x = x_element.text
        result = calc(x)

        input1 = browser.find_element(By.ID, "answer")
        input1.send_keys(result)
        robot_checkbox = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
        robot_checkbox.click()
        robot_radio = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
        robot_radio.click()

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
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
