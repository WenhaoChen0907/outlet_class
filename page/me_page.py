import time

from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MePage(BaseAction):

    # 用户名 特征
    username_feature = By.ID, "com.yunmall.lc:id/tv_user_nikename"

    # 设置 按钮
    setting_button = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"

    # 加入超级VIP
    vip_button = By.XPATH, "//*[@resource-id='com.yunmall.lc:id/tv_my_shop_text' and @text='加入超级VIP']"

    # 获取 用户名
    def get_username_text(self):
        return self.get_feature_text(self.username_feature)

    # 点击 设置
    def click_setting(self):
        self.click(self.setting_button)

    # 点击 加入超级VIP
    def click_vip(self):
        self.find_element_with_scroll(self.vip_button).click()
        time.sleep(2)
