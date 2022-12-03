from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    select_product_1 = "//button[@id='add-to-cart-sauce-labs-backpack']"
    select_product_2 = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    select_product_3 = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    cart = "//a[@class='shopping_cart_link']"
    menu_button = "//button[@id='react-burger-menu-btn']"
    about_link = "//a[@id='about_sidebar_link']"

    def get_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_2)))

    def get_product_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_3)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_menu_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_button)))

    def get_about_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.about_link)))

    def click_select_product_1(self):
        self.get_product_1().click()
        print("Click product 1")

    def click_select_product_2(self):
        self.get_product_2().click()
        print("Click product 2")

    def click_select_product_3(self):
        self.get_product_3().click()
        print("Click product 3")

    def click_cart(self):
        self.get_cart().click()
        print("Click cart")

    def click_menu_button(self):
        self.get_menu_button().click()
        print("Click menu")

    def click_about_link(self):
        self.get_about_link().click()
        print("Click about link")

    def select_1_product_1(self):
        self.get_current_url()
        self.click_select_product_1()
        self.click_cart()

    def select_2_product_2(self):
        self.get_current_url()
        self.click_select_product_2()
        self.click_cart()

    def select_3_product_3(self):
        self.get_current_url()
        self.click_select_product_3()
        self.click_cart()

    def select_menu_about(self):
        self.get_current_url()
        self.click_menu_button()
        self.click_about_link()
        self.assert_url('https://saucelabs.com/')
