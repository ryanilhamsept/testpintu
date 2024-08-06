from nose.tools import assert_true

from base_test import BaseTest
from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage


class TestLogin(BaseTest):
    """
    Test suite deals with testing login feature
    """

    def test_01_login_with_valid_credentials(self):
       
     
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)

        "Login details"
        email = "test@abc.com"
        password = "123456"

        "Login with valid username and password"

        login_page.login_with_credentials(email=email, password=password)

        "Verify that account button is displayed"
        home_displayed = home_page.is_displayed_homepage()
        assert_true(home_displayed, "Account button is not displayed")
        print("User successfully logged in. Account button is displayed.")

    def test_02_login_with_invalid_username_valid_password(self):
        """
        Login with invalid username and valid password.
        Verify user is not logged in and correct message is displayed.
        """
    
        login_page = LoginPage(self.driver)

        "Login details"
        email = "fake@username.com"
        password = "ValidPassword"

        "Login with invalid username and valid password"
    
        login_page.login_with_credentials(email=email, password=password)

        "Verify user is not logged in, message for invalid login is displayed"
        invalid_login_message = login_page.get_invalid_login_message()
        assert_true(invalid_login_message ==  "Wrong Email or Password")
        print("Wrong Email or Password")

