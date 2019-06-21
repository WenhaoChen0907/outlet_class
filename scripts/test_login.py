from base.base_driver import init_driver
from page.page import Page


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_login(self):
        # 首页 - 点击 我
        self.page.home.click_me()
        # 注册 - 点击 已有账号去登陆
        self.page.register.click_login()
        # 登陆 - 输入 账户
        self.page.login.input_username("itheima_test")
        # 登陆 - 输入 密码
        self.page.login.input_password("itheima")
        # 登陆 - 点击 登陆
        self.page.login.click_login()
        # 断言："我"页面的用户名内容，是否和输入一致
        assert self.page.me.get_username_text() == "itheima_test"