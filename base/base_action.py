from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10, poll=1):
        """
        根据元组的feature在timeout时间之内每poll秒照一次，找到对应的一个元素
        :param feature: 元素的特征
        :param timeout: 超时时间
        :param poll: 频率
        :return: 元素
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*feature))
        # return self.driver.find_element(*feature)

    def find_elements(self, feature, timeout=10, poll=1):
        """
        根据元组的feature在timeout时间之内每poll秒照一次，找到对应的一组元素
        :param feature: 元素的特征
        :param timeout: 超时时间
        :param poll: 频率
        :return: 元素
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*feature))

    def click(self, feature):
        """
        根据特征，点击元素
        :param feature: 特征
        :return:
        """
        self.find_element(feature).click()

    def input(self, feature, value):
        """
        根据特征，先清空，再输入文字
        :param feature: 特征
        :param value: 文字
        :return:
        """
        self.clear(feature)
        self.find_element(feature).send_keys(value)

    def clear(self, feature):
        """
        根据特征，清空
        :param feature: 特征
        :return:
        """
        self.find_element(feature).clear()

    def get_feature_text(self, feature):
        """
        根据元素的特征，获取元素的文字内容
        :param feature: 元素的特征
        :return: 元素的文字内容
        """
        if self.is_feature_exist(feature):
            return self.find_element(feature).text
        else:
            raise Exception("没有找到，对应的feature的元素，请检查。")

    def is_feature_exist(self, feature):
        """
        根据元素的特征，判断这个元素是否存在
        :param feature: 元素的特征
        :return: 是否存在
        """
        try:
            self.find_element(feature)
            return True
        except TimeoutException:
            return False

    def get_toast_text(self, message):
        """
        根据toast的部分消息，获取全部的toast的文字内容
        :param message: 部分消息
        :return: 全部的toast的文字内容
        """
        toast_feature = By.XPATH, "//*[contains(@text,'%s')]" % message
        if self.is_feature_exist(toast_feature):
            return self.find_element(toast_feature).text
        else:
            raise Exception("没有找到，对应的toast内容，请检查。")

    def is_toast_exist(self, message):
        """
        根据toast的部分消息，判断toast是否存在
        :param message: 部分消息
        :return: 是否存在
        """
        toast_feature = By.XPATH, "//*[contains(@text,'%s')]" % message
        return self.is_feature_exist(toast_feature)