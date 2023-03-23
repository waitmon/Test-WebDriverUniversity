from pages.accordion_page import AccordionPage
from pages.actions_page import ActionsPage
from pages.ajax_loader_page import AjaxLoaderPage
from pages.click_buttons_page import ClickButtonsPage
from pages.hidden_elements_page import HiddenElementsPage
from pages.scrolling_page import ScrollingPage
from pages.to_do_list_page import ToDoListPage
from pages.popup_alerts_page import PopUpAlertsPage
from pages.autocomplete_page import AutoCompleteTextFieldPage


class TestClickButtonsPage:
    """Performing various types of clicking methods, close buttons interactions, dialog boxes text assertions."""

    def test_web_element_click(self, driver):
        click = ClickButtonsPage(driver, 'https://webdriveruniversity.com/Click-Buttons/index.html')
        click.open()
        web_element_click_result = click.check_web_element_click()
        assert web_element_click_result == 'Well done for successfully using the click() method!'

    def test_js_click(self, driver):
        click = ClickButtonsPage(driver, 'https://webdriveruniversity.com/Click-Buttons/index.html')
        click.open()
        js_click_result = click.check_js_click()
        assert js_click_result == 'It’s that Easy!! Well I think it is.....'

    def test_action_move_click(self, driver):
        click = ClickButtonsPage(driver, 'https://webdriveruniversity.com/Click-Buttons/index.html')
        click.open()
        action_click_result = click.check_action_click()
        assert action_click_result == 'Well done! the Action Move & Click can become very useful!'


class TestToDoListPage:
    """Performing basic operations with to-do list: adding, removing, hidding tasks."""

    def test_complete_tasks(self, driver):
        to_do = ToDoListPage(driver, 'https://webdriveruniversity.com/To-Do-List/index.html')
        to_do.open()
        to_do.check_completed_task()

    def test_delete_tasks(self, driver):
        to_do = ToDoListPage(driver, 'https://webdriveruniversity.com/To-Do-List/index.html')
        to_do.open()
        to_do.check_deleted_task()

    def test_hide_task(self, driver):
        to_do = ToDoListPage(driver, 'https://webdriveruniversity.com/To-Do-List/index.html')
        to_do.open()
        to_do.check_hidden_button()

    def test_add_task(self, driver):
        to_do = ToDoListPage(driver, 'https://webdriveruniversity.com/To-Do-List/index.html')
        to_do.open()
        to_do.check_add_new_task()


class TestAccordionPage:
    """Performing basic operations with accordion widgets: expanding buttons and contents checking."""

    def test_accordian_buttons(self, driver):
        accordion_page = AccordionPage(driver, 'https://webdriveruniversity.com/Accordion/index.html')
        accordion_page.open()
        first_button, first_content, = accordion_page.check_buttons_contents_titles('manual')
        second_button, second_content = accordion_page.check_buttons_contents_titles('cucumber')
        third_button, third_content = accordion_page.check_buttons_contents_titles('automation')
        assert first_button == 'Manual Testing' and first_content > 0
        assert second_button == 'Cucumber BDD' and second_content > 0
        assert third_button == 'Automation Testing' and third_content > 0

    def test_accordian_status(self, driver):
        accordion_page = AccordionPage(driver, 'https://webdriveruniversity.com/Accordion/index.html')
        accordion_page.open()
        accordion_page.check_buttons_status()

    def test_keep_clicking_menu(self, driver):
        accordion_page = AccordionPage(driver, 'https://webdriveruniversity.com/Accordion/index.html')
        accordion_page.open()
        loading_text = accordion_page.check_keep_clicking_menu()
        assert loading_text == 'This text has appeared after 5 seconds!'

    def test_loading_box_text(self, driver):
        accordion_page = AccordionPage(driver, 'https://webdriveruniversity.com/Accordion/index.html')
        accordion_page.open()
        loading_text = accordion_page.check_loading_text()
        assert loading_text == 'LOADING COMPLETE.'


class TestActionsPage:
    """Performing basic actions: double-clicking, dragging and dropping, hovering, holding and releasing."""

    def test_double_click_button(self, driver):
        actions = ActionsPage(driver, 'https://webdriveruniversity.com/Actions/index.html')
        actions.open()
        actions.check_double_click()

    def test_dragg_and_drop(self, driver):
        actions = ActionsPage(driver, 'https://webdriveruniversity.com/Actions/index.html')
        actions.open()
        drop_text = actions.check_dragg_and_drop()
        assert drop_text == 'Dropped!'

    def test_drag_box_moving(self, driver):
        actions = ActionsPage(driver, 'https://webdriveruniversity.com/Actions/index.html')
        actions.open()
        before, after = actions.check_drag_box_moving()
        assert before != after

    def test_hover_button(self, driver):
        actions = ActionsPage(driver, 'https://webdriveruniversity.com/Actions/index.html')
        actions.open()
        alert_message = actions.check_hover_button()
        assert alert_message == 'Well done you clicked on the link!'

    def test_click_and_hold(self, driver):
        actions = ActionsPage(driver, 'https://webdriveruniversity.com/Actions/index.html')
        actions.open()
        box_message = actions.check_click_and_hold()
        assert box_message == 'Well done! keep holding that click now.....'

    def test_click_and_release(self, driver):
        actions = ActionsPage(driver, 'https://webdriveruniversity.com/Actions/index.html')
        actions.open()
        box_message = actions.check_click_and_release()
        assert box_message == 'Dont release me!!!'


