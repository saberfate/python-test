# -*- coding: utf-8 -*-
'''
比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
创建子类【猫】，继承【动物类】，
重写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发 = 短毛，
添加一个新的方法， 会捉老鼠，
重写父类的【会叫】的方法，改成【喵喵叫】
'''
from animal import Animal


class Cat(Animal):
    def __init__(self, name, color, age, gender):
        self.hair = "短毛"
        super().__init__(name, color, age, gender)

    def cat_move(self):
        print(f"{self.name}会捉老鼠")

    def animal_call(self):
        print(f"{self.name}会喵喵叫")

if __name__ == '__main__':
    cat = Cat('波斯猫','black',10,'female')
    print(cat.hair)
    cat.cat_move()
    cat.animal_call()
