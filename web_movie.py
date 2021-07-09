from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Movie():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:/Program Files (x86)/chromedriver.exe")

    def movie_review(self, name):
        self.driver.get(url="https://www.google.com/")
        search = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input')
        search.click()
        search.send_keys(name + " movie reviews")
        search.send_keys(Keys.ENTER)
