from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "what it this?" in browser.currect_url == "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/", "No login url" 
        assert True

    def should_be_login_form(self):
        self.is_element_present(*LoginPageLocators.login_form), "No autorizacion form"
        assert True

    def should_be_register_form(self):
        self.is_element_present(*LoginPageLocators.register_form), "No register form"
        assert True