"""
写一个计算BMI的函数，函数名为calculate_BMI。
1,可以计算任意体重和身高的BMI值
2.执行过程中打印一句话，"您的BMT分类为：Xx”
3.返回计算出的BMI值

BMI=体重/（身高**2）

BMI分类
偏瘦：BMI<=18.5
正常：18.5<BMI<=25
偏胖：25<BMI<=30
肥胖：BMI>30
"""

def caculate_bmi(weight, height):
    BMI =  weight / (height ** 2)
    if BMI <= 18.5:
        category = "偏瘦"
    elif BMI <= 25:
        category = "正常"
    elif BMI <= 30:
        category = "偏胖"
    else:
        category = "肥胖"
    print(f"您的BMI分类为：{category}")
    return BMI

weight = float(input("您的体重为："))
height = float(input("您的身高为："))

bmi_result = caculate_bmi(weight, height)
print(f"您的BMI值为：{bmi_result}")