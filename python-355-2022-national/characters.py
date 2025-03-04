class Character:
  def __init__(self, name, id):
    
    self.name = name
    self.id = id

class hero(Character):
    def __init__(self, name, id, level, loot):
        super().__init__(name, id)
        self.level = level
        self.loot = loot

class boss(Character):
    def __init__(self, name, id, level, hp, attack_damage, lifespan):
        super().__init__(name, id)
        self.level = level
        self.hp = hp
        self.attack_damage = attack_damage
        self.lifespan = lifespan