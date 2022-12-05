# -*- coding: utf-8 -*-
import time

import allure
import pytest

reruns = 1


@allure.epic("М.Видео")
@allure.feature("Проверка добавления товара в корзину")
@pytest.mark.flaky(reruns=reruns)
class TestAddProductToCart:


    @allure.story("Стиральные машины")
    @allure.title("Стиральная машина узкая Candy Smart Pro CO34 106TB1/2-07")
    def test_add_candy_smart_pro(self, app):
        with allure.step("Переход на страницу с выбором стиральных машин"):
            app.main_page.goToWashingPage()
        with allure.step("Установка необходимых фильтров"):
            app.filter_page.choosing_filter()
        with allure.step("Выбор товара"):
            app.filter_page.choosing_product_with_filter()
        with allure.step("Проверка соответствия цены и товара в корзине"):
            app.cart_page.compliance_checks_product()
