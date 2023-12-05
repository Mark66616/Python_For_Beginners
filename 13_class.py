class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.grades = {"语文": 0, "数学": 0, "英语": 0}

    def setGrades(self, course, grade):
        if course in self.grades:
            self.grades[course] = grade
        else:
            print(f"您修改的科目[{course}]不存在")

    def print_grades(self):
        print(f"学生{self.name}(学号：{self.id})的成绩为：")
        for course in self.grades:
            print(f"{course}:{self.grades[course]}")

zhangsan = Student("张三","250")
zhangsan.setGrades("语文",10)
zhangsan.setGrades("数学",10)
zhangsan.setGrades("英语",10)
zhangsan.print_grades()
zhangsan.setGrades("英语1",10)

