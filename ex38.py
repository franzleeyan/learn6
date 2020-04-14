# 定义ten_things 物品的数量以及名称
ten_things = "Apples Oranges Crows Teltphone Light Sugar"


# 打印我们需要10个道具，但这里没有10个，要修复这个问题
print("Wait there are not 10 things in that list. Let's fix that.")
# print(ten_things)

# 以空格为分隔符，分解字符串中的子串，返回一个列表
stuff = ten_things.split(' ')

# 定义一个列表，更多的物品
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]

# 打印列表
# print(stuff)

# 循环，当列表元素不等于10的时候
while len(stuff) != 10:
    next_one = more_stuff.pop()  # 从更多的物品列表中最后一个删除，并返回
    print("Adding: ", next_one)  # 加入的物品名称
    stuff.append(next_one)  # 将删除的物品加入到最初的10个物品末尾，并返回
    print(f"The stuff are {len(stuff)} item now.")  # 打印我们的物品中现在有几个
    print(f"The more_stuff are {len(more_stuff)} item now.")  # 打印更多的物品中现在有几个

print("There we go: ", stuff)  # 打印我们现在有的物品

print("Let's do some things with stuff.")

# 打印物品的第2个元素
print(stuff[1])
# 打印列表最后1个元素
print(stuff[-1])  # whoa! fancy
# 打印删除列表的最后一个元素
print(stuff.pop())
# 用空格字符连接列表中的元素
print(' '.join(stuff))  # what? cool!
# 用#连接列表的第四和第五个元素
print('#'.join(stuff[3:5]))  # spuer stellar!
