import pytest


@pytest.fixture
def set_up():
    print('Start test')  # до теста
    # driver = webdriver.Chrome(executable_path='C:\\resource\\chromedriver.exe')
    # url = 'https://www.saucedemo.com'
    # driver.get(url)
    # driver.maximize_window()
    yield
    print('Finish test')
    # driver.quit()


@pytest.fixture(scope="module")
def set_group():
    print('Enter system')
    yield
    print('Exit system')
