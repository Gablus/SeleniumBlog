from selenium.webdriver.common.by import By


class BasePage(object):
    def __init__(self,browser):
        self.browser = browser
        # Define Explicit Waits for 5 sec
        self.wait = WebDriverWait(self.browser,5)

class LoginPage(BasePage):
    # Selectors 
    CSS_SELECTOR = By.CSS_SELECTOR
    EMAIL_FIELD = "input[type='email']"
    PASSWORD_FIELD = "input[type='password']"
    SUBMIT_BUTTON = "input[type='submit']"
    HEADER_LABEL = "h1[align='center']"

    # Methods 
    # def __init__(self,browser):
    #    self.browser = browser

    def enter_email(self,email):
        email_field = self.browser.find_element(self.CSS_SELECTOR, self.EMAIL_FIELD)
        email_field.send_keys(email)

    def enter_password(self,password):
        password_field = self.browser.find_element(self.CSS_SELECTOR, self.PASSWORD_FIELD)
        password_field.send_keys(password)
    
    def submit_form(self):
        submit_button = self.browser.find_element(self.CSS_SELECTOR,self.SUBMIT_BUTTON)
        submit_button.click()

class ArticlesPage(BasePage):
    # Selectors 
    CSS_SELECTOR = By.CSS_SELECTOR
    # Css selector Article page 
    DELETE_BUTTON = "a[data-method='delete']"
    EDIT_BUTTON = "a.btn.btn-xs.btn-primary"
    CREATE_LINK = "a[href='/articles/new']"
    HEADER_LABEL = "h1[align='center']"
    # CSS selector new article page
    TITLE_FIELD = "#article_title"
    DESCRIPTION_FIELD = "#article_description"
    SUBMIT_BUTTON = "input[type='submit']"
    CANCEL_LINK = "a[href='/articles']"

    # Methods 
    # def __init__(self,browser):
    #   self.browser = browser

    def get_header(self):
        header = self.browser.find_element(self.CSS_SELECTOR,self.HEADER_LABEL)
        return header.text

    def enter_title(self,title):
        email_field = self.browser.find_element(self.CSS_SELECTOR, self.TITLE_FIELD)
        email_field.send_keys(title)

    def enter_description(self,description):
        password_field = self.browser.find_element(self.CSS_SELECTOR, self.DESCRIPTION_FIELD)
        password_field.send_keys(description)

    def submit_form(self):
        delete_buttons = self.wait.until(EC.element_to_be_clickable((self.CSS_SELECTOR,self.SUBMIT_BUTTON)))
        delete_buttons.click()
    
    def edit_article(self):
        edit_button = self.wait.until(EC.element_to_be_clickable((self.CSS_SELECTOR,self.EDIT_BUTTON)))
        edit_button.click()
    
    def create_article(self):
        create_button = self.browser.find_element(self.CSS_SELECTOR,self.CREATE_LINK)
        create_button.click()
    
    def delete_article(self):
        delete_button = self.wait.until(EC.element_to_be_clickable((self.CSS_SELECTOR,self.DELETE_BUTTON)))
        delete_button.click()

    def click_cancel(self):
        cancel_link = self.wait.until(EC.element_to_be_clickable((self.CSS_SELECTOR,self.CANCEL_LINK)))
        cancel_link.click()
    
class LayoutPage(BasePage):

    # Selectors 
    CSS_SELECTOR = By.CSS_SELECTOR
    LOGIN_BUTTON = "a.btn.btn-lg.btn-primary"
    SIGNUP_BUTTON = "a.btn.btn-lg.btn-success"
    LOGIN_LINK = "a[href='/login']"
    SIGNPUP_LINK = "a[href='/signup']"

    # Methods 
    # def __init__(self,browser):
    #    self.browser = browser
    #    # Define Explicit Waits for 5 sec
    #    self.wait = WebDriverWait(self.browser,5)

    def click_login_button(self):
        login_buttons = self.wait.until(EC.element_to_be_clickable((self.CSS_SELECTOR,self.LOGIN_BUTTON)))
        login_buttons.click()

    def click_signup_button(self):
        signup_buttons = self.wait.until(EC.element_to_be_clickable((self.CSS_SELECTOR,self.SIGNUP_BUTTON)))
        signup_buttons.click()

    def click_login_link(self):
        signup_buttons = self.wait.until(EC.element_to_be_clickable((self.CSS_SELECTOR,self.LOGIN_BUTTON)))
        signup_buttons.click()
    
    def click_sigup_link(self):
        signup_buttons = self.wait.until(EC.element_to_be_clickable((self.CSS_SELECTOR,self.SIGNUP_BUTTON)))
        signup_buttons.click()

class SignupPage(BasePage):

    # selectors 
    CSS_SELECTOR = By.CSS_SELECTOR
    USERNAME_FIELD = "#user_username"
    EMAIL_FIELD = "#user_email"
    PASSWORD_FIELD = "#user_password"
    SUBMIT_BUTTON = "#submit"
    HEADER_LABEL = "h1[align='center']"

    # Methods 
    # def __init__(self,browser):
    #     self.browser = browser

    def get_header(self):
        header = self.browser.find_element(self.CSS_SELECTOR,self.HEADER_LABEL)
        return header.text

    def enter_username(self,username):
        username_field = self.browser.find_element(self.CSS_SELECTOR, self.USERNAME_FIELD)
        username_field.send_keys(username)
    
    def enter_email(self,email):
        email_field = self.browser.find_element(self.CSS_SELECTOR, self.EMAIL_FIELD)
        email_field.send_keys(email)

    def enter_password(self,password):
        password_field = self.browser.find_element(self.CSS_SELECTOR, self.PASSWORD_FIELD)
        password_field.send_keys(password)

    def submit_form(self):
        submit_button = self.browser.find_element(self.CSS_SELECTOR,self.SUBMIT_BUTTON)
        submit_button.click()
               
class UserPage(BasePage):
    # Selectors
    CSS_SELECTOR = By.ID
    SUCCESS_BANNER = "flash_success"

    # Methods
    # def __init__(self,browser):
    #     self.browser = browser

    def get_banner_text(self):
        banner = self.browser.find_element(self.CSS_SELECTOR,self.SUCCESS_BANNER)
        return banner.text