from selenium.webdriver.common.by import By


class PortalAnalistasHomeLocators:
    INP_USUARIO = (By.XPATH, "//label[text()='Usuario']/following-sibling::div/input")
    INP_CONTRASENA = (By.XPATH, "//label[text()='Contraseña']/following-sibling::div/input")
    BTN_INGRESAR = (By.ID, "btn-ingresar")
