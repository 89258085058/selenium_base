# -*- coding: utf-8 -*-
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

catalog_button = '(//*[.="Каталог"])[1]'
home_appliances_button = '(//*[.="Техника для дома"])[1]'
washing_machines_button = '//*[@class="sidebar-category"][.="Стиральные машины"]'


class MainPageHelpers:

    def __init__(self, app):
        self.app = app

    def goToMainPage(self):
            wd = self.app.wd
            wd.get(self.app.base_url)

    # Клик по кнопке католог
    def PushCatologButton(self, locator=catalog_button):
        wd = self.app.wd
        element = WebDriverWait(wd, 10).until(
            EC.element_to_be_clickable((By.XPATH, ('%s' % locator))))
        element.click()

    # Клик по кнопке Техника для дома
    def PushHomeAppliancesButton(self, locator=home_appliances_button):
        wd = self.app.wd
        element = WebDriverWait(wd, 10).until(
            EC.element_to_be_clickable((By.XPATH, ('%s' % locator))))
        element.click()

    # Клик по кнопке Стиральные машины
    def PushWashingMachinesButton(self, locator=washing_machines_button):
        wd = self.app.wd
        element = WebDriverWait(wd, 10).until(
            EC.element_to_be_clickable((By.XPATH, ('%s' % locator))))
        element.click()

    # Метод перехода на страницу с выбором стиральных машин
    def goToWashingPage(self):
        self.PushCatologButton()
        time.sleep(2)
        self.PushHomeAppliancesButton()
        time.sleep(2)
        self.PushWashingMachinesButton()
        time.sleep(3)
