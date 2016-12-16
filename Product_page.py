#_*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class ProductPage(object):

    url = "http://kiev.prom.ua/p417815776-belyj-svitshot-loshadkoj.html"

    def __init__(self, driver):
        self.driver = driver

    @property
    def click_comparison_star_on_foto(self):
        return self.driver.find_element(
            By.CSS_SELECTOR,
            "#product-image-main-content .qa-comparison-star"
        )

    @property
    def click_comparison_link(self):
        return self.driver.find_element(
            By.CSS_SELECTOR,
            ".qa-main-product-block [data-qaid='comparison-link']>span>span"
        )

    @property
    def click_comparison_link_in_block(self):
        return self.driver.find_element(
            By.CSS_SELECTOR,
            ".qa-sidebar-right-block [data-qaid='comparison-link']>span>span"
        )

    @property
    def star_change_color(self):
        return self.driver.find_element(
            By.CSS_SELECTOR,
            ".b-favorites-icon__holder .icon-comparison-active"
        )

    @property
    def popup_hint(self):
        return self.driver.find_element(
            By.CSS_SELECTOR,
            "[data-qaid='popup_hint']"
        )

    @property
    def change_text(self):
        return self.driver.find_element(
            By.XPATH,
            u"//span[text()='Убрать']"
        )

    @property
    def related_products(self):
        return self.driver.find_element(
            By.CSS_SELECTOR,
            ".qa-region_related_products_bottom")

    @property
    def redirect_button(self):
        return self.driver.find_element(
            By.XPATH,
            u"//span[text()='Посмотреть']"
        )
