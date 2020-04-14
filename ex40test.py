# 导入一个库
import random
from urllib.request import urlopen
import sys

# 作者随意准备的词汇，并输出词汇
WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

# 代码及描述中的'函数方法/属性'function/attribute，'参数'parameters，'类名'，'实例名/对象'
PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef__init__(self.***)":
        "class %%% has-a __int__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self,@@@)":
        "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, call it whit params self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and it do '***'."
}

# do they want to drill phrases first
# 由答题者选择是根要根据描述编码还是根据代码描述
if len(sys.argv) == 2 and sys.argv[1] == 'english':
    PHRASES_FIRST = True
else:
    PHRASES_FIRST = False

# load up the words from the website
# 将词汇们载入到列表WORD中
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))


# 定义覆盖描述及代码中预留位置的函数，参数为片段、描述
# 最后返回一个列表results
# 先将预留放置词汇的位置分类
# 参数为key或者value，两个总是相对的
def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        # 参数的个数为1-3个随机
        param_count = random.randint(1, 3)
        # 随机到几个参数就从WORDS中获取几个词
        param_names.append(', '.join(
            random.sample(WORDS, param_count)))

    # 准备好要进行替换的PHRASES
    for sentence in snippet, phrase:
        result = sentence[:]
        # result = [snippet, phrase]
        # fake class names 类的名字
        for word in class_names:
            result = result.replace("%%%", word, 1) # 最后一位参数规定每次替换一个，保证%%%不重复。

        # fake other names 对象、方法和其他
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists 参数名
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results


# keep going until they hit CTRL-D
# 保持输入知道输入CTRL-D
try:
    while True:# 循环抽题
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)# 随机打乱顺序

        for snippet in snippets:# 抽题
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASES_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"ANSWER:  {answer}\n\n")
except EOFError:
    print("\nBye")
