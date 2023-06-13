import random
import os
import time

start_battle = None
battle_count = 0  # Add a counter to keep track of the number of battles

# Rolls a number between (1-sides)
def diceRoll(sides):
    roll = random.randint(1, sides)
    return roll

# Generates player stats
def charGen():
    base = diceRoll(6) * diceRoll(12) / 2
    type = random.choice(["Imp", "Human", "Wizard", "Ork"])
    health = base + 10
    strength = base + 12
    return health, strength, type

player1_name = input("Player 1 Name > ")
player1_health, player1_strength, player1_type = charGen()
player1_initial_health = player1_health  # Store initial health
print()
print(f"{player1_name}'s Stats: ")
print(f"TYPE: {player1_type}")
print(f"HP: {player1_health}")
print(f"STR: {player1_strength}")
print("")

player2_name = input("Player 2 Name > ")
player2_health, player2_strength, player2_type = charGen()
player2_initial_health = player2_health  # Store initial health
print()
print(f"{player2_name}'s Stats: ")
print(f"TYPE: {player2_type}")
print(f"HP: {player2_health}")
print(f"STR: {player2_strength}")

attack_strength = abs(player1_strength - player2_strength) + 1
print("")
start_battle = input("Commence the battle? ")
os.system("clear")
print("⚔️  BATTLE TIME ⚔️")
time.sleep(2)

# Determines which player rolled higher
while start_battle == "yes" or start_battle == "Yes":
    os.system("clear")
    battle_count += 1  # Increment the battle counter
    
    player1_roll = diceRoll(6)
    player2_roll = diceRoll(6)

    if battle_count == 2:
        print("⚔️  THE BATTLE CONTINUES ⚔️")
        time.sleep(1)  # Wait for 3 seconds
        
    os.system("clear")

    if player1_roll > player2_roll:
        print(f"{player1_name} struck swiftly with their sword!")
        print("")
        player2_health -= attack_strength
        if player2_health <= 0:
            print(f"⚔️ {player1_name} won the battle in {battle_count} rounds!⚔️")
            break
        print(f"{player1_name}")
        print(f"HP: {player1_health} / {player1_initial_health}")
        print("")
        print(f"{player2_name}")
        print(f"HP: {player2_health} / {player2_initial_health}")

    elif player1_roll < player2_roll:
        print(f"{player2_name} cast a powerful spell!")
        print("")
        player1_health -= attack_strength
        if player1_health <= 0:
            print(f"⚔️   {player2_name} won the battle in {battle_count} rounds!  ⚔️")
            break
        print(f"{player1_name}")
        print(f"HP: {player1_health} / {player1_initial_health}")
        print("")
        print(f"{player2_name}")
        print(f"HP: {player2_health} / {player2_initial_health}")

    elif player1_roll == player2_roll:
        print("They attacked at the same time!")

    time.sleep(4)  # Delay between each attack
