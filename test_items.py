
from selenium.webdriver.common.by import By

link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

def test_found(browser):
    browser.get(link)
    assert browser.find_element(By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')

