
# dict
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Bob'])
print(d.get('Bob2','不存在'))

# 特点  dict是用空间来换取时间的一种方法。
# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。

# set 不重复
s = set([1, 1, 2, 2, 3, 3])
print(s)

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
# 交集
print(s1 & s2)
# 并集
print(s1 | s2)
