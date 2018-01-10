print("%s, %(a)s, %(b)s" % {"a":"apple", "b":"banana"})
dict = {"a":"apple", "b":"banana", "g":"grape", "o":"orange"}
dict["w"] = "watermelon"
del(dict["a"])
dict["g"] = "grapefruit"
print(dict.pop("b"))
print(dict)
for k in dict:
    print("dict[%s] =" % k, dict[k])
print(dict.items())

D = {"key1":"value1", "key2":"value2"}
E = {"key2":"value2", "key3":"value3"}
if "key1" in D:
    print(D["key1"])
else:
    print("None")

dict1 = {}
dict1.setdefault("a")
print(dict1)

print(sorted(dict.items(), key=lambda d: d[0]))
E = D.copy()
print(E)
D["key2"] = "value2_D"
E["key2"] = "value2_E"
print(E)


