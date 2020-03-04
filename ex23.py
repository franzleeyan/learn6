# coding=utf-8
# 导入参数，argv的前面都学过，稍微有点不一样，但是结果都一样；
import sys
import io

scirpt, encoding, error = sys.argv


# 定义主函数  main  ，内有三个形参
def main(language_file, encoding, errors):
    # 读取文件中的一行文本，并赋值给line，注意language_file是main主函数的实参
    line = language_file.readline()
    '''
    if语句，用来检测line中是否为真值，如果为真，则执行下面2行代码，如果为假，则跳过不执行；
    所以如果readling()返回包含东西，则继续执行下面2行，如果返回为null，则不执行，这是为了防止死循环；
    '''
    if line:
        # 在主函数main内调用了另外一个函数 print_line
        print_line(line, encoding, errors)
        # 这个return是让我们在主函数main内又调用一次main，看上去不可能，实际上就是跳到main顶端在运行一次；
        return main(language_file, encoding, errors)


# 定义 print_line 函数，内有3个形参，这个函数的作用就是对languages.txt里的每一行进行编码
def print_line(line, encoding, errors):
    # .strip()的作用删掉每行结尾的\n
    next_lang = line.strip()
    # .encode()的作用：把每一行字符串编码成字节串bytes
    raw_bytes = next_lang.encode(encoding, errors = errors)
    # .decode()的作用：把每一行字节串解码成字符串string
    cooked_string = raw_bytes.decode(encoding, errors = errors)

    # 打印： ”字节串 <===> 字符串“
    print(raw_bytes, "<==>", cooked_string)


# 把languages.txt文件以utf-8的编码方式打开
languages = io.open("languages.txt", encoding = "utf-8")

main(languages, encoding, error)