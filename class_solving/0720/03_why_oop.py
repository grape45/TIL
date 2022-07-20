# # 우리편 야스오
# yasuo_2_hp = 100
# # 상대편 야스오
# yasuo_1_hp = 100

class Yasuo:

    def __init__(self):
        self.health = 100
        self.energy = 0

yasuo1 = Yasuo()
yasuo2 = Yasuo()

yasuo1.health = yasuo1.health - 20

print(yasuo1.health, yasuo2.health)