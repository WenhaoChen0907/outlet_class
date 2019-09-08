from selenium.webdriver.common.by import By

from base.base_analyze import analyze_data
from base.base_driver import init_driver
from page.page import Page

import pytest
# github修改
# 第一次本地修改
# 第二次本地修改

class TestLogin:

    def setup(self):
        self.driver = init_driver(False)
        self.page = Page(self.driver)

    @pytest.mark.parametrize("args", analyze_data("login_data", "test_login"))
    def test_login(self, args):
        # 获取数据
        username = args["username"]
        password = args["password"]
        toast = args["toast"]

        # 首页 - 点击 我
        self.page.home.click_me()
        # 注册 - 点击 已有账号去登陆
        self.page.register.click_login()
        # 登陆 - 输入 账户
        self.page.login.input_username(username)
        # 登陆 - 输入 密码
        self.page.login.input_password(password)
        # 登陆 - 点击 登陆
        self.page.login.click_login()

        if toast is None:
            # 断言："我"页面的用户名内容，是否和输入一致
            assert self.page.me.get_username_text() == "itheima_test"
        else:
            # 断言：toast内容是否和预期一致
            assert self.page.login.is_toast_exist(toast)


