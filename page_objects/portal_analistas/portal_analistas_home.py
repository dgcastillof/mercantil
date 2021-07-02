from page_objects.base_page import Page
from page_objects.portal_analistas.properties.locators import PortalAnalistasHomeLocators


class PortalAnalistasHome(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = PortalAnalistasHomeLocators()

    def completar_usuario_contrasena(self, nombreUsuario):
        self.wait_for_element_visibility(self.__locators.INP_USUARIO)
        self.find_element(*self.__locators.INP_USUARIO).send_keys(nombreUsuario)
        self.find_element(*self.__locators.INP_CONTRASENA).send_keys("sinu1404")

    def iniciar_sesion(self):
        self.find_element(*self.__locators.BTN_INGRESAR).click()
