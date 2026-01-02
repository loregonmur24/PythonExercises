"""
=====================
Find the espensive book
"""

# List of books with prices
books = [('Horror', 1.63), ('Love', 2.6), ('Fiction', 1.25)]

def find_most_expensive(book_list):
    """Find the book with highest price"""
    highest_price = 0
    expensive_book = ''
    
    for book_name, book_price in book_list:
        print(f"Checking: {book_name} (${book_price})")
        
        if book_price > highest_price:
            highest_price = book_price
            expensive_book = book_name
            print(f"  → New highest price found!")
    
    return highest_price, expensive_book

# Run the function
print("📚 FINDING MOST EXPENSIVE BOOK")
print("=" * 30)

price, book = find_most_expensive(books)

print("\n" + "⭐" * 30)
print(f"RESULT: The {book} book is most expensive")
print(f"        Price: ${price}")
print("⭐" * 30)
