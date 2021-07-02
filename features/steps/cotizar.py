from behave import *

from page_objects import home


@given("el usuario se encuentra en el home")
def step_impl(context):
    context.driver.get(context.ambiente['url'])
    context.page = home.Home(context.driver)
    context.page.verificar_tipo_cliente_abierto()


@when("ingresa a la sección: {tipoCliente} - {submenu}")
def step_impl(context, tipoCliente, submenu):
    context.page.seleccionar_tipo_cliente(tipoCliente)
    context.page.seleccionar_submenu(submenu)


@when("ingresa al seguro de {tipoSeguro}")
def step_impl(context, tipoSeguro):
    context.page = context.page.seleccionar_tipo_seguro(tipoSeguro)


@when("realiza una cotización con la siguiente información")
def step_impl(context):
    context.page.click_cotizar()
    i = 0
    for row in context.table:
        filter = context.table[i][0]
        value = context.table[i][1]
        context.page.llenar_formulario(filter, value)
        i += 1

    context.page.cotizar()
    context.page.esperar_cotizacion()


@then("obtengo las cotizaciones")
def step_impl(context):
    context.page.obtener_cotizaciones()


@then("se visualiza el chat online")
def step_impl(context):
    assert context.page.visualizo_chat_online()


@then("el valor mensual es positivo y entero")
def step_impl(context):
    assert context.page.verificar_costo_positivo_entero()