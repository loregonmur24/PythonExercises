"""
PROGRAM: Date Manager
DESCRIPTION: A simple application to store, retrieve, and manage dates associated with names.
             Data is persistently stored in a JSON file.
"""

# Import the json module for working with JSON files
import json

# Import the datetime module for date validation (enhancement)
from datetime import datetime

# Define the filename for persistent storage
DATE_FILE = 'dates.json'

def save_dates(dates_dict):
    """
    Save the dates dictionary to a JSON file.
    
    Parameters:
    dates_dict (dict): Dictionary with names as keys and dates as values
    
    Raises:
    PermissionError: If the program doesn't have write permissions
    IOError: If there's a disk I/O error
    """
    try:
        # Step 1: Open the file in write mode ('w')
        with open(DATE_FILE, 'w') as file:
            # Step 2: Convert Python dictionary to JSON format and write to file
            json.dump(dates_dict, file, indent=4)  # Added indent for better readability
        print(f"✓ Data successfully saved to {DATE_FILE}")
    except PermissionError:
        print(f"✗ Error: Cannot write to {DATE_FILE}. Check file permissions.")
        raise
    except IOError as e:
        print(f"✗ Error: Failed to write to {DATE_FILE}. {str(e)}")
        raise

def load_dates():
    """
    Load dates from the JSON file.
    
    Returns:
    dict: Dictionary with dates if file exists, empty dictionary if file doesn't exist
    
    Raises:
    json.JSONDecodeError: If the JSON file is corrupted
    """
    try:
        # Step 1: Try to open the file in read mode ('r')
        with open(DATE_FILE, 'r') as file:
            # Step 2: Convert JSON content to Python dictionary
            dates_data = json.load(file)
            print(f"✓ Data loaded from {DATE_FILE}")
            return dates_data
    except FileNotFoundError:
        # Step 3: If file doesn't exist, return empty dictionary
        print(f"ℹ No existing data file found. Starting with empty database.")
        return {}
    except json.JSONDecodeError:
        # Step 4: Handle corrupted JSON file
        print(f"✗ Error: {DATE_FILE} contains invalid JSON. Starting with empty database.")
        return {}

def validate_date(date_string):
    """
    Validate if a string is a proper date in YYYY-MM-DD format.
    
    Parameters:
    date_string (str): Date string to validate
    
    Returns:
    bool: True if valid, False otherwise
    """
    try:
        # Step 1: Try to parse the date string
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        # Step 2: Return False if parsing fails
        return False

def add_date(dates_dict, name, date):
    """
    Add a new date to the dictionary and save it permanently.
    
    Parameters:
    dates_dict (dict): Current dictionary of dates
    name (str): Person's name
    date (str): Date to store in YYYY-MM-DD format
    
    Raises:
    ValueError: If date format is invalid
    """
    # Step 1: Validate the date format
    if not validate_date(date):
        print(f"✗ Invalid date format: {date}. Please use YYYY-MM-DD format.")
        raise ValueError(f"Invalid date format: {date}")
    
    # Step 2: Validate name (should not be empty)
    if not name.strip():
        print("✗ Error: Name cannot be empty.")
        raise ValueError("Name cannot be empty")
    
    # Step 3: Check if name already exists
    if name in dates_dict:
        print(f"ℹ {name} already exists. Overwriting previous date: {dates_dict[name]}")
    
    # Step 4: Add or update the date for the given name
    dates_dict[name] = date
    
    # Step 5: Save changes to JSON file
    save_dates(dates_dict)
    
    # Step 6: Confirm operation success to user
    print(f"✓ {name}'s date ({date}) has been successfully added.")

def list_dates(dates_dict):
    """
    Display all dates stored in the system.
    
    Parameters:
    dates_dict (dict): Dictionary containing all dates
    
    Returns:
    int: Number of dates displayed
    """
    # Step 1: Check if dictionary has elements
    if dates_dict:
        print("\n" + "="*50)
        print("LIST OF STORED DATES")
        print("="*50)
        
        # Step 2: Display header
        print(f"{'No.':<5} {'Name':<30} {'Date':<15}")
        print("-"*50)
        
        # Step 3: Iterate over each key-value pair in the dictionary
        for index, (name, date) in enumerate(dates_dict.items(), 1):
            # Step 4: Display each name and its corresponding date with numbering
            print(f"{index:<5} {name:<30} {date:<15}")
        
        print("="*50)
        print(f"Total: {len(dates_dict)} date(s) stored")
        return len(dates_dict)
    else:
        # Step 5: Message if no dates are stored
        print("ℹ No dates have been added to the system.")
        return 0

