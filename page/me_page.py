from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MePage(BaseAction):

    # 用户名 特征
    username_feature = By.ID, "com.yunmall.lc:id/tv_user_nikename"

    # 设置 按钮
    setting_button = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"

    # 获取 用户名
    def get_username_text(self):
        return self.get_feature_text(self.username_feature)

    # 点击 设置
    def click_setting(self):
        self.click(self.setting_button)
