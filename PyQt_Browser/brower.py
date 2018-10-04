#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 22:22:35 2018

@author: pengchengliu
"""
# resource
# https://zhuanlan.zhihu.com/p/40634325

# to download the resources in this exercise
# in commandline
# $ wget http://labfile.oss.aliyuncs.com/courses/705/icons.zip
# unzip icons.zip

###################################################
#         Develop a simple brower via PyQt        #
###################################################

# features of brower:
#   a window to display web pages
#   a navigation bar, address bar
#   tages to display mutiple pages

from PyQt5.QtCore import *
from PyQt5.Widgets import *
from PyQt5.Gui import *
from PyQt5.QtWebKitWidgets import *

import sys

###############################
#  Step1: Create the Browser  #
###############################

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # set window title
        self.setWindowTitle('My Browser')
        # set window icon
        self.setWindowIcon(QIcon('icons/penguin.png'))
        self.show()
        
        # set browser
        self.browser = QWebView()
        # set default url
        url = 'Google'
        self.browser.setUrl(QUrl(url))
        # add broswer to window
        self.setCentralWidget(self.browser)
        
        # add navigation bar
        navigation_bar = QToolBar('Navigation')
        # set icon size
        navigation_bar.setIconSize(QSize(16,16))
        self.addToolBar(naviagtion_bar)

        # add functional buttons to tool bar
        back_button = QAction(QIcon('icons/back.png'), 'back', self)
        next_button = QAction(QIcon('icons/next.png'), 'Forward', self)
        stop_button = QAction(QIcon('icons/stop.png'), 'stop', self)
        reload_button = QAction(QIcon('icons/reload.png'), 'reload', self)

        # add reactions of button clicking
        back_button.triggered.connect(self.browser.back)
        next_button.triggered.connect(self.browser.forward)
        stop_button.triggered.connect(self.browser.stop)
        reload_button.triggered.connect(self.browser.reload)

        # add buttons to navigation bar
        navigation_bar.addAction(back_button)
        navigation_bar.addAction(next_button)
        navigation_bar.addAction(stop_button)
        navigation_bar.addAction(reload_button)

        # add url bar
        self.urlbar = QLineEdit()
        navigation_bar.addSeperator()
        navigation_bar.addWidget(self.urlbar)
        
        # tabs
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)
        self.tabs.currentChanged.connect(self.current_tab_changed)
 
       # close tag
        self.tabs.setTabsClosable(True)
        # add connection to close the tab
        self.tabs.tabCloseRequested.connect(self.close_current_tab)
        # add default new tab
        self.add_new_tab(QUrl('https://Google.de'), 'Homepage')
        # add tabs as widget
        self.setCentralWidget(self.tabs)
         
        
    def renew_urlbar(self, q):
        # sync the current url to url pad
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

    def add_new_tab(self, qurl=QUrl(''), label='Blank'):
        browser = QWebView()
        browser.setUrl(qurl)
        
        # set index of tabs for the sake of managing tabs
        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)
        # TODO: why brower=brower?
        browser.urlChanged.connect(
                lambda qurl, brower=brower: self.renew_urlbar(qurl, browser))
        
        # modify tab title as tab is loaded
        browser.loadFinished.connect(lambda _, i=i, brower=brower:
            self.tabs.setTabText(i, browser.page().mainFrame().title()))
        
    def close_current_tab(self, i):
        if self.tabs.count() < 2:
            return
        self.tabs.removeTab(i)
        

# start the browser
# init the app
app = QApplication(sys.argv)
# init the browser
window = MainWindow()
# display the window
window.show()
# run the app
app.exec_()

###############################
#  Step2: Add Navigation Bar  #
###############################
# QToolBar for navigation bar
# QAction for buttons of back, next, reload, stop

###############################
#      Step3: Add URL Bar     #
###############################
# add URL bar to navigation bar as widget
# update URL bar content to the real-time url

###############################
#       Step4: Add Tabs       #
###############################
# use QTabWidget to add tab bar
# add button of 'adding tabs' 
# add functions of 'adding tabs by double clicking the tab bar'
# add functions of 'chosing the tag'

 



















