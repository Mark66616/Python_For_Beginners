# BMI公式：体重/(身高**2)
weight = float(input("请输入您的体重（单位：kg）:"))
height = float(input("请输入您的身高（单位：m）:"))
bmi = weight / (height ** 2)
print("您的BMI为：" + str(bmi))

"""
结果：
请输入您的体重（单位：kg）:66
请输入您的身高（单位：m）:1.7
您的BMI为：22.837370242214536
"""