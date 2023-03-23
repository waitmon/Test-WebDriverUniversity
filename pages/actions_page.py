import random
import time
from pages.base_page import BasePage
from locators.locators import WebDriverUniversityLocators


class ActionsPage(BasePage):
    """Methods for performing some action chains components: double-clicking, dragging and dropping, hovering,
    holding and releasing. """

    locators = WebDriverUniversityLocators()

    def check_double_click(self):
        click_button = self.element_is_visible(self.locators.DOUBLE_CLICK_BUTTON)
        button_status_before_click = click_button.get_attribute('class')
        self.action_double_click(self.element_is_visible(self.locators.DOUBLE_CLICK_BUTTON))
        button_status_after_click = click_button.get_attribute('class')
        assert button_status_before_click != button_status_after_click

    def check_dragg_and_drop(self):
        drag_box = self.element_is_visible(self.locators.DRAGGABLE_BOX)
        drop_box = self.element_is_visible(self.locators.DROPPABLE_BOX)
        self.action_drag_and_drop_to_element(drag_box, drop_box)
        return drop_box.text

    def get_before_and_after_position(self, drag_element):
        self.action_drag_and_drop_by_offset(drag_element, random.randint(0, 50), random.randint(0, 50))
        before_position = drag_element.get_attribute('style')
        self.action_drag_and_drop_by_offset(drag_element, random.randint(0, 50), random.randint(0, 50))
        after_position = drag_element.get_attribute('style')
        return before_position, after_position

    def check_drag_box_moving(self):
        drag_box = self.element_is_visible(self.locators.DRAGGABLE_BOX)
        before_position, after_position = self.get_before_and_after_position(drag_box)
        return before_position, after_position

    def check_hover_button(self):
        self.action_move_to_element(self.element_is_present(self.locators.HOVER_FIRST_BUTTON))
        self.element_is_present(self.locators.HOVER_FIRST_BUTTON_LINK).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_click_and_hold(self):
        self.action_click_and_hold(self.element_is_present(self.locators.CLICK_BOX))
        click_box = self.element_is_present(self.locators.CLICK_BOX)
        return click_box.text

    def check_click_and_release(self):
        click_box = self.element_is_present(self.locators.CLICK_BOX)
        self.element_is_present(self.locators.CLICK_BOX).click()
        return click_box.text
