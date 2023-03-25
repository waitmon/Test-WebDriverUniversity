import random
from pages.base_page import BasePage
from locators.locators import WebDriverUniversityLocators


class DatePickerPage(BasePage):
    """Methods for randomly picking year/month/day and asserting chosen date value."""
    locators = WebDriverUniversityLocators()

    def check_change_date(self):
        default_date = self.element_is_present(self.locators.TEXT_FIELD)
        default_date_attr = default_date.get_attribute("value")
        self.element_is_present(self.locators.SELECT_DATE).click()
        self.element_is_present(self.locators.MONTH_SWITCHER).click()
        self.element_is_present(self.locators.YEAR_SWITCHER).click()
        year_list = self.elements_are_present(self.locators.YEARS_LIST)
        year_selection = year_list[random.randint(1, 9)]
        self.action_move_to_element(year_selection)
        year_selection.click()
        month_list = self.elements_are_present(self.locators.MONTH_LIST)
        month_selection = month_list[random.randint(1, 12)]
        self.action_move_to_element(month_selection)
        month_selection.click()
        days_list = self.elements_are_present(self.locators.DAYS_LIST)
        days_selection = days_list[random.randint(1, 31)]
        self.action_move_to_element(days_selection)
        days_selection.click()
        chosen_date = self.element_is_present(self.locators.TEXT_FIELD)
        chosen_date_attr = chosen_date.get_attribute("value")
        assert default_date_attr != chosen_date_attr
