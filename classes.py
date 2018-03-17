class Enemy():

    def __init__(self):
        self.life = 5
        self.freq = 0
    def attack(self,lost):
        print("enemy is attacked")
        self.life  -=  lost
        self.freq += 1
    def check_life_left(self):
        if self.life <= 0:
            print("Enemy is Dead!!!")
        else:
            print("life left:",str(self.life),' attack freq : ',str(self.freq))

enemy1 = Enemy()
enemy2 = Enemy()

enemy1.attack(1)
enemy2.attack(2)
enemy1.attack(3)

enemy1.check_life_left()
enemy2.check_life_left()