from appium.webdriver.common.mobileby import MobileBy

from page_objects.page import Page


class HomePage(Page):
    """ Class contains elements from Home page """

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)
        self.os = str(self.driver.desired_capabilities['platformName']).lower()


    home_field = (MobileBy.XPATH, '//android.widget.TextView[@text="Android NewLine Learning"]')
    detail_name_field = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="com.loginmodule.learning:id/textViewName" and @text="tese"]')
    detail_email_field = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="com.loginmodule.learning:id/textViewEmail"]')


    def is_displayed_homepage(self):
        """
        Check if success login to home page
        """
        el_visible = self.is_element_visible(*getattr(self, 'home_field' + self.os))
        return el_visible