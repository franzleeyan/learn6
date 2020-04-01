# exit用于结束程序
from sys import exit


# global = how_much
def gold_room():
    # 进入黄金房间的选择逻辑
    global how_much
    print("This room is full of gold.   How much do you take?")

    choice = input("> ")  # 输入选择
    if choice.isdigit():  # 判断是否为数字
        # if "0" in choice or "1" in choice:
        how_much: int = int(choice)  # 赋值输入的数量
    else:
        dead("Man, learn to type a number.")  # 如果不是数字则死亡

    if how_much < 50:  # 输入的数字小于50，则提示你赢了
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:  # 否则就死了
        dead("You greedy bastard!")


# 进入熊房间的逻辑
def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of anther door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


# 进入克苏鲁房间的逻辑
def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head.")

    choide = input("> ")

    if "flee" in choide:
        start()
    elif "head" in choide:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


# 惨死函数
def dead(why):
    print(why, "Good job!")
    exit(0)


# 启动函数--开始的房间
def start():
    # 你在一个黑暗的房间
    print("You are in a dark room.")
    # 门在你的左侧和右侧
    print("There is a door to your right and left.")
    # 开始你的选择
    print("Which one do you take?")

    # 输入你的选择
    choice = input("> ")

    # 如果选择左侧 进入熊房间
    if choice == "left":
        bear_room()
    # 如果选择右侧 进入克苏鲁房间
    elif choice == "right":
        cthulhu_room()
    # 否则就是死
    else:
        dead("You stumble around the room until you starve.")


start()
