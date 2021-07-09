from selenium import webdriver

class Music():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:/Program Files (x86)/chromedriver.exe")

    def playMusic(self, track):
        self.driver.get(url=f"https://www.youtube.com/results?search_query={track}")
        video = self.driver.find_element_by_xpath('//*[@id="dismissable"]')
        video.click()
