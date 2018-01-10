
import copy
dict = {"a":"apple", "b":{"g":"grape", "o":"orange"}}
dict2 = copy.deepcopy(dict)
dict3 = copy.copy(dict)
dict2["b"]["g"] = "2grape"
print(dict)
dict3["b"]["g"] = "3grape"
print(dict)

origin = [1,2, [3, 4]]
cop1 = copy.copy(origin)
cop2 = copy.deepcopy(origin)
print(cop1 == cop2)
print(cop1 is cop2)
origin[2][0] = "hey!"
print(origin)
print(cop1)
print(cop2)