f1 = open("hello2.txt")
while True:
    line = f1.readline(2)
    if line:
        print(line)
    else:
        break
f1.close()

# 使用readlines()读文件
f2 = open("hello2.txt")
lines = f2.readlines()
for line in lines:
    print(line)
f2.close()


import os
li = os.listdir(".")
print(li)
if "hello.txt" in li:
    os.rename("hello.txt", "hi.txt")
elif "hi.txt" in li:
    os.rename("hi.txt", "hello.txt")