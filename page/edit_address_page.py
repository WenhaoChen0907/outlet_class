from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class EditAddressPage(BaseAction):
    # 收件人
    name_edit_text = By.ID, "com.yunmall.lc:id/address_receipt_name"

    # 手机号
    phone_edit_text = By.ID, "com.yunmall.lc:id/address_add_phone"

    # 详细地址
    detail_edit_text = By.ID, "com.yunmall.lc:id/address_detail_addr_info"

    # 邮编
    postal_code_edit_text = By.ID, "com.yunmall.lc:id/address_post_code"

    # 设为默认地址
    default_button = By.ID, "com.yunmall.lc:id/address_default"

    # 所在地区
    region_button = By.ID, "com.yunmall.lc:id/address_province"

    # 保存
    save_button = By.XPATH, "//*[@resource-id='com.yunmall.lc:id/button_send' and @text='保存']"

    # 输入 收件人
    def input_name(self, value):
        self.input(self.name_edit_text, value)

    # 输入 手机号
    def input_phone(self, value):
        self.input(self.phone_edit_text, value)

    # 输入 详细地址
    def input_detail(self, value):
        self.input(self.detail_edit_text, value)

    # 输入 邮编
    def input_postal_code(self, value):
        self.input(self.postal_code_edit_text, value)

    # 点击 设为默认地址
    def click_default(self):
        self.click(self.default_button)

    # 点击 所在区域
    def click_region(self):
        self.click(self.region_button)

    # 点击 保存
    def click_save(self):
        self.click(self.save_button)

    # 获取 收件人 的文字内容
    def get_name_text(self):
        return self.get_feature_text(self.name_edit_text)

    # 获取 手机号 的文字内容
    def get_phone_text(self):
        return self.get_feature_text(self.phone_edit_text)

    # 获取 详细地址 的文字内容
    def get_detail_text(self):
        return self.get_feature_text(self.detail_edit_text)

    # 获取 收件人 的文字内容
    def get_postal_code_text(self):
        text = self.get_feature_text(self.postal_code_edit_text)
        if text == "可选填":
            text = ""
        return text

    # 获取 所在区域 的文字内容
    def get_region_text(self):
        return self.get_feature_text(self.region_button)


