from selenium.webdriver.common.by import By

from page_objects.base_page import Page
from .properties.locators import HomeLocators
from .seguros_personales import hogar


class Home(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = HomeLocators()

    def verificar_tipo_cliente_abierto(self):
        submenu_activo = self.__locators.UL_SUBMENU_ACTIVO
        if self.is_element_present(submenu_activo):
            self.cerrar_tipo_cliente(submenu_activo)

    def seleccionar_tipo_cliente(self, tipoCliente):
        LBL_TIPO_CLIENTE = (By.XPATH, "//a[text()='" + tipoCliente + "']")
        self.wait_for_element_visibility(LBL_TIPO_CLIENTE).click()

    def seleccionar_submenu(self, submenu):
        LBL_SUBMENU = (By.XPATH, "//a[text()='" + submenu + "']")
        self.wait_for_element_visibility(LBL_SUBMENU).click()

    def cerrar_tipo_cliente(self, locator):
        self.find_element(*locator).click()

    def seleccionar_tipo_seguro(self, tipoSeguro):
        IMG_TIPO_SEGURO = (By.XPATH, "//img[@alt='" + tipoSeguro + "']")
        self.wait_for_element_visibility(IMG_TIPO_SEGURO).click()
        return hogar.Hogar(self.driver)