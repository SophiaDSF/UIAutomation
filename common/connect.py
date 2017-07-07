#coding=utf-8
from appium import webdriver

def init_connet(pfName,version,dvname,package,activity):
    desired_caps = {}
    desired_caps['platformName'] = pfName
    desired_caps['platformVersion'] = version
    desired_caps['deviceName'] = dvname
    desired_caps['appPackage'] = package
    desired_caps['appActivity'] = activity
    return desired_caps

def connects(desired_caps):
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver

def disconnects(driver):
    driver.quit()