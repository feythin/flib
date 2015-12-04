# -*- coding: utf-8 -*-
"""
单例模式：
在应用这个模式时，单例对象的类必须保证只有一个实例存在。
对于缓存，数据库连接，网络请求队列等资源消耗比较大得，通常我们只是需要一个实例来减少资源的消耗。
"""
class Singleton(object):
    __instance = None

    def __new__(classtype, *args, **kwargs):
        if classtype != type(classtype.__instance):
            classtype.__instance = object.__new__(classtype, *args, **kwargs)
            classtype.__instance.init()

        return classtype.__instance

    def init(self):
        pass
if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()
    if(id(s1) == id(s2)):
        print "Same"
    else:
        print "Different"
