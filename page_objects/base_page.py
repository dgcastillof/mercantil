import sys

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.TIMEOUT = 30
        self.wait = WebDriverWait(self.driver, self.TIMEOUT)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def find_select(self, *locator):
        return Select(self.find_element(*locator))

    def is_clickable(self, locator):
        return expected_conditions.element_to_be_clickable(locator)

    def is_element_present(self, locator):
        try:
            self.find_element(*locator)
            return True
        except:
            return False

    def wait_for_text(self, locator, text):
        return self.wait.until(lambda driver: self.find_element(*locator).text == text)

    def wait_for_url(self, url):
        try:
            return self.wait.until(expected_conditions.url_contains(url), "No se encontró la URL.")
        except:
            return False

    def wait_for_element_visibility(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator), "Tiempo de espera excedido.")

    def wait_for_element_to_be_clicable(self, locator):
        return self.wait.until(expected_conditions.element_to_be_clickable(locator), "Tiempo de espera excedido.")

    def wait_for_element_invisibility(self, locator):
        return self.wait.until(expected_conditions.invisibility_of_element_located(locator))