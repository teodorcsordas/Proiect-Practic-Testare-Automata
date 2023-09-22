from behave import *

from pages.base_page import BasePage


@given('I am on the signin page')
def step_impl(context):
    context.page = BasePage()
    context.page.load_signin_page()
    try:
        context.page.accept_cookie()
    except:
        pass


@when("I enter correct email")
def step_impl(context):
    context.page.fill_signin_email(context.config.userdata['email'])
    try:
        context.page.accept_cookie()
    except:
        pass


@when("I enter correct password")
def step_impl(context):
    context.page.fill_signin_password(context.config.userdata['password'])
    try:
        context.page.accept_cookie()
    except:
        pass


@when('I click on Autentificare button')
def step_impl(context):
    try:
        context.page.accept_cookie()
    except:
        pass
    context.page.click_autentificare()


@then('I should recive a successfuly signed in message')
def step_impl(context):
    context.page.confirmation_signin()


@when('I enter incorrect email')
def step_impl(context):
    context.page.fill_signin_email(context.config.userdata['incorrect_email'])


@when('I enter incorrect password')
def step_impl(context):
    context.page.fill_signin_password(context.config.userdata['incorrect_password'])


@then('I should recive an error message')
def step_impl(context):
    context.page.signin_error()


@then('I should see an error tip')
def step_impl(context):
    context.page.error_tip()
