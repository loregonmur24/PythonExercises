"""
LEARN BY DOING - TEXT ANALYZER
==============================
"""

print("LEARN PYTHON - TEXT ANALYZER")
print("=" * 40)

# Lesson 1: Getting input
print("\n📝 LESSON 1: GETTING TEXT")
print("The input() function gets text from user:")
user_text = input("Try typing your name: ")
print(f"Hello {user_text}! You typed: '{user_text}'")

# Lesson 2: Counting letters
print("\n📝 LESSON 2: COUNTING LETTERS")
print("The count() method counts letters:")

sample = "banana"
letter_to_count = "a"
result = sample.count(letter_to_count)

print(f"In '{sample}', the letter '{letter_to_count}' appears {result} times")

# Lesson 3: Splitting words
print("\n📝 LESSON 3: SPLITTING WORDS")
print("The split() method divides text into words:")

sample_sentence = "Python is fun"
words_list = sample_sentence.split()

print(f"Sentence: '{sample_sentence}'")
print(f"Words: {words_list}")
print(f"Number of words: {len(words_list)}")

# Now you try!
print("\n" + "=" * 40)
print("NOW YOU TRY!")
print("=" * 40)

your_text = input("Write a sentence: ")
print(f"\nYour sentence: '{your_text}'")
print(f"It has {len(your_text)} characters")

words = your_text.split()
print(f"It has {len(words)} words")

if your_text:
    print(f"First character: '{your_text[0]}'")
    print(f"Last character: '{your_text[-1]}'")

print("\nGreat job! You're learning Python! 🎉")
