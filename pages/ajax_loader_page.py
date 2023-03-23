import time

from pages.base_page import BasePage
from locators.locators import WebDriverUniversityLocators


class AjaxLoaderPage(BasePage):
    """Method for waiting performance of ajax button loading process."""

    locators = WebDriverUniversityLocators()

    def check_button_loading(self):
        self.element_is_visible(self.locators.LOADING_BUTTON)
        self.element_is_present(self.locators.LOADING_BUTTON).click()
        modal_window_text = self.element_is_visible(self.locators.BUTTON_MODAL_TEXT)
        return modal_window_text.text


