my_list = [1,2,10,3,4,4]
print(my_list)

my_list.append(5)
print(my_list)

my_list.extend([6,7,8])
print(my_list)

my_list.insert(2, 9)
print(my_list)

my_list.remove(9)
print(my_list)

popping = my_list.pop(7)
print(my_list, "removing element is ;", popping)

counting = my_list.count(4)
print(counting)

my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)

length = len(my_list)
print(length)

maximum = max(my_list)
print(maximum)

checking = 3 not in my_list
print(checking)


print(my_list)
getting = my_list.index(3)