# 既然Student实例本身就拥有这些数据，要访问这些数据，就没必要从外面的函数去访问
# 可以直接在Student类的内部定义和访问这些数据的函数,这样，就把”数据“给封装起来了


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


stu = Student('Bob', 93)
stu.print_score()

print(stu.get_grade())