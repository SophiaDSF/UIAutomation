#coding=utf-8
from appium import webdriver
from appium.webdriver import WebElement
from selenium import webdriver
from time import ctime,sleep

def getSize(driver):
    x = driver.get_window_size()
    width = x[0]
    height = x[1]
    return (width,height)

def swipToUp(driver,during,num):
    size = getSize(driver)
    for i in range(1,num):
        driver.swipe(size[0]/2,size[1]*3/4,size[0]/2,size[1]/4,during)
        sleep(1)

def swipToDown(driver,during,num):
    size = getSize(driver)
    for i in range(1,num):
        driver.swipe(size[0]/2,size[1]/4,size[0]/2,size[1]*3/4,during)
        sleep(1)

def swipToLeft(driver,during,num):
    size = getSize(driver)
    for i in range(1,num):
        driver.swipe(size[0]*3/4,size[1]/2,size[0]/4,size[1]/2,during)
        sleep(1)

def swipToRight(driver,during,num):
    size = getSize(driver)
    for i in range(1,num):
        driver.swipe(size[0]/4,size[1]/2,size[0]*3/4,size[1]/2,during)
        sleep(1)