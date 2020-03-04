my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_wight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_wight} pounds heavy")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_wight
print(f"If I add {my_age}, {my_height}, and {my_wight} I get {total}.")


# 巩固练习
# 1.移除my_
# 2.使用变量将原来的英寸和磅换成厘米和千克，使用python的数学计算功能完成
name = 'Zed A. Shaw'
age = 35 # not a lie
height = round(74 * 2.54) # cm
wight = round(180 * 0.4535924) # kg
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print("This is new massage.")
print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {wight} pounds heavy")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + wight
print(f"If I add {age}, {height}, and {wight} I get {total}.")
