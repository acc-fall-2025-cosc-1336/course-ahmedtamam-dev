from repetition import get_factorial, sum_odd_numbers
def main():
    while True:
        print("\nHomework 4 Menu")
        print("1 - Factorial")
        print("2 - Sum odd numbers")
        print("3 - Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            num = int(input("Enter a number (1-9): "))
            while num <= 0 or num >= 10:
                print("Number must be greater than 0 and less than 10.")
                num = int(input("Enter a number (1-9): "))
            print(f"Factorial of {num} = {get_factorial(num)}")

        elif choice == "2":
            num = int(input("Enter a number (1-99): "))
            while num <= 0 or num >= 100:
                print("Number must be greater than 0 and less than 100.")
                num = int(input("Enter a number (1-99): "))
            print(f"Sum of odd numbers up to {num} = {sum_odd_numbers(num)}")

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
