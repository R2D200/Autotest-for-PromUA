#_*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class FavoritePage(object):

    url = "http://prom.ua/comparison/list"

    def __init__(self, driver):
        self.driver = driver

    @property
    def element_in_list(self):
        return self.driver.find_element(
            By.CSS_SELECTOR,
            "[data-list_type='gallery']>.b-compare-view"
        )
