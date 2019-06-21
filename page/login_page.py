from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):
    # 登陆
    login_button = By.ID, "com.yunmall.lc:id/logon_button"

    # 账号
    username_edit_text = By.ID, "com.yunmall.lc:id/logon_account_textview"

    # 密码
    password_edit_text = By.ID, "com.yunmall.lc:id/logon_password_textview"

    # 点击 登陆
    def click_login(self):
        self.click(self.login_button)

    # 输入 账号
    def input_username(self, value):
        self.input(self.username_edit_text, value)

    # 输入 密码
    def input_password(self, value):
        self.input(self.password_edit_text, value)
