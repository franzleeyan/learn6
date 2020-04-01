# 打印让你在2个黑暗的门前进行选择，选择1号门，或者2号门
print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

# 给门赋值，让用户进行输入
door = input("> ")

# 如果选择1号门
if door == "1":
    print("There's a giant bear here eating a chees cake.") # 打印这里有只大熊在吃芝士蛋糕
    print("What do you do?") # 打印你想怎么做
    print("1. Take the cake.") # 第一个选择拿走蛋糕
    print("2. Scream at the bear.") # 第二个选择对熊尖叫

    bear = input("> ") # 用户选择给熊的赋值选择

    if bear == "1": # 如果选择1
        print("The bear eats your face off.  Good job!")
    elif bear == "2":
        print("The bear eats your legs off.  Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powerd by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")