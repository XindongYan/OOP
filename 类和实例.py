class Student(object):
    pass


class Teacher(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

bart = Student()
bart.name = 'Bob'

tea = Teacher('Lisa', '59')

# 打印出类在内存中的地址
print(bart)
# 打印出name属性的值
print(bart.name)

# 打印出Teacher类中的name属性
print(tea.name)