from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddressListPage(BaseAction):
    # 新增地址
    new_address_button = By.XPATH, "//*[@text='新增地址' and @resource-id='com.yunmall.lc:id/address_add_new_btn']"

    # 点击 版本更新
    def click_new_address(self):
        self.click(self.new_address_button)

        
