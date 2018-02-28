
# file
try:
    f = open('../README.md', 'r')
    print(f.read())
finally:
    if f:
        f.close()


with open('../README.md', 'r') as f:
    print(f.read())


# json
import json
print(json.dumps([1, 'simple', 'list']))

# os
import os
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
