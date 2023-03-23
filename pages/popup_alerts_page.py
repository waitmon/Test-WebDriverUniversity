import random
import time

from pages.base_page import BasePage
from locators.locators import WebDriverUniversityLocators


class PopUpAlertsPage(BasePage):
    """Methods for clicking and text content extracting."""
    locators = WebDriverUniversityLocators()

    def check_js_alert(self):
        self.element_is_present(self.locators.JS_ALERT).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_modal_popup(self):
        self.element_is_present(self.locators.MODAL_POPUP_BUTTON).click()
        modal_title = self.element_is_visible(self.locators.MODAL_TITLE)
        modal_content = self.element_is_visible(self.locators.MODAL_CONTENT).text
        return modal_title.text, len(modal_content)

    def check_ajax_loader(self):
        self.element_is_present(self.locators.AJAX_LOADER).click()
        self.element_is_visible(self.locators.AJAX_BUTTON)
        self.element_is_present(self.locators.AJAX_BUTTON).click()
        modal_title = self.element_is_visible(self.locators.MODAL_TITLE)
        modal_content = self.element_is_visible(self.locators.AJAX_CONTENT).text
        return modal_title.text, len(modal_content)

    def check_js_confirm_box_accept(self):
        self.element_is_present(self.locators.JS_CONFIRM_BOX).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()
        confirm_text = self.element_is_present(self.locators.JS_CONFIRM_TEXT).text
        return confirm_text

    def check_js_confirm_box_dismiss(self):
        self.element_is_present(self.locators.JS_CONFIRM_BOX).click()
        alert_window = self.driver.switch_to.alert
        alert_window.dismiss()
        confirm_text = self.element_is_present(self.locators.JS_CONFIRM_TEXT).text
        return confirm_text
