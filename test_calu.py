# -*- coding: utf-8 -*-

'''
补全计算器中加法和除法的测试用例
使用参数化完成测试用例的自动生成
在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
'''
import pytest
import yaml

from python_code.python_calu import Calculator


def test_a():
    print("普通测试a")
#读取yaml文件
with open("./datas/cala.yaml") as f:
    datas = yaml.safe_load(f)['add']
    add_datas = datas['AddDatas']
    add_id = datas['AddIds']
    div_datas = datas['DivDatas']
    div_id = datas['DivIds']
class TestCalu():
    # 实例化计算器
    def setup_class(self):
        self.calu = Calculator()

    # 结束测试
    def teardown_class(self):
        print("测试结束")

    def setup(self):
        print("【开始计算】")

    def teardown(self):
        print("【计算结束】")
    @pytest.mark.parametrize(
       "a, b, expect",
       add_datas, ids=add_id
   )


   #加法计算
    def test_add(self,a, b, expect):
        #实例化计算器
        #calu = Calculator()
        #调用add方法
        result = self.calu.add(a, b)
        #判断result是浮点数，保留两位小数
        if isinstance(result,float):
            result = round(result,2)
        assert result == expect

    @pytest.mark.parametrize(
        "a, b, expect",
        div_datas, ids=div_id
    )
    def test_div(self,a, b, expect):
        #调用div方法
        result = self.calu.div(a, b)
        #判断除数是否为0
        if b == 0:
            print('除数不能为0')

        assert result == expect
