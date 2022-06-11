import math
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    try:
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/redirect_accept.html"
        browser.get(link)
        button = browser.find_element(By.TAG_NAME, "button")
        button.click()

        new_window = browser.window_handles[1]
        browser.switch_to.window(new_window)
        x_val = browser.find_element(By.ID, "input_value").text
        name_field = browser.find_element(By.NAME, "text")
        name_field.send_keys(calc(x_val))
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
