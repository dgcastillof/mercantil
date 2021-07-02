from selenium.webdriver.common.by import By


class HogarLocators:
    BTN_COTIZAR = (By.XPATH, "//a[@href='#form-seguros']")
    BTN_PEDIR_COTIZACION = (By.ID, "cotizador-submit")
    TXT_MENSAJE_FORMULARIO = (By.XPATH, "//h4[contains(text(), 'Dejanos tus datos')]")
    INP_NAME = (By.ID, "inputName")
    INP_TELEFONO = (By.ID, "inputTel")
    INP_EMAIL = (By.ID, "inputemail")
    DDL_TIPO_VIVIENDA = (By.ID, "tipovivienda")
    DDL_SUPERFICIE = (By.ID, "superficie")
    DDL_UBICACION = (By.ID, "ubicacion")
    IMG_LOADING = (By.XPATH, "//img[@class='loader-image']")
    TABLA_COTIZACIONES_FILAS = (By.XPATH, "//div[@id='cotizador-result']//tbody/tr")
    IMG_CHAT_ONLINE = (By.XPATH, "//button[@aria-label='Abrir chat']")
    TXT_COSTO_MENSUAL = (By.XPATH, "//h3[text()='Costo mensual:']/../following-sibling::td/h3")
    LBL_COTIZACION_MENSUAL = (By.XPATH, "//h3[text()='Costo mensual:']")