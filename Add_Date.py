import json

def save_dates(dates):
    with open('dates.json', 'w') as file:
        json.dump(dates, file)

def load_dates():
    try:
        with open('dates.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def add_date(dates, name, date):
    dates[name] = date
    save_dates(dates)
    print(f"{name}'s date has been added.")

def list_dates(dates):
    if dates:
        print("List of Dates:")
        for name, date in dates.items():
            print(f"{name}: {date}")
    else:
        print("No dates have been added.")

def search_date(dates, name):
    if name in dates:
        print(f"{name}'s date: {dates[name]}")
    else:
        print(f"No date found for {name}.")

def main():
    dates = load_dates()

    while True:
        print("\nOptions:")
        print("1. Add Date")
        print("2. List Dates")
        print("3. Search Date")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the person's name: ")
            date = input("Enter the date (e.g., YYYY-MM-DD): ")
            add_date(dates, name, date)

        elif choice == '2':
            list_dates(dates)

        elif choice == '3':
            name = input("Enter the person's name: ")
            search_date(dates, name)

        elif choice == '4':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()