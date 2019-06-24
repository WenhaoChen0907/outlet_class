import time
import allure

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddressListPage(BaseAction):
    # 新增地址
    new_address_button = By.XPATH, "//*[@text='新增地址' and @resource-id='com.yunmall.lc:id/address_add_new_btn']"

    # 默认的收件人和电话信息
    receipt_name_text_view = By.ID, "com.yunmall.lc:id/receipt_name"

    # 默认标记
    default_button = By.ID, "com.yunmall.lc:id/address_is_default"

    # 编辑
    edit_button = By.XPATH, "//*[@text='编辑']"

    # 删除
    delete_button = By.XPATH, "//*[@text='删除']"

    # 确认
    commit_button = By.XPATH, "//*[@text='确认']"

    # 点击 新建地址
    @allure.step(title="地址管理 - 点击 新建地址")
    def click_new_address(self):
        self.click(self.new_address_button)

    # 获取 默认的收件人和电话信息 的文字内容
    def get_default_receipt_name_text(self):
        return self.get_feature_text(self.receipt_name_text_view)

    @allure.step(title="地址管理 - 点击 默认地址")
    def click_default(self):
        self.click(self.default_button)

    def is_default_exist(self):
        return self.is_feature_exist(self.default_button)

    @allure.step(title="地址管理 - 删除10次 收货地址")
    def delete_all_address(self):
        for i in range(10):
            try:
                self.delete_item()
            except TimeoutException:
                # 删除完了
                return
            time.sleep(1)

    # 删除第一个收货地址
    def delete_item(self):
        self.click_edit()
        self.click_delete()
        self.click_commit()

    # 点击 编辑
    @allure.step(title="地址管理 - 点击 编辑")
    def click_edit(self):
        self.click(self.edit_button)

    # 点击 删除
    @allure.step(title="地址管理 - 点击 删除")
    def click_delete(self):
        self.click(self.delete_button)

    # 点击 确认
    @allure.step(title="地址管理 - 点击 确认")
    def click_commit(self):
        self.click(self.commit_button)



