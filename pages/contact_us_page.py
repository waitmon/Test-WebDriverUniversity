from data.generator import generated_new_user
from pages.base_page import BasePage
from locators.locators import WebDriverUniversityLocators


class ContactUsPage(BasePage):
    """Methods for generating input fields information and checking fields requirement."""

    locators = WebDriverUniversityLocators()

    def check_complete_info_filling(self):
        user_info = next(generated_new_user())
        first_name = user_info.first_name
        last_name = user_info.last_name
        email = user_info.email
        comments = user_info.comments
        self.element_is_present(self.locators.FIRST_NAME_FIELD).send_keys(first_name)
        self.element_is_present(self.locators.LAST_NAME_FIELD).send_keys(last_name)
        self.element_is_present(self.locators.EMAIL_FIELD).send_keys(email)
        self.element_is_present(self.locators.COMMENTS_FIELD).send_keys(comments)
        self.element_is_present(self.locators.SUBMIT_BUTTON_CU).click()
        submit_success = self.element_is_visible(self.locators.SUBMIT_MSG).text
        return submit_success

    def check_empty_info_filling(self):
        self.element_is_present(self.locators.SUBMIT_BUTTON_CU).click()
        error_page = self.element_is_present(self.locators.ERROR_TXT).text
        return error_page

    def check_incomplete_info_filling(self):
        user_info = next(generated_new_user())
        last_name = user_info.last_name
        email = user_info.email
        comments = user_info.comments
        self.element_is_present(self.locators.LAST_NAME_FIELD).send_keys(last_name)
        self.element_is_present(self.locators.EMAIL_FIELD).send_keys(email)
        self.element_is_present(self.locators.COMMENTS_FIELD).send_keys(comments)
        self.element_is_present(self.locators.SUBMIT_BUTTON_CU).click()
        error_page = self.element_is_present(self.locators.ERROR_TXT).text
        return error_page

    def check_invalid_email_filling(self):
        user_info = next(generated_new_user())
        first_name = user_info.first_name
        last_name = user_info.last_name
        comments = user_info.comments
        self.element_is_present(self.locators.FIRST_NAME_FIELD).send_keys(first_name)
        self.element_is_present(self.locators.LAST_NAME_FIELD).send_keys(last_name)
        self.element_is_present(self.locators.EMAIL_FIELD).send_keys('userdotcom')
        self.element_is_present(self.locators.COMMENTS_FIELD).send_keys(comments)
        self.element_is_present(self.locators.SUBMIT_BUTTON_CU).click()
        error_page = self.element_is_present(self.locators.ERROR_TXT).text
        return error_page

    def check_reset_button(self):
        user_info = next(generated_new_user())
        first_name = user_info.first_name
        last_name = user_info.last_name
        email = user_info.email
        comments = user_info.comments
        name_field = self.element_is_present(self.locators.FIRST_NAME_FIELD)
        name_field.send_keys(first_name)
        last_name_field = self.element_is_present(self.locators.LAST_NAME_FIELD)
        last_name_field.send_keys(last_name)
        email_field = self.element_is_present(self.locators.EMAIL_FIELD)
        email_field.send_keys(email)
        comments_field = self.element_is_present(self.locators.COMMENTS_FIELD)
        comments_field.send_keys(comments)
        self.element_is_present(self.locators.RESET_BUTTON).click()
        assert '' in name_field.get_attribute('value')
        assert '' in last_name_field.get_attribute('value')
        assert '' in email_field.get_attribute('value')
        assert '' in comments_field.get_attribute('value')
