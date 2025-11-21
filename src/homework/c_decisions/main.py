import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from src.homework.c_decisions.decisions import get_options_ratio, get_faculty_rating

def main():
    try:
        option = float(input("Enter the number of options (e.g. positive votes): "))
        total = float(input("Enter the total number: "))

        ratio = get_options_ratio(option, total)
        rating = get_faculty_rating(ratio)

        print(f"\nRatio: {ratio:.2f}")
        print(f"Faculty Rating: {rating}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

