from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    checkout_button = "//button[@id='checkout']"

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Click Checkout button")

    def confirm_product(self):
        self.get_current_url()
        self.click_checkout_button()
