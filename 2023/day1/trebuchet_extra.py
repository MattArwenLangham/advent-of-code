import re

f = open("input_extra.txt", "r")
raw_data = f.read().split("\n")
calibration_num = 0
calibration_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def generate_regex(): 
    regex_string = '(\d{1' + '}'
    for key in calibration_dict:
        regex_string += f'|{key}'
    regex_string += ')'
    return re.compile(regex_string)

def generate_xereg():
    xeger_string = '(\d{1' + '}'
    for key in calibration_dict:
        xeger_string += f'|{key[::-1]}'
    xeger_string += ')'
    return re.compile(xeger_string)

regex = generate_regex()
xeger = generate_xereg()

def extract_calibration(raw_string):
    first_number = re.search(regex, raw_string).group(0)
    last_number = re.search(xeger, raw_string[::-1]).group(0)[::-1]
    if first_number in calibration_dict:
        first_number = calibration_dict.get(first_number)
    if last_number in calibration_dict:        
        last_number = calibration_dict.get(last_number)
    return int(first_number + last_number)

for raw_string in raw_data:
    calibration_value = extract_calibration(raw_string)
    calibration_num += calibration_value

print(calibration_num)