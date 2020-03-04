# 打开argv模块
from sys import argv
# 定义模块脚本
script, filename = argv
# 打开文件
txt = open(filename)
# 显示文件的文件的名称
print(f"Here 's your file {filename}:")
# 显示文件内容
print(txt.read())
# 巩固练习添加close()状态
print(txt.close())

# 再次键入显示的文件名称
print("Type the filename again:")
# 输入提示符
file_again = input("> ")
# 再次打开该文件
txt_again = open(file_again)
# 再次显示文件的内容
print(txt_again.read())
# 巩固练习添加close()状态
print(txt_again.close())
