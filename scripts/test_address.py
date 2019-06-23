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
        self.page.region.choose_region()
        # 新增地址 - 点击 设为默认地址
        self.page.edit_address.click_default()

        # 新增地址 - 点击 保存
        self.page.edit_address.click_save()

        # 断言：保存后的手机号和收件人，时候和输入的一致
        assert self.page.address_list.get_default_receipt_name_text() == "%s  %s" % ("zhangsan", "18888888888")
