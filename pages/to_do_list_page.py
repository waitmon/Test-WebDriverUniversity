import random
import time
from selenium.webdriver import Keys
from pages.base_page import BasePage
from locators.locators import WebDriverUniversityLocators


class ToDoListPage(BasePage):
    """Methods for basic interaction with to-do list: checking tasks attributes, deleting and adding tasks."""

    locators = WebDriverUniversityLocators()

    def check_completed_task(self):
        tasks_available = [self.locators.ALL_TASKS]
        self.element_is_present(random.choice(tasks_available)).click()
        task_status_list = []
        tasks_status = self.elements_are_present(self.locators.COMPLETED_TASKS)
        for status in tasks_status:
            completed_status = status.get_attribute('class')
            task_status_list.append(completed_status)
        assert 'completed' in task_status_list

    def check_deleted_task(self):
        available_tasks = [self.locators.TASK_1, self.locators.TASK_2, self.locators.TASK_3]
        trash_buttons_icons = [self.locators.TRASH_BUTTONS]
        self.element_is_present(random.choice(trash_buttons_icons)).click()
        time.sleep(0.5)
        total_tasks = self.elements_are_present(self.locators.ALL_TASKS)
        tasks_remains_list = []
        for task in total_tasks:
            task_available = task.text
            tasks_remains_list.append(task_available)
        assert len(tasks_remains_list) == len(available_tasks) - 1

    def check_hidden_button(self):
        self.element_is_present(self.locators.HIDDEN_BUTTON).click()
        time.sleep(0.5)
        new_task_field = self.element_is_present(self.locators.ADD_NEW_TODO_FIELD)
        new_task_status = new_task_field.get_attribute('style')
        assert 'display: none;' in new_task_status

    def check_add_new_task(self):
        available_tasks = [self.locators.TASK_1, self.locators.TASK_2, self.locators.TASK_3]
        new_task_field = self.element_is_visible(self.locators.ADD_NEW_TODO_FIELD)
        new_task_field.send_keys('coding')
        new_task_field.send_keys(Keys.RETURN)
        total_tasks = self.elements_are_present(self.locators.ALL_TASKS)
        tasks_remains_list = []
        for task in total_tasks:
            task_available = task.text
            tasks_remains_list.append(task_available)
        assert len(tasks_remains_list) == len(available_tasks) + 1
