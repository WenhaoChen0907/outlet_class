from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddressListPage(BaseAction):
    # 新增地址
    new_address_button = By.XPATH, "//*[@text='新增地址' and @resource-id='com.yunmall.lc:id/address_add_new_btn']"

    # 默认的收件人和电话信息
    receipt_name_text_view = By.ID, "com.yunmall.lc:id/receipt_name"

    # 默认标记
    default_button = By.ID, "com.yunmall.lc:id/address_is_default"

    # 点击 版本更新
    def click_new_address(self):
        self.click(self.new_address_button)

    # 获取 默认的收件人和电话信息 的文字内容
    def get_default_receipt_name_text(self):
        return self.get_feature_text(self.receipt_name_text_view)

    def click_default(self):
        self.click(self.default_button)

    def is_default_exist(self):
        return self.is_feature_exist(self.default_button)

