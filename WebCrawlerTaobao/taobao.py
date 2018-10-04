#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 22:22:35 2018

@author: pengchengliu
"""
# resource
# http://www.junlz.com/?p=927

import os, re
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver

browserPath = '/opt/phantomjs-2.1.1-linux-x86_64/bin/phantomjs'
homepage = 'https://mm.taobao.com/search_tstar_model.htm?'
outputDir = 'photo/'
parser = 'html5lib'


##########
def main():
    # mimic a browser to read the source code
    # workflow: init driver, driver visits page, parse page, find specific info
    
    # init driver
    # init a PhantomJS, which is a browser
    # selenium supports: chrome, FireFox etc.
    driver = webdriver.PhantomJS(executable_path = browserPath)
    
    # driver visits page
    driver.get(homepage)
    
    # parse HTML, use BeautifulSoup(driver.page_source, parser) 
    # this is Right Click - Inspect per se
    # driver.page_source is the entire source code on the page
    bsObj = BeautifulSoup(driver.page_source, parser)
    
    # find specific info
    girlsList = driver.find_element_by_id('J_GirlsList').text.split('\n')
    
    # parse the home page url of girls
    # girls home page url template: //xxxx.htm?xxxuserid=xxxx
    girlsUrl = bsObj.find_all(
            "a", 
            {"href": re.compile("\/\/.*\.htm\?(userId=)\d*")})
    
    # find girls' img
    # img url template: //gtd.alicdn.com/sns_logo/xx/xxxxxx.jpg
    img_re_str = '\/\/gtd\.alicdn\.com\/sns_logo.*\.jpg'
    imagesUrl = re.findall(img_re_str, driver.page_source)
    
    # girls' name and location
    girlsNL = girlsList[::3]
    # girls' height and weight
    girlsHW = girlsList[1::3]
    # girls' home page url
    girlsHURL = [('http:' + i['href']) for i in girlsUrl]
    # girls' cover image url
    girlsPhotoUrl = [('https:' + i) for i in imagesUrl]
    # combine
    girlsInfo = zip(girlsNL, girlsHW, girlsHURL, girlsPhotoUrl)

    # now get and store following info:
    # cover image
    # images in homepage
    assembly(driver, outputDir, girlsInfo)


def assembly(driver, outputDir, girlsInfo):
    for girlNL, girlHW, girlHURL, girlCover in girlsInfo:
        print("[*]Girl: ", girlNL, girlHW)
        # create folder for the girl
        mkdir(outputDir + girlNL)
        print("   [*]Saving...")
        # get the cover img
        get_cover_img(outputDir, girlCover, girlNL)
        # get images in the home page
        getImgs(girlHURL, outputDir + girlNL)
    driver.close()

# create path and folder
def mkdir(path):
    isExists = os.path.exists(path)
    if not isExists:
        print("    [*] new folder created", path)
        os.mkdirs(path)
    else:
        print("    [+]folder", path, "already created")
        
### get images in homepage
def getImgs(url, path):
    # Part 1: get the web content
    # init the browser/driver
    driver = webdriver.PhantomJS(executable_path=browserPath)
    driver.get(url)
    print("    [*]Opening...")
    # parse the web
    bsObj = BeautifulSoup(driver.page_source, parser)
    
    # Part 2: get imgs from web content
    # find_all on bsObj
    imgs = bsObj.find_all("img", {"src": re.compile(".*\.jpg")})
    # TODO: check imgs, seems to be a dict
    for i, img in enumerate(imgs[1:]):
        try:
            html = urlopen('https:' + img['src'])
            data = html.read()
            fileName = "{}/{}.jpg".format(path, i+1)
            print("    [+]Loading...", fileName)
            with open(fileName, 'wb') as f:
                f.write(data)
        # catch any kind of exceptions
        except Exception:
            print("    [!]Address Error!")
    driver.close()
    
# get girl's cover image
def get_cover_img(outputDir, girlCover, girlNL):
    data = urlopen(girlCover).read()
    with open(outputDir + girlNL + '/cover.jpg', 'wb') as f:
        f.write(data)
    print("    [+]Loading Cover...")






























