from pages.base_page import BasePage
from locators.locators import WebDriverUniversityLocators


class HiddenElementsPage(BasePage):
    """Methods for clicking and text content extracting."""

    locators = WebDriverUniversityLocators()

    def check_not_displayed_element(self):
        element = self.element_is_present(self.locators.NOT_DISPLAYED)
        self.js_script_click(element)
        modal_title = self.element_is_visible(self.locators.NOT_DISPLAYED_MODAL_TITLE).text
        self.element_is_visible(self.locators.NOT_DISPLAYED_MODAL_CLOSE).click()
        return modal_title

    def check_visibility_hidden_element(self):
        element = self.element_is_present(self.locators.VISIBILITY_HIDDEN)
        self.js_script_click(element)
        modal_title = self.element_is_visible(self.locators.VISIBILITY_HIDDEN_MODAL_TITLE).text
        self.element_is_visible(self.locators.VISIBILITY_HIDDEN_MODAL_CLOSE).click()
        return modal_title

    def check_zero_opacity_element(self):
        element = self.element_is_present(self.locators.ZERO_OPACITY)
        self.js_script_click(element)
        modal_title = self.element_is_visible(self.locators.ZERO_OPACITY_MODAL_TITLE).text
        self.element_is_visible(self.locators.ZERO_OPACITY_MODAL_CLOSE).click()
        return modal_title

