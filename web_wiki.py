from selenium import webdriver
import pyttsx3 as py

class Info():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:/Program Files (x86)/chromedriver.exe")

    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://en.wikipedia.org/wiki/Main_Page")
        search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)

        enter = self.driver.find_element_by_xpath('//*[@id="searchButton"]')
        enter.click()

        info = self.driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]')
        readable_text = info.text
        Ashley = py.init()
        Ashley.say(readable_text)
        Ashley.runAndWait()
