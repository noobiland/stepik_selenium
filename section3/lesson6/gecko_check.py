import os

from selenium import webdriver
psth = os.environ["PATH"]
# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Firefox()

driver.get("https://stepik.org/lesson/25969/step/8")