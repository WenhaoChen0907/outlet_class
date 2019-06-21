from base.base_driver import init_driver


class TestHello:

    def setup(self):
        self.driver = init_driver()

    def test_hello(self):
        print("123")
