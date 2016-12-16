#_*- coding: utf-8 -*-
import unittest
import datetime
import pytest
from selenium import webdriver
from Favorite_page import FavoritePage
from Product_page import ProductPage
from nose_parameterized import parameterized


class TestFavoritesProduct(unittest.TestCase):

    # @pytest.mark.parametrize('param_name', ['click_on_link', 'click_on_star', 'click_on_link_in_block'])
    @parameterized.expand(['click_comparison_link_in_block'])
    def test_add_to_favotites_from_product_cart(self, param_name):
        driver = webdriver.Chrome()
        driver.maximize_window()
        product = ProductPage(driver)
        favorite = FavoritePage(driver)
        try:
            driver.get(product.url)
            if param_name == 'click_comparison_link_in_block':
                driver.execute_script("return arguments[0].scrollIntoView();", product.related_products)
            product.__getattribute__(param_name).click()
            assert product.popup_hint
            assert product.star_change_color
            assert product.change_text
            product.redirect_button.click()
            assert favorite.element_in_list
        except Exception as error:
            driver.save_screenshot('screenshots/%s' % (datetime.datetime.now()))
            print driver.current_url
            print "ERROR in test %s %s!" % (param_name, error)
            # assert False
        driver.close()
