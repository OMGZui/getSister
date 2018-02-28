fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

print(fruits.count('apple'))
print(fruits.index('apple'))

fruits.reverse()
print(fruits)

fruits.sort()
print(fruits)

print(fruits.pop())

# lambda 匿名函数
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)
print(list(map(lambda x: x**2, range(10))))
# list comprehension 列表生成式
print([x**2 for x in range(10)])

# nested 嵌套
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print([[row[i] for row in matrix] for i in range(4)])

print(list(zip(*matrix)))


# tuple
print((0, 1, 2, 3, 4, 5)[:3])

# 切片
print((0, 1, 2, 3, 4, 5)[::2])

# dict to list
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])