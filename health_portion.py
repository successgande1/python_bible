import random

import math

player_health = 50

player_difficulty = 3
portion_health = int(random.randint(25, player_health) / player_difficulty)
#print(portion_health)

player_health = player_health + portion_health

print(player_health)
