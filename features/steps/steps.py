from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


@given('I navigate to the kayak main page')
def step_impl(context):
    context.driver.get('https://www.kayak.com')


@then('I should be in the "home" page')
def step_impl(context):
    assert "KAYAK" in context.driver.title


@then('The page "should" contain the next elements')
def step_impl(context):

    elements = {
        "name_tag": "input",
        "name_dropdown_column": "input",
        "search_tag": "input",
        "cancel": "button",
        "create_column_disabled": "button"
    }

    for row in context.table:
        try:
            element = context.driver.find_element(By.NAME, row['name'])
            assert element.tag_name == row['type']
        except NoSuchElementException:
            assert False, f"Element with name '{row['name']}' not found."


@then('The url page should be equal to the next "{url}" url')
def step_impl(context, url):
    assert context.driver.current_url == url


@when('I navigate to the "{url}" URL')
def step_impl(context, url):
    context.driver.get(url)
