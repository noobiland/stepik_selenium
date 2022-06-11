import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    try:
        browser = webdriver.Chrome()
        link = "https://SunInJuly.github.io/execute_script.html"
        browser.get(link)
        button = browser.find_element(By.TAG_NAME, "button")
        button.click()

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == "__main__":
    main()
