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