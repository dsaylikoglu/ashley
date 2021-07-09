from selenium import webdriver

class Recom():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:/Program Files (x86)/chromedriver.exe")

    def movieRecom(self):
        self.driver.get(url="https://www.imdb.com/chart/moviemeter/")
        select = self.driver.find_element_by_xpath('//*[@id="lister-sort-by-options"]')
