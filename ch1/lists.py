# lists
lists = [1, 4, 9, 16, 25]
# 相同
print(lists)
print(lists[:])

print(lists[0]) # 1
print(lists[-1]) # 25
print(lists[0:3]) # [1,4,9]

# +运算
lists = lists + [36, 49, 65, 81, 100]
print(lists)

# 赋值
lists[7] = 64  # replace the 65
print(lists)

# 新增
lists.append(121)
print(lists) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]

# 置空
lists_empty = lists
lists_empty[:] = []
print(lists_empty) # []

# 嵌套
lists = [['a', 'b', 'c'], [1, 2, 3]]
print(lists[0][1]) # b