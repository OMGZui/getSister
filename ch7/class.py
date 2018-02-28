class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


stu = Student('张三', 98)
print(stu.name)

stu.print_score()


# 继承
class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


dog = Dog()
dog.run()

print(isinstance(dog, Animal))


# 对象信息
print(type(dog))
print(dir(dog))

# Generator Expressions
print(sum(x*y for x,y in zip([10, 20, 30], [7, 5, 3])))
