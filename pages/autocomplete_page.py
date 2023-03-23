import random
import time
from data.generator import generated_food
from pages.base_page import BasePage
from locators.locators import WebDriverUniversityLocators


class AutoCompleteTextFieldPage(BasePage):
    """Methods for autocomplete performing and asserting inner data from js.bundle."""
    locators = WebDriverUniversityLocators()

    def check_input_placeholder_data(self):
        food = random.sample(next(generated_food()).food_name, k=1)
        input_single = self.element_is_clickable(self.locators.INPUT_FIELD)
        input_single.send_keys(food)
        placeholder = self.element_is_visible(self.locators.AUTOCOMPLETE_PLACEHOLDER)
        assert placeholder.is_displayed()

    def check_input_non_placeholder_data(self):
        input_single = self.element_is_clickable(self.locators.INPUT_FIELD)
        input_single.send_keys('steak')
        placeholder = self.locators.AUTOCOMPLETE_PLACEHOLDER
        assert self.element_is_not_visible(placeholder)

