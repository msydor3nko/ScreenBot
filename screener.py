import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


DIR_PATH = os.getcwd()
WEB_DRIVER_PATH = os.getcwd() + '/chromedriver' # ChromeDriver 83.0.4103.39 (mac64) using
CONFIG_WIDTH = 1920


def run_screener(url):
    # webdriver settings
    options = webdriver.ChromeOptions()
    options.headless = True

    # webdriver activation
    driver = webdriver.Chrome(WEB_DRIVER_PATH)

    # following by URL
    driver.get(url)
    
    # web page manipulations, getting screenshot and saving it to 'static' directory
    WEB_PAGE = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)
    driver.set_window_size(CONFIG_WIDTH, WEB_PAGE('Height'))
    driver.find_element_by_tag_name('body').screenshot(f"{DIR_PATH}/static/screenshot_.png")
    
    # stop webdriver
    print('Web page screened!')
    driver.quit()