class TestAjaxLoader:
    """Performing explicit waiting of AJAX element."""

    def test_ajax_loader(self, driver):
        ajax = AjaxLoaderPage(driver, 'https://webdriveruniversity.com/Ajax-Loader/index.html')
        ajax.open()
        button_text = ajax.check_button_loading()
        assert button_text == 'Well Done For Waiting....!!!'


class TestScrollingPage:
    """Performing scrolling imitations."""

    def test_scrolling_to_thumbnail(self, driver):
        scrolling = ScrollingPage(driver, 'https://webdriveruniversity.com/Scrolling/index.html')
        scrolling.open()
        thumbnail = scrolling.check_scrolling_to_thumbnail()
        assert thumbnail == 'Well done for scrolling to me!'

    def test_scrolling_to_entries(self, driver):
        scrolling = ScrollingPage(driver, 'https://webdriveruniversity.com/Scrolling/index.html')
        scrolling.open()
        scrolling.check_scrolling_to_entries_thumbnails()

    def test_scrolling_to_footer_thumbnail(self, driver):
        scrolling = ScrollingPage(driver, 'https://webdriveruniversity.com/Scrolling/index.html')
        scrolling.open()
        scrolling.check_scrolling_to_footer_thumbnail()


class TestPopUpAlerts:
    """Performing interactions with various pop-up and modal windows: clicking, contents extracting."""
    def test_js_alert(self, driver):
        alert = PopUpAlertsPage(driver, 'https://webdriveruniversity.com/Popup-Alerts/index.html')
        alert.open()
        alert_message = alert.check_js_alert()
        assert alert_message == 'I am an alert box!'

    def test_modal_popup(self, driver):
        alert = PopUpAlertsPage(driver, 'https://webdriveruniversity.com/Popup-Alerts/index.html')
        alert.open()
        alert_message, alert_content = alert.check_modal_popup()
        assert alert_message == 'It’s that Easy!! Well I think it is.....' and alert_content > 0

    def test_ajax_loader(self, driver):
        alert = PopUpAlertsPage(driver, 'https://webdriveruniversity.com/Popup-Alerts/index.html')
        alert.open()
        alert_message, alert_content = alert.check_ajax_loader()
        assert alert_message == 'Well Done For Waiting....!!!' and alert_content > 0

    def test_js_confirm_box_accept(self, driver):
        alert = PopUpAlertsPage(driver, 'https://webdriveruniversity.com/Popup-Alerts/index.html')
        alert.open()
        alert_message = alert.check_js_confirm_box_accept()
        assert alert_message == 'You pressed OK!'

    def test_js_confirm_box_dismiss(self, driver):
        alert = PopUpAlertsPage(driver, 'https://webdriveruniversity.com/Popup-Alerts/index.html')
        alert.open()
        alert_message = alert.check_js_confirm_box_dismiss()
        assert alert_message == 'You pressed Cancel!'


class TestHiddenElements:
    """Performing clicking interactions with hidden elements."""
    def test_not_displayed_element(self, driver):
        hidden_elements = HiddenElementsPage(driver, 'https://webdriveruniversity.com/Hidden-Elements/index.html')
        hidden_elements.open()
        modal_title = hidden_elements.check_not_displayed_element()
        assert modal_title == 'Congratulations!'

    def test_visibility_hidden_element(self, driver):
        hidden_elements = HiddenElementsPage(driver, 'https://webdriveruniversity.com/Hidden-Elements/index.html')
        hidden_elements.open()
        modal_title = hidden_elements.check_visibility_hidden_element()
        assert modal_title == 'It’s that Easy!! Well I think it is.....'

    def test_zero_opacity_element(self, driver):
        hidden_elements = HiddenElementsPage(driver, 'https://webdriveruniversity.com/Hidden-Elements/index.html')
        hidden_elements.open()
        modal_title = hidden_elements.check_zero_opacity_element()
        assert modal_title == 'Well done! the Action Move & Click can become very useful!'


class TestAutoCompleteTextField:
    """Performing interactions with autocomplete fields: inputting and asserting inner data."""
    def test_input_placeholder_data(self, driver):
        autocomplete = AutoCompleteTextFieldPage(driver, 'https://webdriveruniversity.com/Autocomplete-TextField'
                                                         '/autocomplete-textfield.html')
        autocomplete.open()
        autocomplete.check_input_placeholder_data()

    def test_input_non_placeholder_data(self, driver):
        autocomplete = AutoCompleteTextFieldPage(driver, 'https://webdriveruniversity.com/Autocomplete-TextField'
                                                         '/autocomplete-textfield.html')
        autocomplete.open()
        autocomplete.check_input_non_placeholder_data()
