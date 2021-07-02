from behave.model import Scenario

from selenium.webdriver.chrome.options import Options
from selenium import webdriver


from config.parameters import Parameters
from page_objects import home


def before_all(context):
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(options=options)
    Scenario.continue_after_failed_step = False
    # Parámetros
    Parameters.execute_file(context.config.userdata['test'])
    context.ambiente = Parameters.get_ambiente()
    # Pages
    context.page = home.Home(context.driver)


def after_all(context):
    context.driver.quit()