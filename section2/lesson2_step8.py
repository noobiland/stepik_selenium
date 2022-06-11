import math
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    try:
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/file_input.html"
        browser.get(link)

        name_field = browser.find_element(By.NAME, "firstname")
        name_field.send_keys("name")
        last_name_field = browser.find_element(By.NAME, "lastname")
        last_name_field.send_keys("last name")
        email_field = browser.find_element(By.NAME, "email")
        email_field.send_keys("email@email.com")

        current_dir = os.path.abspath(os.path.dirname(__file__))

        file_field = browser.find_element(By.ID, "file")
        file_field.send_keys(os.path.join(current_dir, 'resourse', 'test.txt'))

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
