# 8.3类的属性
class Fruit():
    price = 0 # 定义公有类属性price

    def __init__(self):
        self.color = "red" # 定义公有的实例属性，前缀用self声明
        zone = "China" # 定义局部变量zone，不能被实例化对象使用

if __name__ == "__main__":
    print(Fruit.price) # 输出类属性price的值
    apple = Fruit() # 实例化Fruit类，生成对象apple
    print(apple.color) # 输出实例对象apple的实例属性color
    Fruit.price += 10 # 类属性price值自加10
    print("apple的价格是：" + str(apple.price)) # 输出对象apple的属性price
    banana = Fruit()
    print("banana的价格是：" + str(banana.price))

# 类的私有方法和公有方法
class Fruit1():
    price = 0

    def __init__(self):
        self.__color = "red"

    def getColor(self):
        print(self.__color)

    @staticmethod
    def getPrice():
        print(Fruit1.price)

    def __getPrice():
        Fruit1.price = Fruit1.price + 10
        print(Fruit1.price)

    count = staticmethod(__getPrice)

if __name__ == "__main__":
    apple = Fruit1()
    apple.getColor() # 使用实例调用静态方法
    Fruit1.count() # 使用类名调用静态方法
    banana = Fruit1()
    Fruit1.count()
    Fruit1.getPrice()


