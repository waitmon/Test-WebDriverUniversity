from pages.base_page import BasePage
from locators.locators import WebDriverUniversityLocators


class ScrollingPage(BasePage):
    """Methods for scrolling actions: performing scrolling itself and getting attribute changes of web-elements."""

    locators = WebDriverUniversityLocators()

    def check_scrolling_to_thumbnail(self):
        thumbnail = self.element_is_present(self.locators.SCROLL_TO_ME_THUMBNAIL)
        self.action_move_to_element(thumbnail)
        return thumbnail.text

    def check_scrolling_to_entries_thumbnails(self):
        first_thumbnail = self.element_is_present(self.locators.FIRST_ENTRIES_THUMBNAIL)
        second_thumbnail = self.element_is_present(self.locators.SECOND_ENTRIES_THUMBNAIL)
        self.scroll_to_element(first_thumbnail)
        self.action_move_to_element(first_thumbnail)
        self.scroll_to_element(second_thumbnail)
        self.action_move_to_element(second_thumbnail)
        assert '0 Entries' not in first_thumbnail.text, second_thumbnail.text

    def check_scrolling_to_footer_thumbnail(self):
        footer_thumbnail = self.element_is_present(self.locators.FOOTER_THUMBNAIL)
        self.scroll_to_element(footer_thumbnail)
        self.action_move_to_element(footer_thumbnail)
        footer_attr = footer_thumbnail.get_attribute('style')
        assert 'background: black' in footer_attr
