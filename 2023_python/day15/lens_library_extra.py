def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.read().split(",")
    
def get_box_number(label_name):
    current_value = 0
    for char in label_name:
        current_value += ord(char)
        current_value *= 17
        current_value = current_value % 256
    return current_value

lens_library_dict = {}

def add_lens_to_box(box_number, label_name, focal_length):
    if not box_number in lens_library_dict.keys():
        lens_library_dict[box_number] = []

    for lens in lens_library_dict[box_number]:
        if lens[0] == label_name:
            lens[1] = focal_length
            return
    
    lens_library_dict[box_number].append([label_name, focal_length])

def remove_lens_from_box(box_number, label_name):
    if box_number in lens_library_dict.keys():
        for i, lens in enumerate(lens_library_dict[box_number]):
            if lens[0] == label_name:
                lens_library_dict[box_number].pop(i)
        if len(lens_library_dict[box_number]) == 0:
            del lens_library_dict[box_number]

def hashmap_initialization_sequences(initialization_sequences):
    for initialization_sequence in initialization_sequences:
        delimiter = '=' if "=" in initialization_sequence else '-'
        label_name, operation, focal_length = initialization_sequence.partition(delimiter)
        box_number = get_box_number(label_name)
        if operation == '=':
            add_lens_to_box(box_number, label_name, int(focal_length))
        else:
            remove_lens_from_box(box_number, label_name)
    
def calculate_sum_focusing_power_of_hashmap():
    sum_focusing_power = 0
    for box_number, lenses in lens_library_dict.items():
        for pos, [_, focal_length] in enumerate(lenses):
            sum_focusing_power += (box_number + 1) * (pos + 1) * focal_length
    return sum_focusing_power

initialization_sequences = read_input('input.txt')
hashmap_initialization_sequences(initialization_sequences)
result = calculate_sum_focusing_power_of_hashmap()
print(result)