# -*- coding: utf-8 -*-
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

cart_button = '(//*[@type="cart"])[1]'

nameWM = '//*[@class="cart-item__name ng-star-inserted"]'
priceWM = '(//*[@class="price__main-value"])[1]'


class CartPageHelpers:

    def __init__(self, app):
        self.app = app

    # Клик по кнопке корзина
    def PushCartButton(self, locator=cart_button):
        wd = self.app.wd
        element = WebDriverWait(wd, 10).until(
            EC.element_to_be_clickable((By.XPATH, ('%s' % locator))))
        element.click()
        time.sleep(2)

    # Получение наименования товара
    def getNameProduct(self, locator=nameWM):
        wd = self.app.wd
        element = WebDriverWait(wd, 10).until(
            EC.element_to_be_clickable((By.XPATH, ('%s' % locator))))
        return element.text()

    # Получение цены товара
    def getPriceProduct(self, locator=priceWM):
        wd = self.app.wd
        element = WebDriverWait(wd, 10).until(
            EC.element_to_be_clickable((By.XPATH, ('%s' % locator))))
        return element.text()

    # Метод проверки соответствия цены и товара в корзине
    def compliance_checks_product(self):
        self.PushCartButton()
        name = 'Стиральная машина узкая Candy Smart Pro CO34 106TB1/2-07'
        price = '26 499 ₽'
        print(self.getNameProduct())
        print(self.getPriceProduct())

