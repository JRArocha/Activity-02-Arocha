import random

Ptype       = str(input("\nPokemon Type: "))
CharLevel   = int(input("Charizard's Level: "))
SAtt        = int(input("Special Attack: "))
Stype       = str(input("Skill Type: "))
power       = int(input("Power: "))
FerLevel    = int(input("\nFeraligatr's Level: "))
SDef        = int(input("Special Defense: "))
Etype       = str(input("Enemy Type: "))
badge       = int(input("\nGeneration: "))
weather     = int(input("[1] Beneficial [2] Against [3] Normal \nWeather: "))
target      = int(input("Target/s: "))


def modifier (target, weather, badge, Ptype, Stype, Etype):
    
    # TARGET
    if target == 1:
        target = 1
    else:
        target = .5

    # WEATHER
    if weather == 1:
        weather = 1.5
    if weather == 2:
        weather = 0.5
    if weather == 3:
        weather = 1

    # BADGE
    if badge == 2:
        badge = 1.25
    else:
        badge = 1

    # STAB   
    if Ptype == "fire" and Stype == "fire":
        effect2 = 1.5
    else:
        effect2 = 1
    stab = effect2

    # RANDOM
    rand = [.85 , 1]
    rando = random.choice(rand)

    # CRITICAL
    crit= [1 , 2]
    critic = random.choice(crit)
    if critic == 2:
        print("\nA Critical Hit\n")
    
    # BURN
    burnn = [0.5 , 1]
    burn = random.choice(burnn)
    if burn == .5:
        print("\nThe attacker was burned")

    # OTHER
    other = 1

    # TYPE
    if Stype == "fire" and Etype == "water":
        effect = .5
    if Stype == "fire" and Etype == "fire":
        effect = .5
    if Stype == "fire" and Etype == "rock":
        effect = .5  
    if Stype == "fire" and Etype == "dragon":
        effect = .5 
    if Stype == "fire" and Etype == "normal":
        effect = 1
    if Stype == "fire" and Etype == "fighting":
        effect = 1
    if Stype == "fire" and Etype == "flying":
        effect = 1
    if Stype == "fire" and Etype == "poison":
        effect = 1
    if Stype == "fire" and Etype == "ground":
        effect = 1
    if Stype == "fire" and Etype == "ghost":
        effect = 1
    if Stype == "fire" and Etype == "electric":
        effect = 1
    if Stype == "fire" and Etype == "psychic":
        effect = 1
    if Stype == "fire" and Etype == "dark":
        effect = 1
    if Stype == "fire" and Etype == "fairy":
        effect = 1
    if Stype == "fire" and Etype == "bug":
        effect = 2
    if Stype == "fire" and Etype == "steel":
        effect = 2
    if Stype == "fire" and Etype == "grass":
        effect = 2
    if Stype == "fire" and Etype == "ice":
        effect = 2

    type = effect
    
    # ATTACK CONDITION
    if type <= .5:
        print("It's not very effective")
    if type >= 2:
        print("It's super effective")
    else:
        type == 1

    # CALCULATION FOR MODIFIER
    mod = target * weather * badge * burn * other * critic * rando * type * stab
    return mod

# CALCULATION FOR DAMAGE
damage = ((((((2*CharLevel)/5)+2)* power * SAtt / SDef)/50)+2) * modifier(target, weather, badge, Ptype, Stype, Etype)
print("Charizards Damage to Feraligatr is:", damage)