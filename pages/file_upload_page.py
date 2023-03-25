import os
from data.generator import generated_file
from pages.base_page import BasePage
from locators.locators import WebDriverUniversityLocators


class FileUploadPage(BasePage):
    """Methods for generating files and further uploading."""

    locators = WebDriverUniversityLocators()

    def check_file_upload(self):
        file_name, path = generated_file()
        self.element_is_present(self.locators.UPLOAD_BUTTON).send_keys(path)
        os.remove(path)
        self.element_is_present(self.locators.SUBMIT_UPLOAD).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text
