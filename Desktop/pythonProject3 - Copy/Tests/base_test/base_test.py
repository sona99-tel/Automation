import unittest
from selenium import webdriver
class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()