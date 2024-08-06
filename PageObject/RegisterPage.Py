from appium.webdriver.common.mobileby import MobileBy

from page_objects.page import Page


class RegisterPage(Page):
    """ Class contains elements from Register page """

    def __init__(self, driver):
        super(RegisterPage, self).__init__(driver)
        self.os = str(self.driver.desired_capabilities['platformName']).lower()

    # Android
    name_field = (MobileBy.ID, 'com.loginmodule.learning:id/textInputEditTextEmail')
    email_field = (MobileBy.ID, 'com.loginmodule.learning:id/textInputEditTextEmail')
    password_field = (MobileBy.ID, 'com.loginmodule.learning:id/textInputEditTextPassword')
    confirmpassword_field = (MobileBy.ID, 'com.loginmodule.learning:id/textInputLayoutConfirmPassword')
    login_button = (MobileBy.ID, 'com.loginmodule.learning:id/appCompatButtonLogin')
    register_button = (MobileBy.ID, 'com.loginmodule.learning:id/appCompatButtonRegister')


    def register_with_credentials(self, name, email, password, confirmpassword):
        """
        Register with credentials
        :param username: string - username that will be used for logging in
        :param password: string - password that will be used for logging in
        :param password: string - password that will be used for logging in
        :param password: string - password that will be used for logging in
        :return: None
        """
        el = self.wait_for_element_present(*getattr(self, 'name_field_' + self.os))
        el.click()
        el.send_keys(name)
        el = self.wait_for_element_present(*getattr(self, 'email_field_' + self.os))
        el.send_keys(email)
        el = self.wait_for_element_present(*getattr(self, 'password_field_' + self.os))
        el.click()
        el.send_keys(password)
        el = self.wait_for_element_present(*getattr(self, 'confirmpassword_field_' + self.os))
        el.send_keys(confirmpassword)
        self.click_register_button()


    def click_register_button(self):
        """
        Click on Login button
        :return: None
        """
        el = self.wait_for_element_present(*getattr(self, 'login_button_' + self.os))
        el.click()

    def get_invalid_register_message(self):
        """
        Get element text
        :return: Invalid login message
        :rtype: string
        """
        el_text = self.get_element_text(*getattr(self, 'invalid_register_message_' + self.os))
        return el_text


