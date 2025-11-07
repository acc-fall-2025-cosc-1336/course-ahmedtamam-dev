from lists import get_lowest_list_value, get_highest_list_value

def main():
    numbers = []

    while True:
        print("Menu:")
        print("1 - Show the list low/high values")
        print("2 - Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            numbers.clear()  # start fresh each time user chooses option 1

            while True:
                try:
                    num = float(input("Enter a list value: "))
                    numbers.append(num)
                except ValueError:
                    print("Please enter a valid number.")
                    continue

                # After 3 values, ask if they want to continue
                if len(numbers) >= 3:
                    while True:
                        more = input("Do you want to enter another value? (y/n): ").strip().lower()
                        if more in ("y", "n"):
                            break
                        else:
                            print("Please enter 'y' or 'n'.")

                    if more == "n":
                        break

            # Display results
            print(f"\nLowest value in list: {get_lowest_list_value(numbers)}")
            print(f"Highest value in list: {get_highest_list_value(numbers)}")

        elif choice == "2":
            print("Exiting program...")
            break
        else:
            print("Invalid option. Please choose 1 or 2.")

if __name__ == "__main__":
    main()
