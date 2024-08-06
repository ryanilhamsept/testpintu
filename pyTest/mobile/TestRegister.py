from nose.tools import assert_true

from base_test import BaseTest
from page_objects.login_page import LoginPage
from page_objects.register_page import RegisterPage



class TestRegister(BaseTest):
    """
    Test suite deals with testing register feature
    """

    def test_01_register_with_valid(self):
        """
        Register new account
        """
        
        login_page = LoginPage(self.driver)
        Register_page = RegisterPage(self.driver)

        "Login details"
        name = "test-001"
        email = "test@abc.com"
        password = "123456"
        confirmpasswordpassword = "123456"

        "Register with data valid"
        login_page.click_register_button()
        Register_page.login_with_credentials(name=name, email=email ,password=password, confirmpassword=confirmpasswordpassword)

        "Verify that account button is displayed"
        account_button_displayed = Register_page()
        assert_true(account_button_displayed, "Registration Successfull")
        print("Registration Successfull")

    def test_02_register_invalid_email(self):
        """
        Register with invalid format email .
        """

        login_page = LoginPage(self.driver)
        Register_page = RegisterPage(self.driver)

        "Login details"
        name = "test-001"
        email = "123132342424"
        password = "123456"
        confirmpasswordpassword = "123456"

        "Register with data valid"
        login_page.click_register_button()
        Register_page.login_with_credentials(name=name, email=email ,password=password, confirmpassword=confirmpasswordpassword)


        "Verify user is not logged in, message for invalid login is displayed"
        invalid_register_message_ = Register_page.get_invalid_register_message()
        assert_true(invalid_register_message_ == "Enter Valid Email")
        print("Enter Valid Email")

