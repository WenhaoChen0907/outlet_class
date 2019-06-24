import random

from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class CategoryPage(BaseAction):
    # 商品列表的元素的特征
    goods_list_button = By.ID, "com.yunmall.lc:id/iv_img"

    # 点击 商品列表的元素的特征
    def click_goods_list(self):
        goods = self.find_elements(self.goods_list_button)
        goods_count = len(goods)
        goods_index = random.randint(0, goods_count - 1)
        goods[goods_index].click()
