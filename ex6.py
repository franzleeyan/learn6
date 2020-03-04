type_of_people = 10
x = f"There are {type_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}")

hilarious = False
joke_evaluation = "Isn't that joke so funny? {}!"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side"

print(w + e)

# 巩固练习
# 增加注释

# 设定用户类型数量
type_of_people = 10
# 定义这里有多少个用户类型的文本
x = f"There are {type_of_people} types of people."

# 定义二进制的名称
binary = "binary"
# 不知道的定义名词
do_not = "don't"
# 知道二进制的人和不知道二进制的人文本
y = f"Those who know {binary} and those who {do_not}."

# 打印x值
print(x)
# 打印y值
print(y)

# 打印我说的x值
print(f"I said: {x}")
# 打印我还说的y值
print(f"I also said: '{y}")

# 定义这不是一个搞笑的说法
hilarious = True
# 笑话评级
joke_evaluation = "Isn't that joke so funny? {}!"
# 打印笑话的效果
print(joke_evaluation.format(hilarious))

# 定义w文本
w = "This is the left side of..."
# 定义e文本
e = "a string with a right side"

# 打印文本w和e
print(w + e)