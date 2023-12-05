import math

# 数学计算，一元二次方程

a = -1
b = 2
c = 3

upResult = (-b + math.sqrt((b ** 2 - 4 * a * c))) / 2 * a
lowResult = (-b - math.sqrt((b ** 2 - 4 * a * c))) / 2 * a

print(upResult)
print(lowResult)
