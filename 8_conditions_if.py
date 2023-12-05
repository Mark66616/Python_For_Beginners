#if条件判断
happy_num = int(input("你今天心情数值为："))

if happy_num >= 60:
    print("开心")
elif happy_num < 50 and happy_num <60:
    print("有点不开心")
else:
    print("不开心")
