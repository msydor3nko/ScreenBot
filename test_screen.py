#coding=utf-8
# import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# WEB_DRIVER_PATH = os.getcwd() + '/chromedriver' # ChromeDriver 83.0.4103.39 (mac64) using
WEB_DRIVER_PATH = './chromedriver' # ChromeDriver 83.0.4103.39 (mac64) using
DISPLAY_WIDTH = 1920


def run_screener(url):
    # webdriver settings
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--start-maximized')
    print("Webdriver ready to work...")
    
    # init driver
    driver = webdriver.Chrome(WEB_DRIVER_PATH, chrome_options=chrome_options)
    # following by URL
    driver.get(url)
    print(f"Webdriver getted url: {url}")

    # setting window
    TOTAL_HEIGHT = driver.execute_script("return document.scrollingElement.scrollHeight")
    driver.set_window_size(DISPLAY_WIDTH, TOTAL_HEIGHT)
    print(f"Webdriver processed web page ...")

    # getting screenshot
    element = driver.find_element_by_tag_name('body')
    element_png = element.screenshot_as_png
    # saving as .png
    with open("static/screenshot.png", "wb") as file:
        file.write(element_png)
    print("The web page screenshot saved in 'static' dir!\n")
    
    # stop webdriver
    driver.quit()
    print('Screenshot done!\n')


# test
# run_screener("https://alpha-bots.com/")







# #coding=utf-8
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# import os
# WEB_DRIVER_PATH = os.getcwd() + '/chromedriver' # ChromeDriver 83.0.4103.39 (mac64) using


# def test_fullpage_screenshot():
#     chrome_options = Options()
#     chrome_options.add_argument('--headless')
#     chrome_options.add_argument('--start-maximized')
#     driver = webdriver.Chrome(WEB_DRIVER_PATH, chrome_options=chrome_options)
#     driver.get("https://alpha-bots.com/")

#     TOTAL_HEIGHT = driver.execute_script("return document.scrollingElement.scrollHeight")
#     driver.set_window_size(1920, TOTAL_HEIGHT)

#     element = driver.find_element_by_tag_name('body')
#     element_png = element.screenshot_as_png
#     with open("test2.png", "wb") as file:
#         file.write(element_png)

#     driver.quit()


# if __name__ == "__main__":
#     test_fullpage_screenshot()
