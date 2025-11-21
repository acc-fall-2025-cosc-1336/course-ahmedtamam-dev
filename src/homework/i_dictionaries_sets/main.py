from dictionary import add_inventory, remove_inventory_widget

def main():
    widgets = {}

    while True:
        print("\nInventory Menu")
        print("1 - Add or Update Item")
        print("2 - Delete Item")
        print("3 - Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter widget name: ")
            qty = int(input("Enter quantity (+ or - OK): "))
            add_inventory(widgets, name, qty)
            print("Inventory updated:", widgets)

        elif choice == "2":
            name = input("Enter widget name to delete: ")
            result = remove_inventory_widget(widgets, name)
            print(result)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid selection. Try again.")

if __name__ == "__main__":
    main()