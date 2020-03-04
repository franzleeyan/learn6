# 赋值车数量
i = 100
# 赋值车内空间
x = 4.0
# 赋值司机数量
j = 30
# 赋值乘客数量
y = 90

# 乘客数量
cars = i
# 车内空间
space_in_a_car = x
# 司机数量
drivers = j
# 乘客数量
passengers = y
# 不在使用的车数量=
cars_not_driven = cars - drivers
# 使用的车数量
cars_driven = drivers
# 拼车容量
carpool_capacity = cars_driven * space_in_a_car
# 平均拼车容量
average_passengers_per_car = passengers / cars_driven


# 这里有多少可以使用的车
print("There are", cars,"cars available.")
# 这里只有多少司机可以用
print("There are only", drivers, "drivers available.")
# 今天将有多少空车
print("There will be", cars_not_driven, "empty cars today.")
# 今天我们将能运输多少乘客
print("We can transport", carpool_capacity, "people today.")
# 今天我们停车场将有多少乘客
print("We have", passengers, "to carpool today.")
# 我们每辆车的平均载客量是多少
print("We need to put about", average_passengers_per_car, "in each car.")