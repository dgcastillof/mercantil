from page_objects.base_page import Page
from page_objects.seguros_personales.properties.locators import HogarLocators
from selenium.webdriver.common.by import By


class Hogar(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = HogarLocators()

    def click_cotizar(self):
        self.wait_for_element_to_be_clicable(self.__locators.BTN_COTIZAR).click()
        self.wait_for_element_visibility(self.__locators.TXT_MENSAJE_FORMULARIO)

    # Esto lo suelo hacer con un switch en C#. Es para poder pasar los parámetros por el feature, sino lo que tmb se puede
    # hacer es leer datos desde algún json.

    def llenar_formulario(self, filter, valor):
        if filter == "nombre":
            self.completar_nombre(valor)
        elif filter == "telefono":
            self.completar_telefono(valor)
        elif filter == "correo":
            self.completar_email(valor)
        elif filter == "tipo de vivienda":
            self.seleccionar_tipo_vivienda(valor)
        elif filter == "superficie":
            self.seleccionar_superficie(valor)
        elif filter == "ubicacion":
            self.seleccionar_ubicacion(valor)

    def completar_nombre(self, nombre):
        self.find_element(*self.__locators.INP_NAME).send_keys(nombre)

    def completar_telefono(self, telefono):
        self.find_element(*self.__locators.INP_TELEFONO).send_keys(telefono)

    def completar_email(self, email):
        self.find_element(*self.__locators.INP_EMAIL).send_keys(email)

    def seleccionar_tipo_vivienda(self, tipoVivienda):
        self.find_select(*self.__locators.DDL_TIPO_VIVIENDA).select_by_value(tipoVivienda)

    def seleccionar_superficie(self, superficie):
        self.find_select(*self.__locators.DDL_SUPERFICIE).select_by_visible_text(superficie)

    def seleccionar_ubicacion(self, ubicacion):
        self.find_select(*self.__locators.DDL_UBICACION).select_by_visible_text(ubicacion)

    def cotizar(self):
        self.find_element(*self.__locators.BTN_PEDIR_COTIZACION).click()

    def esperar_cotizacion(self):
        self.wait_for_element_visibility(self.__locators.IMG_LOADING)
        self.wait_for_element_invisibility(self.__locators.IMG_LOADING)

    def obtener_cotizaciones(self):
        self.wait_for_element_visibility(self.__locators.LBL_COTIZACION_MENSUAL)
        cotizaciones = {}
        cantidad_filas = self.find_elements(*self.__locators.TABLA_COTIZACIONES_FILAS)
        numero_fila = 1
        for fila in cantidad_filas:
            LBL_TITULO_FILA_N = (By.XPATH, "//div[@id='cotizador-result']//tbody/tr[" + str(numero_fila) + "]/td[1]")
            LBL_COTIZACION_FILA_N = (By.XPATH, "//div[@id='cotizador-result']//tbody/tr[" + str(numero_fila) + "]/td[2]")
            titulo_fila_n = self.find_element(*LBL_TITULO_FILA_N).text
            valor_fila_n = self.find_element(*LBL_COTIZACION_FILA_N).text
            cotizaciones[titulo_fila_n] = valor_fila_n
            numero_fila += 1

    #No esto seguro si a esto se refieren con guardar las cotizaciones. Las guardé en un diccionario, pero no validé nada.
    #La validación de que cada elemento tenga ese texto en su tu title no la entendí porque vi que casi no aparece ese title en
    #el DOM, y en los elementos de la grilla no está.

    def visualizo_chat_online(self):
        try:
            self.find_element(*self.__locators.IMG_CHAT_ONLINE)
            visualizo_chat = True
        except:
            visualizo_chat = False
        return visualizo_chat

    #Esto no funciona. Imagino que ese tipo de elementos tipo bots se manipulan de forma diferente, me queda pendiente.

    def verificar_costo_positivo_entero(self):
        costo_mensual_texto = self.find_element(*self.__locators.TXT_COSTO_MENSUAL).text
        costo_validado = False
        try:
            costo = int(costo_mensual_texto.split(" ")[1])
            if (costo >= 0):
                costo_validado = True
        except:
            costo_validado = False

        return costo_validado