from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class GoodsDetailPage(BaseAction):
    # 加入购物车
    add_shop_cart_button = By.XPATH, "//*[@text='加入购物车']"

    # 确认
    commit_button = By.XPATH, "//*[@text='确认']"

    # 点击 版本更新
    def click_add_shop_cart(self):
        self.click(self.add_shop_cart_button)

    # 点击 确认
    def click_commit(self):
        self.click(self.commit_button)

    # # 获取待选择的规格
    # def get_choose_spec(self):
    #     if self.is_toast_exist("请选择"):
    #         toast_text = self.get_toast_text("请选择")
    #         return toast_text.split(" ")[1]

    # 选择所有应该选择的规格
    def choose_spec(self):
        while True:
            self.click_commit()

            if self.is_toast_exist("请选择"):
                toast_text = self.get_toast_text("请选择")
                choose_spec_text = toast_text.split(" ")[1]

                xpath = By.XPATH, "//*[@text='%s']/../*[2]/*[1]" % choose_spec_text
                self.find_element(xpath).click()
            else:
                break


