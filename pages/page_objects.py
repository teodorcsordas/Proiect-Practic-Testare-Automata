class PageObjects:
    # URL:
    signin_page_url = 'https://www.mobilier1.ro/auth-loginform/?return_url=index.php'
    signup_page_url = 'https://www.mobilier1.ro/inregistrare/'

    # Fields:
    email_field_XPATH = '//input[@id="login_main_login"]'
    password_field_XPATH = "//input[@id='psw_main_login']"
    account_button_XPATH = "//div[@id='th_slide_open_btn_prof_slide']//span//*[name()='svg']"
    prenume_field_XPATH = '//*[@id="elm_6"]'
    nume_field_XPATH = '//*[@id="elm_7"]'
    telefon_field_XPATH = '//*[@id="elm_9"]'
    new_email_field_XPATH = '//*[@id="email"]'
    new_password_field_XPATH = '//*[@id="password1"]'
    confirm_password_field_XPATH = '//*[@id="password2"]'
    confirm_password_field_CSS = '#password2'

    # Buttons:
    autentificare_button_XPATH = "//button[@name='dispatch[auth.login]']"
    cookie_permission_button_Xpath = "//button[@id='CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll']"
    privacy_policy_button_XPATH = '//*[@id="gdpr_agreements_user_registration"]'
    inregistrativa_button_XPATH = "//button[@name='dispatch[profiles.update]']"

    # Messages:
    confirmation_message_XPATH = ("//div[@class='cm-notification-content notification-content cm-auto-hide "
                                  "alert-success']")
    error_message_xpath = "//div[@class='cm-notification-content notification-content alert-error']"
    error_tip_XPATH = "//*[@id='login_main_login_error_message']/p"
    signup_error_tip_Xpath = '//p[contains(text(),"Campul")]'
    existing_email_error_XPATH = "//div[@class='cm-notification-content notification-content alert-error']"
    privacy_policy_error_XPATH = "//p[normalize-space()='Acordul dvs. este necesar pentru a continua.']"
