# 定义奶酪量和饼干盒的函数
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # 打印你有多少奶酪
    print(f"You have {cheese_count} cheeses!")
    # 打印你有多少饼干
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    # 男人足以参加一个聚会
    print("Man that's enough for a party!")
    # 盖好毯子
    print("Get a blanket.\n")

# 我们可以直接给出函数编号
print("We can just give the function numbers directly:")
# 奶酪和饼干的变量是20，30
cheese_and_crackers(20, 30)

# 或者我们可以使用脚本中的变量
print("OR, we can use variables from our script:")
# 奶酪的变量是10
amount_of_cheese = 10
# 饼干的变量是50
amount_of_crackers = 50

# 定义奶酪和饼干函数(奶酪数量，饼干数量)
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# 我们甚至可以在内部进行数学运算
print("We can even do math inside too:")
# 奶酪和饼干，分别是 10+20，5+6
cheese_and_crackers(10 + 20, 5 + 6)

# 打印 我们可以将变量和数学结合起来
print("And we can combine the two, variables and math:")
# 奶酪量 + 100，饼干量 + 1000
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# 巩固练习：自己编写一个函数出来，然后用10种不同的方式运行这个函数
# 定义参加聚会的人数和椅子
def Partypeople_and_Chair(partypeople_count,Chair_count):
    print(f"If you have {partypeople_count} Party Peoples.")
    print(f"You must have {Chair_count} chairs.")
    print("The party had to be held.")
    print("Enjoy of the party!\n")
# 打印你有多少就需要有多少椅子(直接给出函数变量)
print("We can just give the function numbers directly:")
Partypeople_and_Chair(20, 20)

# 使用脚本中的变量
print("OR, we can use variables from our script:")
amount_of_Partypeople = 30
amount_of_Chair = 30
Partypeople_and_Chair(amount_of_Partypeople, amount_of_Chair)

# 打印你增加多少人后的总参加人数，需要的总椅子数量（内部数学运算）
print("We can even do math inside too:")
Partypeople_and_Chair(20 + 20, 20 + 20)

# 打印你有多少聚会的人，和多少椅子（变量和数学结合）
print("And we can combine the two, variables and math:")
Partypeople_and_Chair(amount_of_Partypeople + 200, amount_of_Chair + 200)

# 打印输出的数量
print("We can also print out the number of inputs:")
amount_of_Partypeople = int(input())
amount_of_Chair = int(input())
Partypeople_and_Chair(amount_of_Partypeople, amount_of_Chair)
