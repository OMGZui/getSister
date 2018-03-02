x = int(input("Please enter an integer: "))


def check_num(x):
    if x < 0:
        print('负数')
    elif x == 0:
        print('零蛋')
    else:
        print('正数')


check_num(x)


def f(a, L=[]):
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))


def f1(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


print(f1(1))
print(f1(2))
print(f1(3))


# 必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


f1(1, 2)
f1(1, 2, 3, 'a', 'b', x=99)


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# lambda
f = lambda x: x + 1
print(f(1))
