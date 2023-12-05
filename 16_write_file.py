with open("./poem.txt", "w", encoding = "utf-8") as file:
    file.write("我欲乘风归去，\n")
    file.write("又恐琼楼玉宇，\n")
    file.write("高处不胜寒。\n")

with open("./poem.txt", "a", encoding = "utf-8") as file:
    file.write("起舞弄清影，\n")
    file.write("何似在人间。")