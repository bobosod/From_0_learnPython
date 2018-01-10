# 字符串对齐
word = "version3.0"
# center(width)返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
print(word.center(20))
print(word.center(20, "*"))
# ljust(width)返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
print(word.ljust(0))
# rjust(width)返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
print(word.rjust(20))
print("%30s" % word)

# 字符串连接后将分配新空间给连接后的字符串
str1 = "a"
print(id(str1))
print(id(str1+"b"))

# 通过列表的reverse()函数实现反转
def reverse(s):
    li = list(s)
    li.reverse()
    s = "".join(li)
    return s
print(reverse("Hello"))

# 字符串时间转换
import time, datetime
print(time.strftime("%Y-%m-%d %X", time.localtime()))

# re模块
import re
s = "HELLO WORLD"
print(re.findall(r"^hello", s))
print(re.findall(r"^hello", s, re.I))
print(re.findall("WORLD$", s))
s1 = "hello world"
print(id(s1))
print(id(re.sub("hello", "hi", s1)))

# compile()函数
s2 = "1abc23def45"
p = re.compile(r"\d+")
print(p.findall(s2))
print(p.pattern)

# 分组
p1 = re.compile(r"(abc)\1")
m = p1.match("abcabcabc")
print(m.group(0))
print(m.group(1))
print(m.group())
