class Enemy():
    life = 5
    def attack(self):
        print("enemy is attacked")
        self.life -= 1
    def check_life_left(self):
        if self.life <= 0:
            print("Enemy is Dead!!!")
        else:
            print("life left:",str(self.life))

enemy1 = Enemy()
enemy2 = Enemy()

enemy1.attack()
enemy2.attack()
enemy1.attack()
enemy1.attack()

enemy1.check_life_left()
enemy2.check_life_left()