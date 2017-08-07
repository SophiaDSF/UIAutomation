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
        sleep(5)

        elements_update  = driver.find_elements_by_id("update_title")
        elements_adv = driver.find_elements_by_id("adv_dialog")


        if len(elements_update):
            driver.find_element_by_id("com.mia.miababy:id/iv_closed_dialog").click()
        elif len(elements_adv):
            driver.find_element_by_id("com.mia.miababy:id/iv_closed_dialog").click()
        else:
            print("No update and adv info")

        #into cart
        element_cart = driver.find_element_by_android_uiautomator("new UiSelector().className(\"android.widget.LinearLayout\").childSelector(new UiSelector().className(\"android.widget.TextView\").text(\"购物车\"))")

        element_cart.click()
        cart_title = driver.find_element_by_id("com.mia.miababy:id/header_title_text").text
        self.assertEqual(cart_title, "购物车", 'Result Fail')
        print('case1: into shopping cart OK')

    def singleItemCheckout(self):
        # is cart empty ?
        is_cart_empty = driver.find_elements_by_id("com.mia.miababy:id/gohome_button")
        if len(is_cart_empty):
            print("The Shopping cart is not empty")
        else:
            print("The Shopping cart is empty")
            actions.swipToUp(driver, 0.5,1)

        print('test_case2')





