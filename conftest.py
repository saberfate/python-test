# -*- coding: utf-8 -*-
import pytest

from python_code.python_calu import Calculator


@pytest.fixture(scope="class")
def get_calu():
    print("获取计算器")
    calu = Calculator()
    return calu