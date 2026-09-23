# users = [
#     {
#         "name":"张三",
#         "age":17
#     },
#     {
#         "name":"李四",
#         "age":20
#     },
#     {
#         "name":"王五",
#         "age":25
#     }
# ]
# for user in users:
#     if user["age"]>=18:
#         print(user["name"]+"已成年")

name = input("请输入你的名字：")
age = int(input("请输入你的年龄："))

print("你好，我是"+ name)
print("我今年"+str(age)+"岁")