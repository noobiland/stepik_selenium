import math
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('lesson_id', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, lesson_id):
    link = f"https://stepik.org/lesson/{lesson_id}/step/1"
    browser.get(link)
    input_field = WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, "ember-text-area")))
    answer = math.log(int(time.time()))
    input_field.send_keys(answer)
    button = browser.find_element(By.CLASS_NAME, "submit-submission")
    button.click()
    output = WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint")))

    assert output.text == "Correct!"
