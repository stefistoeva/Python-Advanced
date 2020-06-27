def is_valid(bombs):
    return bombs["Cherry Bombs"] >= 3 and bombs["Datura Bombs"] >= 3 and bombs["Smoke Decoy Bombs"] >= 3


bombs = {
    "Cherry Bombs": 0,
    "Datura Bombs": 0,
    "Smoke Decoy Bombs": 0,
}

bomb_effects = input().split(", ")
bomb_casing = input().split(", ")

while bomb_effects and bomb_casing:
    effects = int(bomb_effects.pop(0))
    casing = int(bomb_casing.pop())
    if effects + casing == 40:
        bombs["Datura Bombs"] += 1
    elif effects + casing == 60:
        bombs["Cherry Bombs"] += 1
    elif effects + casing == 120:
        bombs["Smoke Decoy Bombs"] += 1
    else:
        casing -= 5
        bomb_effects.insert(0, effects)
        bomb_casing.append(casing)

    if is_valid(bombs):
        break

if is_valid(bombs):
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if not bomb_effects:
    print("Bomb Effects: empty")
else:
    result = ", ".join(bomb_effects)
    print(f"Bomb Effects: {result}")
if not bomb_casing:
    print("Bomb Casings: empty")
else:
    result = ", ".join(bomb_casing)
    print(f"Bomb Casings: {result}")
[print(f"{key}: {value}") for key, value in bombs.items()]
