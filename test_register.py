# -*- coding: utf-8 -*-
from web.WeComPO.index_page import IndexPage


class TestRegister:
    def setup(self):
        self.index = IndexPage()

    def test_register(self):
        assert self.index.goto_login().goto_register().register()