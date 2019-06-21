from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SettingPage(BaseAction):

    # 关于百年奥莱
    about_button = By.XPATH, "//*[@text='关于百年奥莱']"

    # 清理缓存
    cache_button = By.XPATH, "//*[@text='清理缓存']"

    # 点击 关于百年奥莱
    def click_about(self):
        self.find_element_with_scroll(self.about_button).click()

    # 点击 清理缓存
    def click_cache(self):
        self.find_element_with_scroll(self.cache_button).click()
