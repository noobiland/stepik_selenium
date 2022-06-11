import time

from selenium import webdriver


def main():
    try:
        browser = webdriver.Chrome()
        browser.execute_script("document.title='Script executing';alert('Robots at work');")

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == "__main__":
    main()