def search_date(dates_dict, name):
    """
    Search and display the date associated with a specific name.
    
    Parameters:
    dates_dict (dict): Dictionary containing all dates
    name (str): Name to search for
    
    Returns:
    str: The found date or None if not found
    """
    # Step 1: Check if the name exists in the dictionary
    if name in dates_dict:
        # Step 2: If found, display the associated date
        found_date = dates_dict[name]
        print(f"\n✓ Found: {name}'s date is {found_date}")
        return found_date
    else:
        # Step 3: If not found, inform the user
        print(f"✗ Not found: No date stored for '{name}'.")
        return None

def delete_date(dates_dict, name):
    """
    Delete a date entry by name.
    
    Parameters:
    dates_dict (dict): Dictionary containing all dates
    name (str): Name to delete
    
    Returns:
    bool: True if deleted, False if not found
    """
    # Step 1: Check if the name exists in the dictionary
    if name in dates_dict:
        # Step 2: Store the date before deletion for confirmation message
        deleted_date = dates_dict[name]
        
        # Step 3: Delete the entry
        del dates_dict[name]
        
        # Step 4: Save changes to file
        save_dates(dates_dict)
        
        # Step 5: Confirm deletion
        print(f"✓ Deleted: {name}'s date ({deleted_date}) has been removed.")
        return True
    else:
        # Step 6: Inform if name was not found
        print(f"✗ Cannot delete: No entry found for '{name}'.")
        return False

def display_statistics(dates_dict):
    """
    Display statistics about the stored dates.
    
    Parameters:
    dates_dict (dict): Dictionary containing all dates
    """
    if not dates_dict:
        print("ℹ No data available for statistics.")
        return
    
    print("\n" + "="*50)
    print("STATISTICS")
    print("="*50)
    
    # Step 1: Display total count
    print(f"Total entries: {len(dates_dict)}")
    
    # Step 2: Extract and analyze years
    years = []
    for date_str in dates_dict.values():
        try:
            year = int(date_str.split('-')[0])
            years.append(year)
        except (ValueError, IndexError):
            continue
    
    if years:
        print(f"Date range: {min(years)} - {max(years)}")
        print(f"Most common year: {max(set(years), key=years.count)}")
    
    # Step 3: Show 5 most recent entries
    print(f"\nRecent entries:")
    sorted_items = sorted(dates_dict.items(), key=lambda x: x[1], reverse=True)[:5]
    for name, date in sorted_items:
        print(f"  {name}: {date}")

def main():
    """
    Main function that controls the program flow
    and displays the interactive menu to the user.
    """
    # Step 1: Load existing dates when program starts
    dates = load_dates()
    
    print("\n" + "="*50)
    print("DATE MANAGER APPLICATION")
    print("="*50)
    print("Manage dates associated with names")
    print("Data is automatically saved to dates.json")
    print("="*50)
    
    # Step 2: Infinite loop that keeps program running until user chooses to exit
    while True:
        # Step 3: Display menu options
        print("\nMAIN MENU:")
        print("1. Add New Date")
        print("2. List All Dates")
        print("3. Search Date by Name")
        print("4. Delete Date Entry")
        print("5. View Statistics")
        print("6. Exit Program")
        print("-"*30)
        
        # Step 4: Prompt user to enter their choice
        choice = input("Enter your choice (1-6): ").strip()
        
        # Option 1: Add a new date
        if choice == '1':
            print("\n--- ADD NEW DATE ---")
            name = input("Enter the person's name: ").strip()
            date = input("Enter the date (YYYY-MM-DD format): ").strip()
            try:
                add_date(dates, name, date)
            except ValueError as e:
                print(f"Operation failed: {e}")
        
        # Option 2: List all stored dates
        elif choice == '2':
            print("\n--- ALL STORED DATES ---")
            list_dates(dates)
        
        # Option 3: Search for a specific date by name
        elif choice == '3':
            print("\n--- SEARCH DATE ---")
            name = input("Enter the person's name to search: ").strip()
            search_date(dates, name)
        
        # Option 4: Delete a date entry
        elif choice == '4':
            print("\n--- DELETE DATE ENTRY ---")
            name = input("Enter the person's name to delete: ").strip()
            delete_date(dates, name)
        
        # Option 5: Display statistics
        elif choice == '5':
            print("\n--- STATISTICS ---")
            display_statistics(dates)
        
        # Option 6: Exit the program
        elif choice == '6':
            print("\n" + "="*50)
            print("THANK YOU FOR USING DATE MANAGER")
            print(f"Data has been saved to {DATE_FILE}")
            print("="*50)
            break  # Break the while loop, ending the program
        
        # Step 5: Handle invalid inputs
        else:
            print(f"✗ Invalid choice: '{choice}'. Please enter a number from 1 to 6.")

# Program entry point - only executes if this file is run as the main program
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠ Program interrupted by user. Saving data...")
        # In a real application, you might want to save data here
        print("Goodbye!")
    except Exception as e:
        print(f"\n✗ An unexpected error occurred: {e}")
        print("Please check file permissions and try again.")

