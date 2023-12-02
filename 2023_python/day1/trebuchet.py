import re

f = open("input.txt", "r")
raw_data = f.read().split("\n")
calibration_num = 0

def extract_calibration(raw_string):
    values = re.findall(r'\d', raw_string)
    return int(values[0] + values[-1])

for raw_string in raw_data:
    calibration_value = extract_calibration(raw_string)
    calibration_num += calibration_value

print(calibration_num)