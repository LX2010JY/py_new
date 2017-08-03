#-*-coding:utf-8-*-
#'''当学习编程有了功利心，能达到的高度也就那样了'''
#'''Python本身没有任何机制阻止你干坏事，一切全靠自觉。'''
class Duck:
    '''
        你好，这里是鸭子类
        这里 实现共有的功能，将有区别的，分离出去
    '''
    def __init__(self):
        self.flyBehavior = None
        self.quackBehavior = None
    #定义飞行行为和呱呱叫行为 ，以便于可以修改这两种行为
    def setFlyBehavior(self,flyBehavior):
        self.flyBehavior = flyBehavior
    def setquackBehavior(self,quackBehavior):
        self.quackBehavior = quackBehavior

    def PerformFly(self):
        self.flyBehavior.fly()
    def PerformQuack(self):
        self.quackBehavior.quack()
    def display(self):
        print("I'm just a duck")
        self.PerformFly()
        self.PerformQuack()


# 飞行类接口 TODO python怎么实现接口、抽象类 ？我不知道，所以这里是继承，能使用多态就好
class flyBehavior:
    '''
        你好，这里是鸭子飞类
    '''
    def fly(self):
        pass
class flyWithWing(flyBehavior):
    def fly(self):
        print("I fly with wing")
class flyNoWay(flyBehavior):
    def fly(self):
        print("sorry ,I can't fly")
class flyWithRock(flyBehavior):
    def fly(self):
        print("I fly with rock")


class quackBehavior:
    '''
        你好，这里是鸭子叫类
    '''
    def quack(self):
        pass
class quackWithGG(quackBehavior):
    def quack(self):
        print("quack : Gua 、Gua、Gua")
class quackNoWay(quackBehavior):
    def quack(self):
        print("............................")



# 现世实例 小黄鸭~~~可以飞 不会叫
class LittleYellowDuck(Duck):
    def __init__(self):
        self.flyBehavior = flyWithWing()
        self.quackBehavior = quackWithGG()
    

if __name__ == "__main__":
    duck = LittleYellowDuck()
    duck.display()
    # 策略模式？？？
    duck.setFlyBehavior(flyWithRock())
    duck.display()