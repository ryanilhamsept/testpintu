from appium.webdriver.common.mobileby import MobileBy

from page_objects.page import Page


class LoginPage(Page):
    """ Class contains elements from Login page """

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.os = str(self.driver.desired_capabilities['platformName']).lower()

    # Android
    email_field = (MobileBy.ID, 'com.loginmodule.learning:id/textInputEditTextEmail')
    password_field = (MobileBy.ID, 'com.loginmodule.learning:id/textInputEditTextPassword')
    login_button = (MobileBy.ID, 'com.loginmodule.learning:id/appCompatButtonLogin')
    register_button = (MobileBy.ID, 'com.loginmodule.learning:id/textViewLinkRegister')


    def login_with_credentials(self, username, password):
        """
        Login with credentials
        :param email: string - username that will be used for logging in
        :param password: string - password that will be used for logging in
        :return: None
        """
        el = self.wait_for_element_present(*getattr(self, 'email_field' + self.os))
        el.click()
        el.send_keys(username)
        el = self.wait_for_element_present(*getattr(self, 'password_field' + self.os))
        el.send_keys(password)
        self.click_login_button()

    def get_invalid_login_message(self):
        """
        Get element text
        :return: Wrong Email or Password
        :rtype: string
        """
        el_text = self.get_element_text(*getattr(self, 'invalid_login_message' + self.os))
        return el_text

    def click_register_button(self):
        """
        Click on Login button
        :return: None
        """
        el = self.wait_for_element_present(*getattr(self, 'register_button' + self.os))
        el.click()