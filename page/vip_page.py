import time

from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class VipPage(BaseAction):

    # 邀请码
    invite_code_edit_text = By.XPATH, "//input[@type='tel']"

    # 立即成为会员
    be_vip_button = By.XPATH, "//input[@value='立即成为会员']"

    # 输入 邀请码
    def input_invite_code(self, value):
        self.input(self.invite_code_edit_text, value)

    # 点击 立即成为会员
    def click_be_vip(self):
        self.click(self.be_vip_button)

    def is_can_not_be_vip(self, value):
        """
        如果不能成为vip，邀请码错误，返回True
        :return:
        """
        timeout = 5
        end_time = time.time() + timeout
        while True:
            res = value in self.driver.page_source
            if res:
                assert True
                break
            else:
                print("暂时没找到")

            if time.time() > end_time:
                print("超时，没有找到")
                break

            time.sleep(0.5)
