from base.base_driver import init_driver
from page.page import Page


class TestAddress:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_add_address(self):
        # 首页 - 如果没有登录，则登录，并停留在 "我" 的页面
        self.page.home.login_if_not(self.page)
        # 我 - 点击 设置
        self.page.me.click_setting()
        # 设置 - 点击 地址管理
        self.page.setting.click_address_list()
        # 地址管理 - 点击 新增地址
        self.page.address_list.click_new_address()
        # 新增地址 - 输入 收件人
        self.page.edit_address.input_name("zhangsan")
        # 新增地址 - 输入 手机号
        self.page.edit_address.input_phone("18888888888")
        # 新增地址 - 输入 详细地址
        self.page.edit_address.input_detail("2单元 302")
        # 新增地址 - 输入 邮编
        self.page.edit_address.input_postal_code("100000")
        # 新增地址 - 点击 所在地区
        self.page.edit_address.click_region()
        # 新增地址 - 选择区域
        region_text = self.page.region.choose_region()
        # 新增地址 - 点击 设为默认地址
        self.page.edit_address.click_default()

        # 新增地址 - 点击 保存
        self.page.edit_address.click_save()

        # 点击进入编辑收货地址的页面，根据每一项内容进行断言
        self.page.address_list.click_default()
        # 断言：收件人的内容和输入的收件人的内容是否一致
        assert self.page.edit_address.get_name_text() == "zhangsan"
        # 断言：手机号的内容和输入的手机号的内容是否一致
        assert self.page.edit_address.get_phone_text() == "18888888888"
        # 断言：详细地址的内容和输入的详细地址的内容是否一致
        assert self.page.edit_address.get_detail_text() == "2单元 302"
        # 断言：邮编的内容和输入的邮编的内容是否一致
        assert self.page.edit_address.get_postal_code_text() == "100000"
        # 断言：所在区域的内容和随机点击的所在区域的内容是否一致
        assert self.page.edit_address.get_region_text() == region_text

        # # 断言：保存后的手机号和收件人，时候和输入的一致
        # assert self.page.address_list.get_default_receipt_name_text() == "%s  %s" % ("zhangsan", "18888888888")
