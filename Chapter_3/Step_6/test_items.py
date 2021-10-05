import pytest
from selenium import webdriver

def test_basket_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    button = browser.find_elements_by_class_name("btn-add-to-basket")
    assert button != []