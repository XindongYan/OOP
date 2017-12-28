class Animal(object):
    def run(self):
        print('动物在奔跑...')


# 当需要编写Dog和cat时，就直接可以从Animal类继承
class Dog(Animal):
    pass


class Cat(Animal):
    pass


# 继承有什么好处？
# 最大的好处就是子类能获得父类的全部功能
dog = Dog()
dog.run()


# 可以给子类增加一些方法
class Tiger(Animal):
    # def run(self):
    #     print('老虎在奔跑...')

    def eat(self):
        print('吃肉')


# 当子类和父类都存在相同的属性，那么子类的属性就覆盖了父类的属性
# 在代码运行的时候总是会调用子类的属性，这样我们就获得了继承的另外一个好处：多态
tiger = Tiger()
tiger.run()
tiger.eat()


# 什么是多态？
# 当我们定义一个class的时候我们实际上就定义了一种数据类型
a = Animal()
b = Dog()

# 结果都为True
print(isinstance(a, Animal))
print(isinstance(b, Dog))
# 因为b是Dog的实例，而Dog又继承自Animal
print(isinstance(b, Animal))

# 则是False, 以为a是Animal
print(isinstance(a, Dog))


# 新建函数接受Animal
def run_twice(animal):
    animal.run()


# 输出”动物在奔跑“
run_twice(Animal())


# 我们在定义一个Tortoise类型，也从Animal派生
class Tortoise(Animal):
    def run(self):
        print('乌龟跑的很慢...')


# 输出”乌龟跑的很慢“
run_twice(Tortoise())