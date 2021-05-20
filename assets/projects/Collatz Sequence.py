# Main function which prints sequence and largest value.
def explore_collatz():
    seq = generate_sequence()
    display_sequence(seq)
    print("\nLargest value: ", find_largest(seq))
    
# Prompts the user for a positive integer. Then generates the rest of sequence using n. No error check.
def generate_sequence():
    sequence = []
    n = int(input("Collatz sequence start value (1 or more): "))
    sequence = [n]
    print()
    while n > 1:
        if n % 2 == 0:
            n = n // 2
            sequence.append(n)
        else:
            n = (3 * n) + 1
            sequence.append(n)
    return sequence

# Prints all of the list showing 6 separated tab values in each row using a loop.
def display_sequence(sequence):
    seq = 1
    for i in sequence:
        print(i, "\t", end = " ")
        if(seq % 6 == 0):
            print()
        seq += 1
    print()
    
# Finds and returns the largest value in the integer list sequence using a loop.
def find_largest(sequence):
    largest_value = sequence[0]
    for i in sequence:
        if(i > largest_value):
            largest_value = i
    return largest_value