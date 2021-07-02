from behave import *

from page_objects.portal_analistas import portal_analistas_home


@given("el usuario se encuentra en la pagina principal")
def step_impl(context):
    context.driver.get(context.ambiente['url'])
    context.page = portal_analistas_home.PortalAnalistasHome(context.driver)


@given("inicia sesión con el usuario {nombreUsuario}")
def step_impl(context, nombreUsuario):
    context.page.completar_usuario_contrasena(nombreUsuario)
    context.page.iniciar_sesion()
