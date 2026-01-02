# Hello World - Game Version
print("=" * 30)
print("🎮 HELLO WORLD GAME")
print("=" * 30)

# 1. Show message
message = "Hello World!"
print(f"\nOur message: {message}")

# 2. Play with message
print("\n🔤 LET'S PLAY!")
print(f"Uppercase: {message.upper()}")
print(f"Lowercase: {message.lower()}")
print(f"Backwards: {message[::-1]}")

# 3. Guess the message
print("\n TRY TO GUESS!")
secret = "python is fun"
guess = input("Guess the secret message: ")

if guess.lower() == secret:
    print("✅ Correct! You win!")
else:
    print(f"❌ Try again! It was: {secret}")

print("\nThanks for playing! 🎉")
