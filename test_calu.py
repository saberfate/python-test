# -*- coding: utf-8 -*-

'''
补全计算器中加法和除法的测试用例
使用参数化完成测试用例的自动生成
在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
'''
import allure
import pytest
import yaml

from python_code.python_calu import Calculator


#读取yaml文件
with open("./datas/cala.yaml") as f:
    datas = yaml.safe_load(f)['add']
    add_datas = datas['AddDatas']
    add_id = datas['AddIds']
    div_datas = datas['DivDatas']
    div_id = datas['DivIds']
    sub_datas = datas['SubDatas']
    sub_id = datas['SubIds']
    mul_datas = datas['MulDatas']
    mul_id = datas['MulIds']

@pytest.fixture(params=add_datas, ids=add_id)
def get_add_datas(request):
    print("开始加法计算")
    add_data = request.param
    yield add_data
    print("结束加法计算")

@pytest.fixture(params=div_datas, ids=div_id)
def get_div_datas(request):
    print("开始除法计算")
    div_data = request.param
    yield div_data
    print("结束除法计算")

@pytest.fixture(params=sub_datas, ids=sub_id)
def get_sub_datas(request):
    print("开始减法计算")
    sub_data = request.param
    yield sub_data
    print("结束减法计算")

@pytest.fixture(params=mul_datas, ids=mul_id)
def get_mul_datas(request):
    print("开始乘法计算")
    mul_data = request.param
    yield mul_data
    print("结束乘法计算")


@allure.feature("测试计算器")
class TestCalu():


   #加法计算
    @allure.story("测试加法")
    def test_add(self,get_calu,get_add_datas):
        #实例化计算器
        #calu = Calculator()
        #调用add方法
        with allure.step("测试两者之和"):
            result = get_calu.add(get_add_datas[0], get_add_datas[1])
        #判断result是浮点数，保留两位小数
        if isinstance(result,float):
            result = round(result,2)
        assert result == get_add_datas[2]

    #除法计算
    @allure.story("测试除法")
    def test_div(self, get_calu, get_div_datas):
        #调用div方法
        with allure.step("测试两者之商"):
            result = get_calu.div(get_div_datas[0], get_div_datas[1])
        #判断除数是否为0
        if get_div_datas[1] == 0:
            print('除数不能为0')

        assert result == get_div_datas[2]

    #测试减法
    @allure.story("测试减法")
    def test_sub(self,get_calu,get_sub_datas):
        #实例化计算器
        #calu = Calculator()
        #调用add方法
        with allure.step("测试两者之差"):
            result = get_calu.sub(get_sub_datas[0], get_sub_datas[1])
        #判断result是浮点数，保留两位小数
        if isinstance(result,float):
            result = round(result,2)
        assert result == get_sub_datas[2]

    @allure.story("测试乘法")
    def test_mul(self,get_calu,get_mul_datas):
        #实例化计算器
        #calu = Calculator()
        #调用add方法
        with allure.step("测试两者之积"):
            result = get_calu.mul(get_mul_datas[0], get_mul_datas[1])
        #判断result是浮点数，保留两位小数
        if isinstance(result,float):
            result = round(result,2)
        assert result == get_mul_datas[2]

