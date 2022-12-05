# -*- coding: utf-8 -*-

import allure
from allure_commons.types import AttachmentType
from pages.main_page import MainPageHelpers
from pages.filter_page import FilterPageHelpers
from pages.cart_page import CartPageHelpers
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as CHROME
from selenium.webdriver.firefox.options import Options as FIREFOX


class Application:

    # Настройка выбора браузеров
    def __init__(self, browser, base_url):
        if browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'chrome':
            self.wd = webdriver.Chrome()
        elif browser == 'chrome_headless':
            options = CHROME()
            options.headless = True
            self.wd = webdriver.Chrome(options=options)
            self.wd.set_window_size(1920, 1080)
        elif browser == 'firefox_headless':
            options = FIREFOX()
            options.headless = True
            self.wd = webdriver.Firefox(options=options)
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(10)
        self.wd.maximize_window()
        self.main_page = MainPageHelpers(self)
        self.filter_page = FilterPageHelpers(self)
        self.cart_page = CartPageHelpers(self)
        self.base_url = base_url



    # Открытие домашней страницы
    def open_home_page(self):
        wd = self.wd
        if wd.current_url is not self.base_url:
            wd.get(self.base_url)

    # Выход из браузера
    def destroy(self):
        self.wd.quit()

    # Выполнение скриншота для отчета Allure
    def get_screen(self):
        wd = self.wd
        allure.attach(wd.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
