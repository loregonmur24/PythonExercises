"""
====================================
You can enter your own numbers!
"""

def get_numbers_from_user():
    """Ask user to enter numbers"""
    print("Enter numbers separated by commas")
    print("Example: 1, 8, 15, 7, 6, 8, 12, 54")
    
    user_input = input("\nYour numbers: ")
    
    # Convert input to list of numbers
    try:
        numbers = [float(num.strip()) for num in user_input.split(",")]
        return numbers
    except:
        print("Please enter valid numbers like: 1, 2, 3")
        return []

def simple_average_calculator(numbers):
    """Main calculator function"""
    if not numbers:
        print("No numbers to calculate!")
        return
    
    print("\n" + "=" * 40)
    print("CALCULATION STEPS:")
    print("=" * 40)
    
    print(f"\n1. Your numbers: {numbers}")
    
    # Remove duplicates
    unique_nums = list(set(numbers))
    print(f"2. Without duplicates: {unique_nums}")
    
    # Sort numbers
    unique_nums.sort()
    print(f"3. Sorted: {unique_nums}")
    
    # Remove largest if we have at least 2 numbers
    if len(unique_nums) > 1:
        removed = unique_nums.pop()
        print(f"4. Removed largest ({removed})")
        print(f"5. Numbers for average: {unique_nums}")
    else:
        print("4. Need at least 2 different numbers!")
        return
    
    # Calculate average
    total = sum(unique_nums)
    count = len(unique_nums)
    average = total / count
    
    print(f"\n6. Sum: {total}")
    print(f"7. Count: {count}")
    print(f"8. Average = {total} ÷ {count}")
    
    return average

# Main program
print("=" * 40)
print("WELCOME TO AVERAGE CALCULATOR")
print("=" * 40)

# Use default numbers or user input
choice = input("\nUse default numbers? (y/n): ").lower()

if choice == 'y':
    numbers = [1, 8, 15, 7, 6, 8, 12, 54]
else:
    numbers = get_numbers_from_user()

# Calculate and show result
if numbers:
    result = simple_average_calculator(numbers)
    
    if result is not None:
        print("\n" + "=" * 40)
        print(f"FINAL AVERAGE: {result:.2f}")
        print("=" * 40)

print("\nThank you for using the calculator! 😊")
