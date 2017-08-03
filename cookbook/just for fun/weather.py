#-*-coding:utf-8-*-
'''
    观察者模式
'''

class Subject:
    '''
    主题对象接口
    '''
    def registerObserver(self,observer):
        pass
    def removeObserver(self,observer):
        pass
    def notifyObserver(self):
        pass
class Observer:
    '''
    观察者对象
    '''
    def update(self,temp,humidity,pressure):
        pass

class DisplayElement:
    '''
    显示接口   
    为什么不把他写在观察者接口里面？（是因为观察者对象不一定会实现display方法吗？）
    '''
    def display(self):
        pass

class weatherData(Subject):
    def __init__(self,temp,humidity,pressure):
        self.observers = []
        self.temperature = temp
        self.humidity = humidity
        self.pressure = pressure
    
    def registerObserver(self,observer):
        self.observers.append(observer)

    def removeObserver(self,observer):
        print(self.observers.index(observer))
        if observer in self.observers:
            index = self.observers.index(observer)
            del self.observers[index]
        
    def notifyObservers(self):
        for item in self.observers:
            item.update(self.temperature,self.humidity,self.pressure)
    def measurementChanged(self):
        self.notifyObserver()

class normalObserver(Observer):
    def __init__(self,name):
        self.name = name    
    def update(self,temp,humidity,pressure):
        print("This is {0} ~~~{1}".format(self.name,temp))

web = weatherData(12,34.434,32.43)

obs1 = normalObserver('luoxiao')
obs2 = normalObserver('jiayu')
# 可以把注册方法写到观察者的构造函数里面，这样观察者一生成就加入了主题对象，不用一个个写
web.registerObserver(obs1)
web.registerObserver(obs2)

web.notifyObservers()

web.removeObserver(obs2)

web.notifyObservers()