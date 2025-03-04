import characters
import uuid

char_name = input("Hero Name: ")
char_id = uuid.uuid4()
char_level = 1
char_loot = ["none"]

boss_name = input("Boss Name: ")
boss_id = uuid.uuid4()
boss_level = 1
boss_hp = 300
boss_attack_damage = 10
boss_livespan = boss_hp/300


hero = characters.hero(char_name, char_id, char_level, char_loot)
boss = characters.boss(boss_name, boss_id, boss_level, boss_hp, boss_attack_damage, boss_livespan)


print("\nHero Details:")
print(f"Name: {hero.name}")
print(f"ID: {hero.id}")
print(f"Level: {hero.level}")
print(f"Loot: {hero.loot}")

print("\nBoss Details:")
print(f"Name: {boss.name}")
print(f"ID: {boss.id}")
print(f"Level: {boss.level}")
print(f"HP: {boss.hp}")
print(f"Attack Damage: {boss.attack_damage}")
print(f"Lifespan: {boss.lifespan}")      