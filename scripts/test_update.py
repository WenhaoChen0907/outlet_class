from base.base_driver import init_driver
from page.page import Page


class TestUpdate:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_update(self):
        # 首页 - 如果没有登录，则登录，并停留在 "我" 的页面
        self.page.home.login_if_not(self.page)
        # 我 - 点击 设置
        self.page.me.click_setting()
        # 设置 - 点击 关于百年奥莱
        self.page.setting.click_about()
        # 关于 - 点击 版本更新
        self.page.about.click_update()
        # 断言：toast是不是 "当前已是最新版本"
        assert self.page.about.is_toast_exist("当前已是最新版本")
