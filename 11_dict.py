# 字典
# key:value形式
slang_dict = {"小明": "177****2097"
    , "小名": "177****2098"
    , "小花": "177****2099"}

slang_dict["张三"] = "177****1099"

query = input("请输入谁的手机号码：")
if query in slang_dict:
    print("您查询的手机号为:" + slang_dict[query])
else:
    print("未查询到该号码")
    print("通讯录当前有：" + str(len(slang_dict)))
