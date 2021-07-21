import random

foods = [
    "番茄汤冒菜",
    "蛋炒饭",
    "亲爱的麻辣烫",
    "烤肉饭",
    "皮蛋瘦肉粥",
    "炒河粉",
    "螺蛳粉",
    "螺蛳粉+奶茶",
    "番茄汤冒菜+奶茶",
    "蛋炒饭+奶茶",
    "亲爱的麻辣烫+奶茶",
    "烤肉饭+奶茶",
    "炒河粉+奶茶",
]


milk_tea = 0  # 喝奶茶次数
spicyfood = 0  # 辛辣食物次数
delete_foods = []  # 即将被删除的食物
print("规则：\n 1. 一周不能喝两次奶茶\n 2. 一周不能吃两次螺蛳粉\n")
for i in range(0, 5):
    random_food = foods[random.randint(0, len(foods) - 1)]
    print("今天第 {} 天".format(i + 1))
    print("您今天吃 {}".format(random_food))
    if "奶茶" in random_food:
        milk_tea += 1
    if "螺蛳粉" in random_food:
        spicyfood += 1
    foods.remove(random_food)
    if milk_tea == 2:
        for j in range(0, len(foods)):
            if "奶茶" in foods[j]:
                delete_foods.append(foods[j])
        for delete_food in delete_foods:
            foods.remove(delete_food)
        delete_foods.clear()

    if spicyfood == 1 and random_food == "螺蛳粉" and milk_tea != 2:
        foods.remove("螺蛳粉+奶茶")
    if spicyfood == 1 and random_food == "螺蛳粉+奶茶":
        foods.remove("螺蛳粉")
