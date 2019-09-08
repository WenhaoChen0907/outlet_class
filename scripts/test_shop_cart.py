from selenium.webdriver.common.by import By

from base.base_driver import init_driver
from page.page import Page
# 第二次本地修改


class TestShopCart:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_add_shop_cart(self):
        # 首页 - 如果没有登录，则登录，并停留在 "我" 的页面
        self.page.home.login_if_not(self.page)
        # 首页 - 点击 分类
        self.page.home.click_category()
        # 分类 - 点击 物品列表
        self.page.category.click_goods_list()
        # 物品列表 - 点击 物品详情
        self.page.goods_list.click_goods_detail()

        # 记录商品的名字
        product_title = self.page.goods_detail.get_product_title_text()

        # 物品详情 - 点击 加入购物车
        self.page.goods_detail.click_add_shop_cart()

        # 选择规格
        self.page.goods_detail.choose_spec()
        # 点击购物车
        self.page.goods_detail.click_shop_cart()

        # 断言：点击到购物车之后，是否存在该商品
        assert self.page.goods_detail.is_product_title_exist(product_title)

        # assert self.page.goods_detail.is_toast_exist("成功加入购物车")

