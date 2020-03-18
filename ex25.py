# 从sys导入argv模块,是脚本调用时接受2个参数
from sys import argv
# 两个参数是脚本名和文件名字
script, filename = argv

# 提示用户输入年龄,并存储在变量age中
print("How old are you?", end=' ')
age = input()
# 提示用户输入身高,并存储在变量height中
print("How tall are you?", end=' ')
height = input()
# 提示用户输入体重，并存储在变量weight中
print("How much do you weigh?", end=' ')
weight = input()
# 使用字符串格式化打印前三个用户输入的信息变量
print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# 把文件对象保存在变量txt中
txt = open(filename)
# 字符串格式化打印文件名字
print(f"Here's your file {filename}:")
# 使用read方法读取文件内容并打印返回的字符串
print(txt.read())

# 打印语句提示用户再次输入文件名
print("Type the filename again:")
# 使用input接受用户输入的文件名，保存在file_again变量中
file_again = input("> ")
# 把新输入的文件对象保存在变量txt_again中
txt_again = open(file_again)
# 使用read方法读取文件内容并打印返回的字符串
print(txt_again.read())

# 打印语句
print('Let\'s practice everything.')
# 介绍转义字符的用法，打印转义符本身和转行、制表符、单引号
print('You\'d need to know \'bout escapes\
      with \\ that do \n newlines and \t tabs.')

# 把固定格式的字符串存入变量poem中
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
# 打印poem变量里面的字符，前后用----间隔
print("--------------")
print(poem)
print("--------------")

# 把表达式的结果存在变量five中
five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

# 定义函数secret_formula，需要一个形象并且返回三个值
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars - 100
    return jelly_beans, jars, crates
# 给变量start_point赋值为10000
start_point = 10000
# 调用函数secret_formula，并用三个变量接受函数的三个返回值
beans, jars, crates = secret_formula(start_point)

# 两种字符串格式化格式
# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

# 把变量start_point除以10，然后传递给函数，将返回值元组存储在变量formula中并打印
start_point = start_point / 10
print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



people = 20
cats = 30
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!")

if people < cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")
