from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.cart_page import Cart_page
from pages.login_page import Login_page
from pages.main_page import Main_page


def test_buy_product_1(set_up, set_group):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # options - для очищения консоли от
    # driver = webdriver.Chrome(executable_path='C:\\resource\\chromedriver.exe', chrome_options=options)
    driver = webdriver.Chrome() # если chromeDriver в system32
    login = Login_page(driver)
    login.authorization()
    main = Main_page(driver)
    main.select_1_product_1()
    cart = Cart_page(driver)
    cart.confirm_product()
    driver.quit()


# @pytest.mark.run(order=1)
def test_buy_product_2(set_up, set_group):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # driver = webdriver.Chrome(executable_path='C:\\resource\\chromedriver.exe', chrome_options=options)
    driver = webdriver.Chrome() # если chromeDriver в system32
    login = Login_page(driver)
    login.authorization()
    main = Main_page(driver)
    main.select_2_product_2()
    cart = Cart_page(driver)
    cart.confirm_product()
    driver.quit()


# @pytest.mark.run(order=1)
def test_buy_product_3(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # driver = webdriver.Chrome(executable_path='C:\\resource\\chromedriver.exe', chrome_options=options)
    driver = webdriver.Chrome() # если chromeDriver в system32
    login = Login_page(driver)
    login.authorization()
    main = Main_page(driver)
    main.select_3_product_3()
    cart = Cart_page(driver)
    cart.confirm_product()
    driver.quit()
