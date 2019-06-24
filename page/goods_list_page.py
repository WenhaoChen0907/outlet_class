import random

from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class GoodsListPage(BaseAction):
    # 商品详情
    goods_detail_button = By.ID, "com.yunmall.lc:id/iv_element_1"

    # 点击 商品详情
    def click_goods_detail(self):
        goods = self.find_elements(self.goods_detail_button)
        goods_count = len(goods)
        goods_index = random.randint(0, goods_count - 1)
        goods[goods_index].click()
