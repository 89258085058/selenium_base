# -*- coding: utf-8 -*-
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

narrow_washing_machines = '(//*[.=" Узкие стиральные машины "])[1]'
mark_washing_machines = '(//*[.=" Candy "])[1]'
washing_machine_depth = '(//*[.=" до 40 см "])[1]'
washing_machine_candy = '//*[.=" Стиральная машина узкая Candy Smart Pro CO34 106TB1/2-07 "]'
locator_text_WM = '//*[@itemprop="name"][@class="title"]'
add_pruduct_to_cart = '(//*[@title="Добавить в корзину"])[1]'


class FilterPageHelpers:

    def __init__(self, app):
        self.app = app

    # Выбор фильтра Узкие стиральные машины
    def filterNarrowWashingMachines(self, locator=narrow_washing_machines):
        wd = self.app.wd
        element = WebDriverWait(wd, 10).until(
            EC.element_to_be_clickable((By.XPATH, ('%s' % locator))))
        element.click()
        time.sleep(2)

    # Выбор фильтра Марка стиральной машины Candy
    def filterMarkWashingMachines(self, locator=mark_washing_machines):
        wd = self.app.wd
        element = WebDriverWait(wd, 10).until(
            EC.element_to_be_clickable((By.XPATH, ('%s' % locator))))
        element.click()
        time.sleep(2)

    # Выбор фильтра глубины стиральной машины
    def filterWashingMachineDepth(self, locator=washing_machine_depth):
        wd = self.app.wd
        element = WebDriverWait(wd, 10).until(
            EC.element_to_be_clickable((By.XPATH, ('%s' % locator))))
        element.click()
        time.sleep(2)

    # Выбор необходимой стиральной машины
    def choosingWashingMachineCandy(self, locator=washing_machine_candy):
        wd = self.app.wd
        element = WebDriverWait(wd, 10).until(
            EC.element_to_be_clickable((By.XPATH, ('%s' % locator))))
        element.click()
        time.sleep(2)

    # Получение названия необходимой стиральной машины
    def getTextWM(self, locator=locator_text_WM):
        wd = self.app.wd
        element = WebDriverWait(wd, 10).until(
            EC.element_to_be_clickable((By.XPATH, ('%s' % locator))))
        return element.text()

    # Клик по кнопке добавить в корзину
    def PushAddProductButton(self, locator=add_pruduct_to_cart):
        wd = self.app.wd
        element = WebDriverWait(wd, 10).until(
            EC.element_to_be_clickable((By.XPATH, ('%s' % locator))))
        element.click()

    # Метод выбора фильтров
    def choosing_filter(self):
        self.filterNarrowWashingMachines()
        self.filterMarkWashingMachines()
        self.filterWashingMachineDepth()

    # Метод выбора товара
    def choosing_product_with_filter(self):
        self.choosingWashingMachineCandy()
        # проверка соответствия выбранного товара
        assert str(self.getTextWM()) == 'Стиральная машина узкая Candy Smart Pro CO34 106TB1/2-07'
        # добавление товара в корзину
        self.PushAddProductButton()
