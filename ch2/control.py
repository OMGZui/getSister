# if
x = int(input("Please enter an integer: "))

if x < 0:
    print('负数')
elif x == 0:
    print('零蛋')
else:
    print('正数')

# for
words = ['cat', 'window', 'defenestrate']

for w in words:
    print(w, len(w))

# range
print(list(range(10)))

# break
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '=', x, '*', n // x)
            break
    else:
        print(n, '是一个素数')

# continue
for num in range(2, 10):
    if num % 2 == 0:
        print(num, '偶数')
        continue
    print(num, '奇数')

# pass
