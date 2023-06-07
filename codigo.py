from a_selenium2df import get_df
import undetected_chromedriver as uc
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

def g(q="*",):
    return get_df(driver, By, WebDriverWait, expected_conditions, queryselector=q, with_methods=True, )
if __name__ == "__main__":
    driver = uc.Chrome()
    driver.get(r"https://testpages.herokuapp.com/styled/index.html")

