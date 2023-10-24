from selenium.webdriver.common.by import By
import pytest
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_push_the_button(browser):
    browser.get(link)
    time.sleep(30)
    add_to_basket_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert add_to_basket_button, "Add to basket button is not found"