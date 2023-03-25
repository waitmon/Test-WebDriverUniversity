import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.locators import WebDriverUniversityLocators


class AccordionPage(BasePage):
    """Methods for checking accordion buttons: extracting text contents, waiting for text to be loaded."""

    locators = WebDriverUniversityLocators()

    def check_buttons_contents_titles(self, accordian_button):
        accordian = {'manual':
                         {'title': self.locators.MANUAL_TESTING_BUTTON,
                          'content': self.locators.MANUAL_TESTING_CONTENT},
                     'cucumber':
                         {'title': self.locators.CUCUMBER_BDD_BUTTON,
                          'content': self.locators.CUCUMBER_BDD_CONTENT},
                     'automation':
                         {'title': self.locators.AUTOMATION_BUTTON,
                          'content': self.locators.AUTOMATION_CONTENT},
                     }

        button_title = self.element_is_visible(accordian[accordian_button]['title'])
        button_title.click()
        button_content = self.element_is_visible(accordian[accordian_button]['content']).text
        return [button_title.text, len(button_content)]

    def check_buttons_status(self):
        active_buttons = [self.locators.MANUAL_TESTING_BUTTON, self.locators.CUCUMBER_BDD_BUTTON,
                          self.locators.AUTOMATION_BUTTON]
        self.element_is_present(random.choice(active_buttons)).click()
        button_status_list = []
        button_active = self.elements_are_present(self.locators.BUTTON_ACTIVE_LIST)
        for status in button_active:
            active_status = status.get_attribute('class')
            button_status_list.append(active_status)
        assert 'accordion active' in button_status_list

    def check_keep_clicking_menu(self):
        hidden_text = (By.ID, 'timeout')
        loading_text = 'This text has appeared after 5 seconds!'
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(hidden_text, loading_text))
        text_appear_box = self.driver.find_element(By.ID, 'timeout')
        self.element_is_present(self.locators.KEEP_CLICKING_BUTTON).click()
        return text_appear_box.text

    def check_loading_text(self):
        hidden_text = (By.CSS_SELECTOR, '#hidden-text')
        loading_text = 'LOADING COMPLETE.'
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(hidden_text, loading_text))
        text_appear_box = self.driver.find_element(By.CSS_SELECTOR, '#hidden-text')
        return text_appear_box.text
