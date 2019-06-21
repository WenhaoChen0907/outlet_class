from base.base_driver import init_driver
from page.page import Page


class TestCache:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_cache(self):
        # 首页 - 如果没有登录，则登录，并停留在 "我" 的页面
        self.page.home.login_if_not(self.page)
        # 我 - 点击 设置
        self.page.me.click_setting()
        # 设置 - 点击 清理缓存
        self.page.setting.click_cache()
        # 断言：toast的内容包含 "清理成功"
        assert self.page.setting.is_toast_exist("清理成功")