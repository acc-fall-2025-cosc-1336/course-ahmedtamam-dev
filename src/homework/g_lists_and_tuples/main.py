from lists import get_p_distance_matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{x:.5f}" if x != 0 else "0.00000" for x in row))

def get_dna_sequences_from_user():
    print("Enter DNA sequences as Python lists (one per line).")
    print("Example: ['T', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'A']")
    print("Type 'done' when finished.")
    
    sequences = []
    while True:
        user_input = input("Enter sequence (or 'done'): ").strip()
        if user_input.lower() == 'done':
            break
        try:
            seq = eval(user_input)
            if not isinstance(seq, list):
                print("Error: Must be a list!")
                continue
            if sequences and len(seq) != len(sequences[0]):
                print(f"Error: All sequences must have same length ({len(sequences[0])})")
                continue
            sequences.append(seq)
        except Exception as e:
            print("Invalid input. Please enter a valid Python list.")
    
    return sequences

def main():
    print("=== P-Distance Matrix Calculator ===")
    
    while True:
        print("Menu:")
        print("1 - Get p-distance matrix")
        print("2 - Exit")
        
        choice = input("Choose an option (1-2): ").strip()
        
        if choice == '1':
            sequences = get_dna_sequences_from_user()
            if len(sequences) < 2:
                print("Error: Need at least 2 sequences!")
                continue
            if len(sequences) > 10:
                print("Error: Maximum 10 sequences allowed.")
                continue
                
            try:
                matrix = get_p_distance_matrix(sequences)
                print("P-Distance Matrix:")
                print_matrix(matrix)
            except Exception as e:
                print(f"Error calculating matrix: {e}")
                
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1 or 2.")

if __name__ == "__main__":
    main()
