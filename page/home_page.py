import time

from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):

    # 我
    me_button = By.ID, "com.yunmall.lc:id/tab_me"

    # 分类
    category_button = By.ID, "com.yunmall.lc:id/tab_category"

    # 点击 我
    def click_me(self):
        self.click(self.me_button)

    # 点击 分类
    def click_category(self):
        self.click(self.category_button)

    # 如果没有登录，则登录
    def login_if_not(self, page):
        # 1.判断登录状态
        # 1.1 点击我
        page.home.click_me()
        time.sleep(1)
        # 1.2 如果当前的页面是"注册页面"，认为没有登录
        if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.LogonActivity":
            return

        # 注册 - 点击 已有账号去登陆
        page.register.click_login()
        # 登陆 - 输入 账户
        page.login.input_username("itheima_test")
        # 登陆 - 输入 密码
        page.login.input_password("itheima")
        # 登陆 - 点击 登陆
        page.login.click_login()




        # 如果没有登录则登录
        # 如果已经登录则什么都不做
