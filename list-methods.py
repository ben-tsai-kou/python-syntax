# number = [5, 2, 1, 7, 4]
# number.append(20) # [5, 2, 1, 7, 4, 20]
# number.insert(0, 20) # [20, 5, 2, 1, 7, 4]
# number.remove(7) # [5, 2, 1, 4]
# number.clear() # []
# number.pop() # [5, 2, 1, 7]
# print(number.index(5)) # 0
# print(5 in number) # True
# number.sort() # [1, 2, 4, 5, 7]
# # 下面這兩個要一起用
# number.sort()
# number.reverse() # [7, 5, 4, 2, 1]
# number2 = number.copy()

# print(number.count(5)) # 1
#
# print(number)

array = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []

for item in array:
    if item not in uniques:
        uniques.append(item)

print(uniques)