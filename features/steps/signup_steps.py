import time

from behave import *

from pages.base_page import BasePage


@given('I am on signup page')
def step_impl(context):
    context.page = BasePage()
    context.page.load_signup_page()
    try:
        context.page.accept_cookie()
    except:
        pass


@when('I enter sign up data with existing email')
def step_impl(context):
    context.page.fill_prenume(context.config.userdata['prenume'])
    context.page.fill_nume(context.config.userdata['nume'])
    context.page.fill_telefon(context.config.userdata['telefon'])
    context.page.fill_new_email(context.config.userdata['email'])
    context.page.fill_new_password(context.config.userdata['parola_noua'])
    context.page.confirm_password(context.config.userdata['parola_noua'])


@when('I enter sign up data without prenume')
def step_impl(context):
    context.page.fill_nume(context.config.userdata['nume'])
    try:
        context.page.accept_cookie()
    except:
        pass
    context.page.fill_telefon(context.config.userdata['telefon'])
    context.page.fill_new_email(context.config.userdata['email'])
    context.page.fill_new_password(context.config.userdata['parola_noua'])
    context.page.confirm_password(context.config.userdata['parola_noua'])


@when('I enter sign up data without nume')
def step_impl(context):
    context.page.fill_prenume(context.config.userdata['prenume'])
    context.page.fill_telefon(context.config.userdata['telefon'])
    context.page.fill_new_email(context.config.userdata['email'])
    context.page.fill_new_password(context.config.userdata['parola_noua'])
    context.page.confirm_password(context.config.userdata['parola_noua'])


@when('I enter sign up data without telefon')
def step_impl(context):
    context.page.fill_prenume(context.config.userdata['prenume'])
    context.page.fill_nume(context.config.userdata['nume'])
    context.page.fill_new_email(context.config.userdata['email'])
    context.page.fill_new_password(context.config.userdata['parola_noua'])
    context.page.confirm_password(context.config.userdata['parola_noua'])


@when('I enter sign up data without email')
def step_impl(context):
    context.page.fill_prenume(context.config.userdata['prenume'])
    context.page.fill_nume(context.config.userdata['nume'])
    context.page.fill_telefon(context.config.userdata['telefon'])
    context.page.fill_new_password(context.config.userdata['parola_noua'])
    context.page.confirm_password(context.config.userdata['parola_noua'])


@when('I enter sign up data without password')
def step_impl(context):
    context.page.fill_prenume(context.config.userdata['prenume'])
    context.page.fill_nume(context.config.userdata['nume'])
    context.page.fill_telefon(context.config.userdata['telefon'])
    context.page.confirm_password(context.config.userdata['parola_noua'])


@when('I enter sign up data without password confirmation')
def step_impl(context):
    context.page.fill_prenume(context.config.userdata['prenume'])
    context.page.fill_nume(context.config.userdata['nume'])
    context.page.fill_telefon(context.config.userdata['telefon'])
    context.page.fill_new_password(context.config.userdata['parola_noua'])


@when('I agree the confidentiality policy')
def step_impl(context):
    context.page.agree_policy()


@when('I click on inregistrati-va button')
def step_impl(context):
    context.page.click_inregistrativa()


@then('Then I should recive an error message')
def step_impl(context):
    context.page.signup_error()


@then('I should see a red error tip')
def step_impl(context):
    context.page.signup_error_tip()


@then('I should recive an privacy policy error tip')
def step_impl(context):
    context.page.privacy_policy_error()
