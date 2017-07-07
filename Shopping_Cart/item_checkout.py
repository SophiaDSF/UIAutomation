#coding=utf-8

from appium import webdriver
from appium.webdriver import WebElement
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import threading
from time import ctime,sleep

from GlobalParams import driver
from common import actions

class itemCheckout(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def intoShoppingCart(self):
        #wait
        element = WebDriverWait(driver, 7).until(lambda x: x.find_element_by_id("com.mia.miababy:id/update_title"))

        if element:
            driver.find_element_by_id("com.mia.miababy:id/iv_closed_dialog").click()
        else:
            print("No update info")
        #into cart
        element_cart = driver.find_element_by_xpath("//android.widget.FrameLayout/android.widget.TabWidget/android.widget.FrameLayout[4]")
        element_cart.click()
        cart_title = driver.find_element_by_id("com.mia.miababy:id/header_title_text").text
        self.assertEqual(cart_title, "购物车", 'Result Fail')
        print('case1: into shopping cart OK')

    def singleItemCheckout(self):
        # is cart empty ?
        is_cart_empty =  WebDriverWait(driver, 3).until(lambda x: x.find_element_by_id("com.mia.miababy:id/gohome_button"))
        if is_cart_empty:
            print("The Shopping cart is empty")
            actions.swipToUp(driver,0.5,1)
        else:
            print("The Shopping cart is not empty")
        print('test_case2')





