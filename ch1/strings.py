# \ 转义字符 以下两种方式相同
print('doesn\'t')
print("doesn't")

# """多行表达式
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# + 字符串拼接
print('py' + 'thon') # python
word = 'python'
# 字符串切割

#  +---+---+---+---+---+---+
#  | p | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1

print(word[1]) # y
print(word[-1]) # n
# 相同
print(word[0:2]) # py
print(word[:2]) # py

print(len(word)) # 6
