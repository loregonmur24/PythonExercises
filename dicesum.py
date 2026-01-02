# Dice Game - Interactive
import random

print("=" * 25)
print("🎮 DICE ROLL GAME")
print("=" * 25)

print("\nPress Enter to roll dice...")
input()

# Roll dice
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

print(f"\n🎲 You rolled: {dice1} and {dice2}")
print(f"🎯 Total: {dice1 + dice2}")

# Show dice faces (fun!)
dice_faces = {
    1: "[ • ]",
    2: "[• •]",
    3: "[• •\n • ]",
    4: "[• •\n• •]",
    5: "[• •\n • \n• •]",
    6: "[• • •\n• • •]"
}

print(f"\nDice 1: {dice_faces[dice1]}")
print(f"Dice 2: {dice_faces[dice2]}")

# Result message
total = dice1 + dice2
if total <= 6:
    print("\nResult: Not your lucky roll 😞")
elif total < 10:
    print("\nResult: Good chances! 😊")
else:
    print("\nResult: EXCELLENT! 🎉🎉")

# Play again?
play = input("\nRoll again? (y/n): ").lower()
if play == 'y':
    print("\n" + "🔄" * 10)
    print("NEW ROLL!")
    print("🔄" * 10)
    
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(f"\nNew roll: {dice1} and {dice2}")
    print(f"New total: {dice1 + dice2}")

print("\nThanks for playing! 🎲")
