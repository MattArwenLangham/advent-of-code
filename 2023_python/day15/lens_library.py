def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.read().split(",")
    
def hash_sequence(initialization_sequence):
    print("Hash sequence:", initialization_sequence)
    current_value = 0
    for char in initialization_sequence:
        current_value += ord(char)
        current_value *= 17
        current_value = current_value % 256
    return current_value
        
    
def hash_all_sequences(initialization_sequences):
    sum_of_sequences = 0
    for initialization_sequence in initialization_sequences:
        sum_of_sequences += hash_sequence(initialization_sequence)
    return sum_of_sequences

initialization_sequences = read_input('input.txt')
result = hash_all_sequences(initialization_sequences)
print(result)