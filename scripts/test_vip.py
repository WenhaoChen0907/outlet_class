import time

from selenium.webdriver.support.wait import WebDriverWait

from base.base_analyze import analyze_data
from base.base_driver import init_driver
from page.page import Page


import pytest


class TestVip:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    @pytest.mark.parametrize("args", analyze_data("vip_data", "test_vip"))
    def test_vip(self, args):
        # 解析的数据
        invite_code = args["invite_code"]
        toast = args["toast"]

        # 首页 - 如果没有登录，则登录，并停留在 "我" 的页面
        self.page.home.login_if_not(self.page)
        # 我 - 点击 加入超级Vip
        self.page.me.click_vip()

        # 加入超级Vip 是一个 webview 需要切换环境
        self.driver.switch_to.context("WEBVIEW_com.yunmall.lc")

        # vip - 输入 邀请码
        self.page.vip.input_invite_code(invite_code)
        # vip - 点击 成为会员
        self.page.vip.click_be_vip()

        assert self.page.vip.is_can_not_be_vip(toast)


        # assert WebDriverWait("邀请码输入不正确", 10, 1).until(lambda x: x in self.driver.page_source)

        # assert "邀请码输入不正确" in self.driver.page_source

        # 切换回原生的环境
        self.driver.switch_to.context("NATIVE_APP")


