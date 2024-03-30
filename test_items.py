import time

from selenium.webdriver.common.by import By


link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_found(browser):
    browser.get(link)
    time.sleep(10)
    result = browser.find_elements(By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    assert len(result) > 0, 'button not found'
