# 购物列表
shopping_list = []
# 添加商品
shopping_list.append("主板")
shopping_list.append("cpu")
shopping_list.append("显卡")
shopping_list.append("散热")
shopping_list.append("固态")
shopping_list.append("内存")
shopping_list.append("风扇")
shopping_list.append("无线网卡")
shopping_list.append("音响")
# 删除商品
shopping_list.remove("音响")
# 改变商品
shopping_list[7] = "10米六类网线"

print(shopping_list)
print(str(len(shopping_list)) + "件商品")

#价格表
price_list = [233,3245,333,111]
max_pirce = max(price_list)
min_price = min(price_list)
sort_price = sorted(price_list)
print(max_pirce)
print(min_price)
print(sort_price)