
#一次性读完
file = open("./data.txt", "r", encoding="utf-8")
content = file.read()
print(content)
file.close()

print("---------------------------------")

#每次读取一行
with open("./data.txt", "r", encoding="utf-8") as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())
    print(file.readline())

print("---------------------------------")

#一次性读完
with open("./data.txt", "r", encoding="utf-8") as file:
    #readlines读取每行后会自带一个换行符
    lines = file.readlines()
    for line in lines:
        print(line)