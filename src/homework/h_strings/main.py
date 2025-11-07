import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src')))


from strings import get_hamming_distance, get_dna_complement

def main():
    while True:
        print("1 - Hamming Distance")
        print("2 - DNA Complement")
        print("3 - Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            dna1 = input("Enter first DNA string: ").upper()
            dna2 = input("Enter second DNA string: ").upper()
            result = get_hamming_distance(dna1, dna2)
            print("Hamming Distance:", result)

        elif choice == "2":
            dna = input("Enter DNA string: ").upper()
            result = get_dna_complement(dna)
            print("DNA Reverse Complement:", result)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option, please try again.")
if __name__ == "__main__":
    main()
