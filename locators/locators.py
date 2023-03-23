from selenium.webdriver.common.by import By


class WebDriverUniversityLocators:
    """Set of web-elements locators of various subsections from the main page (https://webdriveruniversity.com/)."""

    # Click-Buttons Page
    WEB_ELEMENT_CLICK_BUTTON = (By.CSS_SELECTOR, "[data-target='#myModalClick']")
    JS_CLICK_BUTTON = (By.CSS_SELECTOR, "[data-target='#myModalJSClick']")
    DIALOG_BOX_DISMISS_X_BUTTON = (By.CSS_SELECTOR, '#myModalClick > div > div > div.modal-header > button')
    DIALOG_BOX_CLOSE_BUTTON = (By.CSS_SELECTOR, "#myModalClick > div > div > div.modal-footer > button")
    WEB_ELEMENT_CONGRATS_TEXT = (By.CSS_SELECTOR, '#myModalClick > div > div > div.modal-body > p')
    JS_DIALOG_BOX_DISMISS_X_BUTTON = (By.CSS_SELECTOR, '#myModalJSClick > div > div > div.modal-header > button')
    JS_DIALOG_BOX_CLOSE_BUTTON = (By.CSS_SELECTOR, "#myModalJSClick > div > div > div.modal-footer > button")
    JS_DIALOG_BOX_TEXT = (By.CSS_SELECTOR, '#myModalJSClick > div > div > div.modal-header > h4')
    ACTION_MOVE_AND_CLICK_BUTTON = (By.CSS_SELECTOR, 'span[id="button3"]')
    ACTION_DIALOG_BOX_DISMISS_X_BUTTON = (By.CSS_SELECTOR, '#myModalMoveClick > div > div > div.modal-header > button')
    ACTION_DIALOG_BOX_CLOSE_BUTTON = (By.CSS_SELECTOR, "##myModalMoveClick > div > div > div.modal-footer > button")
    ACTION_DIALOG_BOX_TEXT = (By.CSS_SELECTOR, '#myModalMoveClick > div > div > div.modal-header > h4')

    # To-Do List Page
    ADD_NEW_TODO_FIELD = (By.CSS_SELECTOR, 'input[type="text"]')
    HIDDEN_BUTTON = (By.CSS_SELECTOR, 'i[id="plus-icon"]')
    TRASH_BUTTON_1 = (By.CSS_SELECTOR, '#container > ul > li:nth-child(1) > span > i')
    TRASH_BUTTON_2 = (By.CSS_SELECTOR, '#container > ul > li:nth-child(2) > span > i')
    TRASH_BUTTON_3 = (By.CSS_SELECTOR, '#container > ul > li:nth-child(3) > span > i')
    TRASH_BUTTONS = (By.CSS_SELECTOR, 'i[class="fa fa-trash"]')
    COMPLETED_TASKS = (By.CSS_SELECTOR, 'li[class]')
    ALL_TASKS = (By.CSS_SELECTOR, '#container > ul > li:nth-child(n)')
    TASK_QTY = (By.XPATH, '//*[@id="container"]/ul/li[*]/text()')
    TASK_1 = (By.CSS_SELECTOR, '#container > ul > li:nth-child(1)')
    TASK_2 = (By.CSS_SELECTOR, '#container > ul > li:nth-child(2)')
    TASK_3 = (By.CSS_SELECTOR, '#container > ul > li:nth-child(3)')

    # Accordion Page
    # buttons / titles
    MANUAL_TESTING_BUTTON = (By.CSS_SELECTOR, 'button[id="manual-testing-accordion"]')
    CUCUMBER_BDD_BUTTON = (By.CSS_SELECTOR, 'button[id="cucumber-accordion"]')
    AUTOMATION_BUTTON = (By.CSS_SELECTOR, 'button[id="automation-accordion"]')
    KEEP_CLICKING_BUTTON = (By.CSS_SELECTOR, 'button[id="click-accordion"]')
    BUTTON_LIST = (By.CSS_SELECTOR, 'button[class="accordion"]')
    BUTTON_ACTIVE_LIST = (By.CSS_SELECTOR, 'button[class="accordion active"]')

    # contents
    MANUAL_TESTING_CONTENT = (By.CSS_SELECTOR, '#manual-testing-description > p')
    CUCUMBER_BDD_CONTENT = (By.CSS_SELECTOR, '#cucumber-testing-description > p')
    AUTOMATION_CONTENT = (By.CSS_SELECTOR, '#automation-testing-description > p')
    KEEP_CLICKING_CONTENT = (By.CSS_SELECTOR, '#timeout')
    HIDDEN_TEXT = (By.CSS_SELECTOR, '#hidden-text')

    # Actions Page
    DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, 'div[id="double-click"]')
    DROPPABLE_BOX = (By.CSS_SELECTOR, 'div[id="droppable"]')
    DRAGGABLE_BOX = (By.CSS_SELECTOR, 'div[id="draggable"]')
    HOVER_FIRST_BUTTON = (By.CSS_SELECTOR, '#div-hover > div.dropdown.hover > button')
    HOVER_FIRST_BUTTON_LINK = (By.CSS_SELECTOR, '#div-hover > div.dropdown.hover > div > a')
    CLICK_BOX = (By.CSS_SELECTOR, 'div[id="click-box"]')

    # AJAX Loader Page
    LOADING_BUTTON = (By.CSS_SELECTOR, '#button1 > p')
    BUTTON_MODAL_TEXT = (By.CSS_SELECTOR, 'h4[class="modal-title"]')

    # Scrolling Page
    SCROLL_TO_ME_THUMBNAIL = (By.CSS_SELECTOR, 'div[id="zone1"]')
    FIRST_ENTRIES_THUMBNAIL = (By.CSS_SELECTOR, 'div[id="zone2"]')
    SECOND_ENTRIES_THUMBNAIL = (By.CSS_SELECTOR, 'div[id="zone3"]')
    FOOTER_THUMBNAIL = (By.CSS_SELECTOR, 'div[id="zone4"]')

    # Pop-up & Alerts Page
    JS_ALERT = (By.CSS_SELECTOR, 'span[id="button1"]')
    MODAL_POPUP_BUTTON = (By.CSS_SELECTOR, 'span[id="button2"]')
    MODAL_POPUP_WINDOW = (By.CSS_SELECTOR, 'div[class="modal-content"]')
    MODAL_CONTENT = (By.CSS_SELECTOR, '#myModal > div > div > div.modal-body > p')
    MODAL_TITLE = (By.CSS_SELECTOR, 'h4[class="modal-title"]')
    AJAX_LOADER = (By.CSS_SELECTOR, 'span[id="button3"]')
    AJAX_BUTTON = (By.CSS_SELECTOR, '#button1 > p')
    AJAX_CONTENT = (By.CSS_SELECTOR, 'div[class="modal-body"]')
    JS_CONFIRM_BOX = (By.CSS_SELECTOR, 'span[id="button4"]')
    JS_CONFIRM_TEXT = (By.CSS_SELECTOR, 'p[id="confirm-alert-text"]')

    # Hidden Elements Page
    NOT_DISPLAYED = (By.CSS_SELECTOR, '#button1')
    VISIBILITY_HIDDEN = (By.CSS_SELECTOR, '#button2')
    ZERO_OPACITY = (By.CSS_SELECTOR, '#button3')
    NOT_DISPLAYED_MODAL_TITLE = (By.XPATH, "//h4[@class='modal-title']")
    NOT_DISPLAYED_MODAL_CLOSE = (By.XPATH, "//div[@class='modal-footer']/button")
    VISIBILITY_HIDDEN_MODAL_TITLE = (By.XPATH, "(//h4[@class='modal-title'])[2]")
    VISIBILITY_HIDDEN_MODAL_CLOSE = (By.XPATH, "(//div[@class='modal-footer']/button)[2]")
    ZERO_OPACITY_MODAL_TITLE = (By.XPATH, "(//h4[@class='modal-title'])[3]")
    ZERO_OPACITY_MODAL_CLOSE = (By.XPATH, "(//div[@class='modal-footer']/button)[3]")

    # Autocomplete Page
    INPUT_FIELD = (By.CSS_SELECTOR, 'input[id="myInput"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'input[id="submit-button"]')
    AUTOCOMPLETE_PLACEHOLDER = (By.CSS_SELECTOR, '#myInputautocomplete-list > div > strong')


