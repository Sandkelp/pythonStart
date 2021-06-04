from selenium import webdriver
def open_browser():
    browser = webdriver.Chrome()
    browser.get = ("https://www.instagram.com/")
    assert 'Instagram' in browser.title

open_browser()


