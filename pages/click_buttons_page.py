from pages.base_page import BasePage
from locators.locators import WebDriverUniversityLocators
import random


class ClickButtonsPage(BasePage):
    """Methods for various types of actions clicking performing: basic web_element.click(), js_executor script and move to
    element method."""

    locators = WebDriverUniversityLocators()

    def check_web_element_click(self):
        self.element_is_present(self.locators.WEB_ELEMENT_CLICK_BUTTON).click()
        close_buttons = [self.locators.DIALOG_BOX_CLOSE_BUTTON, self.locators.DIALOG_BOX_DISMISS_X_BUTTON]
        self.element_is_clickable(random.choice(close_buttons)).click()
        return self.element_is_present(self.locators.WEB_ELEMENT_CONGRATS_TEXT).text

    def check_js_click(self):
        js_button = self.element_is_present(self.locators.JS_CLICK_BUTTON)
        self.js_script_click(js_button)
        close_buttons = [self.locators.JS_DIALOG_BOX_CLOSE_BUTTON, self.locators.JS_DIALOG_BOX_DISMISS_X_BUTTON]
        self.element_is_clickable(random.choice(close_buttons)).click()
        return self.element_is_present(self.locators.JS_DIALOG_BOX_TEXT).text

    def check_action_click(self):
        action_button = self.element_is_present(self.locators.ACTION_MOVE_AND_CLICK_BUTTON)
        self.action_move_to_element(action_button)
        action_button.click()
        close_buttons = [self.locators.ACTION_DIALOG_BOX_CLOSE_BUTTON, self.locators.ACTION_DIALOG_BOX_DISMISS_X_BUTTON]
        self.element_is_clickable(random.choice(close_buttons)).click()
        return self.element_is_present(self.locators.ACTION_DIALOG_BOX_TEXT).text

