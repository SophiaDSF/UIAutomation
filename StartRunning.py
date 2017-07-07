#coding=utf-8

import unittest
import HTMLTestRunner,sys,os
from Shopping_Cart import item_checkout
from common import connect
from GlobalParams import driver

if __name__ == '__main__':

    # add cases to suit
    def suiteShoppingCart():
        suiteTest = unittest.TestSuite()
        suiteTest.addTest(item_checkout.itemCheckout('intoShoppingCart'))
        suiteTest.addTest(item_checkout.itemCheckout('singleItemCheckout'))
        return suiteTest

    # add suit to allsuit
    def allSuit():
        allTest = unittest.TestSuite(suiteShoppingCart())
        return allTest

    # path of result
    filePath = "D:\workspace_2\Result.html"
    fp = open(filePath, 'wb')

    # 生成报告的Title,描述
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='自动化测试例结果', description='购物车测试例执行结果')
    runner.run(allSuit())

    #close result file
    fp.close()

    ##disconnect device
    connect.disconnects(driver)






