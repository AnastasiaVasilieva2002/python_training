from selenium import webdriver

from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.vars = {}
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)


    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost:81/addressbook/")

    def destroy(self):
        self.wd.quit()







