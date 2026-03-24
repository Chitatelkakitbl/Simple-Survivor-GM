import random  # used for random events and outcomes

# display current player stats
def show_status(player):
    print("\n=== STATUS ===")
    print(f"Health: {player['health']}")
    print(f"Energy: {player['energy']}")
    print(f"Day: {player['day']}")
    print("================\n")

# generates a random event when player explores
def random_event(player):
    events = [
        "enemy",
        "food",
        "nothing",
        "trap"
    ]

    event = random.choice(events)  # pick random event

    # enemy attack reduces health
    if event == "enemy":
        damage = random.randint(5, 20)
        player["health"] -= damage
        print(f"You were attacked! Lost {damage} health.")

    # finding food restores health
    elif event == "food":
        heal = random.randint(5, 15)
        player["health"] += heal
        print(f"You found food! Gained {heal} health.")

    # trap deals higher damage
    elif event == "trap":
        damage = random.randint(10, 25)
        player["health"] -= damage
        print(f"You stepped on a trap! Lost {damage} health.")

    # sometimes nothing happens
    else:
        print("Nothing happened today.")

# handles player decision each turn
def player_action(player):
    print("Choose action:")
    print("1 - Rest (+energy)")
    print("2 - Explore (random event)")
    print("3 - Hunt (risk/reward)")

    choice = input("Enter choice: ").strip()

    # resting increases energy (safe option)
    if choice == "1":
        player["energy"] += 10
        print("You rested and gained energy.")

    # exploring triggers random events
    elif choice == "2":
        player["energy"] -= 5
        random_event(player)

    # hunting is risky but can give reward
    elif choice == "3":
        player["energy"] -= 10
        if random.random() > 0.5:
            print("Successful hunt! +15 health")
            player["health"] += 15
        else:
            print("Hunt failed. You got hurt (-10 health)")
            player["health"] -= 10

    else:
        print("Invalid action.")

# main game loop
def main():
    player = {
        "health": 100,
        "energy": 50,
        "day": 1
    }

    print("=== SURVIVAL GAME ===")
    print("Survive 7 days to win.\n")

    # game continues while player is alive and days <= 7
    while player["health"] > 0 and player["day"] <= 7:
        show_status(player)

        player_action(player)

        player["day"] += 1  # move to next day

        # if energy is too low, player loses health
        if player["energy"] <= 0:
            print("You are too tired. Lost health.")
            player["health"] -= 10

    # final result
    if player["health"] > 0:
        print("\n🎉 You survived! You win!")
    else:
        print("\n💀 You died. Game over.")

# entry point of the program
if __name__ == "__main__":
    main()
