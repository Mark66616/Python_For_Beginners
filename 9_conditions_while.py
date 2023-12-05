# 计算平均值
total = 0
count = 0
result = 0

out_put = input("请输入数字（完成数字输入后，输入q结束）:")

while out_put != "q":
    num = float(out_put)
    total += num
    count += 1
    out_put = input("请输入数字（完成数字输入后，输入q结束）:")

if (count == 0):
    result = 0
else:
    result = total / count

print("您输入数字的平均数是：" + str(result))
