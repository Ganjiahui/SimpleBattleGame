import random

class People:
    def __init__(self, name, hp, lv):
        self.name = name
        self.hp = hp
        self.lv = lv

    def get_name(self):
        return self.name
    
    def get_hp(self):
        return self.hp
    
    def get_lv(self):
        return self.lv
    
    def hit_damage(self):
        damage = 0
        if self.lv < 100 and self.lv >= 75:
            damage = 60
        elif self.lv < 15 and  self.lv >= 1:
            damage = 10
        elif self.lv < 30 and  self.lv >= 15:
            damage = 20
        elif self.lv < 45 and  self.lv >= 30:
            damage = 30
        elif self.lv < 60 and self.lv >=  45:
            damage = 40
        elif self.lv < 75 and self.lv >=  60:
            damage = 50
        else:
            damage = 100 
        return damage
    
    def attack_devil(self, devil):
        damage = self.hit_damage()
        devil.take_damage(damage)
        print(f"{self.name} attacks Devil for {damage} damage.")

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print(f"{self.name} has been defeated.")
        else:
            print(f"{self.name} takes {damage} damage. {self.name}'s HP: {self.hp}")

class Devil:
    def __init__(self):
        self.hp = 100
        self.lv = random.randint(1, 100)

    def get_hp(self):
        return self.hp

    def get_lv(self):
        return self.lv
    
    def hit_damage(self):
        damage = 0
        if self.lv < 100 and self.lv >= 75:
            damage = 60
        elif self.lv < 15 and  self.lv >= 1:
            damage = 10
        elif self.lv < 30 and  self.lv >= 15:
            damage = 20
        elif self.lv < 45 and  self.lv >= 30:
            damage = 30
        elif self.lv < 60 and self.lv >=  45:
            damage = 40
        elif self.lv < 75 and self.lv >=  60:
            damage = 50
        else:
            damage = 100 
        return damage
    
    def attack_player(self, player):
        damage = self.hit_damage()
        player.take_damage(damage)
        print(f"Devil attacks {player.get_name()} for {damage} damage.")

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print("Devil has been defeated.")
        else:
            print(f"Devil takes {damage} damage. Devil's HP: {self.hp}")

# player information
player_name = input("Enter player name: ")
player_hp = int(input("Enter player HP: "))
player_lv = int(input("Enter player LV: "))

# Create player
player = People(player_name, player_hp, player_lv)
print(f"\n{player.get_name()} - HP: {player.get_hp()}, LV: {player.get_lv()}")

# Create devil
devil = Devil()
print(f"\nDevil - HP: {devil.get_hp()}, LV: {devil.get_lv()}")

print("\n======= Battle Start =======")
while player.get_hp() > 0 and devil.get_hp() > 0:
    print("\n--- Player's Turn ---")
    player.attack_devil(devil)
    if devil.get_hp() <= 0:
        break
    print("\n--- Devil's Turn ---")
    devil.attack_player(player)
    if player.get_hp() <= 0:
        break
