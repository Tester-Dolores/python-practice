import random
import time
from pprint import pprint

limit_time = 20
current_time = time.time()
print("游戏开始！当前时间：{}\n".format(time.asctime(time.localtime(current_time))))

animals_weight = [100, 200]
rooms = []
for i in range(0, 10):
    weight = animals_weight[random.randint(0, len(animals_weight) - 1)]
    if weight == 100:
        animal = "sheep"
    if weight == 200:
        animal = "tiger"
    rooms.append({"weight": weight, "animal": animal})
while True:
    random_room = random.randint(0, 9)
    print("房间号：{}".format(random_room + 1))
    choose_01 = input("请选择敲门还是喂食。\n a.敲门 b.喂食\n")
    if choose_01 == "a":
        if rooms[random_room]["animal"] == "tiger":
            print("Wow!! I am tiger\n")
        if rooms[random_room]["animal"] == "sheep":
            print("mie~~I am sheep\n")
        rooms[random_room]["weight"] -= 5
    elif choose_01 == "b":
        choose_02 = input("请选择肉（请输入“meat”）或者草（请输入“grass”）。\n")
        if choose_02 == "meat":
            if rooms[random_room]["animal"] == "tiger":
                rooms[random_room]["weight"] += 10
            else:
                rooms[random_room]["weight"] -= 10
        elif choose_02 == "grass":
            if rooms[random_room]["animal"] == "sheep":
                rooms[random_room]["weight"] += 10
            else:
                rooms[random_room]["weight"] -= 10
        else:
            print("【ERROR】指令错误!!!!!!\n")
    else:
        print("【ERROR】指令错误!!!!!!\n")
    game_ing_time = time.time() - current_time
    if game_ing_time > limit_time:
        break
    else:
        print("【Warning】 游戏时间还剩下{}s\n".format(int(limit_time - game_ing_time)))
pprint(rooms)
print("游戏结束！当前时间：{}\n".format(time.asctime(time.localtime(time.time()))))
