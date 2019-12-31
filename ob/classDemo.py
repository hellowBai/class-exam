class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def showInfo(self):
        print("name=%s,age=%s"%(self.name,self.__age))
    def getAge(self,age):
        if age<0and age>150:
            self.__age=age
        else:
            print("please check your data")


class Car:
    def __init__(self,brand,color,type):
        self.brand=brand
        self.color=color
        self.type=type

class Animal:
    def __init__(self,type,name,color):
        self.type=type
        self.name=name
        self.__color=color
    def eat(self):
        print('animal'+':'+self.name+"  "+"eat...")

class Proctected:
    def pro(self):
        print("Protected")

class Dog(Animal,Proctected):
    def showInfo(self):
        print(self.type)
        print(self.name)
    def eat(self):
        print('dog'+':'+self.name+"  "+"eat...")#多态
d=Dog('dog','JULY','red')
d.showInfo()
d.pro()
d.eat()