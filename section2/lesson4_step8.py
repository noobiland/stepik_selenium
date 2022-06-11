import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def main():
    try:
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/explicit_wait2.html"
        browser.get(link)
        # button = WebDriverWait(browser, 5).until(
        #         EC.element_to_be_clickable((By.ID, "verify"))
        #     )
        # price = browser.find_element(By.ID, "price"

        price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

        button = browser.find_element(By.TAG_NAME, "button")
        button.click()

        x_val = browser.find_element(By.ID, "input_value").text
        name_field = browser.find_element(By.NAME, "text")
        name_field.send_keys(calc(x_val))

        button2 = browser.find_element(By.ID, "solve")
        button2.click()
    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(60)
        # закрываем браузер после всех манипуляций
        browser.quit()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


if __name__ == "__main__":
    main()
