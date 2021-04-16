from pprint import pprint
from selenium import webdriver
fireFoxOptions=webdriver.FirefoxOptions()
fireFoxOptions.set_headless()
browser=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver",firefox_options=fireFoxOptions)
browser.get("https://udb.moe.edu.tw")
pprint(browser.page_source)
browser.close()
