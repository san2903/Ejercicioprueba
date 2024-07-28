from selenium import webdriver


def before_all(context):
    context.driver = webdriver.Chrome(
        executable_path='C:/Users/usuario/Documents/develop/chromedriver-win64/chromedriver.exe')


def after_all(context):
    context.browser.driver.quit()


def after_scenario(context, scenario):
    if 'testrail' in context.config.userdata:
        pass
