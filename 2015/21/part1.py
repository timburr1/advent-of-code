
player_hp = 100
boss_hp = 100
boss_dmg = 8
boss_armor = 2

def buy(coins):
    return

def battle(player_hp, player_dmg, player_armor, boss_hp, boss_dmg, boss_armor):
    while True:
        boss_hp -= max(player_dmg - boss_armor, 1)
        # print('Player deals ' + str(player_dmg - boss_armor) + ' damage; boss goes to ' + str(boss_hp))
        if boss_hp <= 0:
            return True
        player_hp -= max(boss_dmg - player_armor, 1)
        # print('Boss deals ' + str(boss_dmg - player_armor) + ' damage; player goes to ' + str(player_hp))
        if player_hp <= 0:
            return False

print(battle(player_hp, 4, 1, boss_hp, boss_dmg, boss_armor))
assert(battle(8, 5, 5, 12, 7, 2), True)