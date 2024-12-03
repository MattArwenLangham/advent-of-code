def read_input(file_path):
    with open(file_path, 'r') as file:
        workflow, _ = file.read().split("\n\n")
        return workflow.split("\n")

rules_dict = {}

part_range = 4000

def create_rules(workflow):
    for rules in workflow:
        name, rules = rules.replace("}", "").split("{")
        rule_list = rules.split(",")
        rules_dict[name] = []
        for rule in rule_list:
            rule = rule.split(':')
            if len(rule) > 1:
                part_to_compare = rule[0][0]
                comparison = rule[0][1]
                value_to_compare = int(rule[0][2:])
                place_to_send = rule[1]
                rules_dict[name].append([part_to_compare, comparison, value_to_compare])
                rules_dict[name].append(place_to_send)
            else:
                rules_dict[name].extend(rule)


range_dict = {
    'a': [0, part_range],
    'm': [0, part_range],
    's': [0, part_range],
    'x': [0, part_range]
}

def reset_range_dict():
    for key in range_dict.keys():
        range_dict[key][0] = 0
        range_dict[key][1] = part_range

def reverse_rule(rule):
    reversed_rule = [rule[0], "", rule[2]]
    if rule[1] == '<':
        reversed_rule[1] = '>'
    else:
        reversed_rule[1] = '<'
    return reversed_rule

def get_product_of_ranges():
    print("multiplying ranges")
    product = 1
    for lo, hi in range_dict.values():
        print(hi - lo)
        product *= (hi - lo)
    return product

def find_range_of_possibilities(key, rules):
    print(key, rules)
    print(key, rules_dict[key])
    for part, operator, number in rules:
        if operator == '>':
            range_dict[part][0] = number + 1
        else:
            range_dict[part][1] = number - 1
    print(range_dict)
    return find_all_accepted_parts(key)

def find_all_accepted_parts(key_to_find = 'A'):
    possibilities = 0
    if key_to_find == 'in':
        possibilities += get_product_of_ranges()
        reset_range_dict()
        return possibilities
    for key, rules in rules_dict.items():
        for i, rule in enumerate(rules):
            if rule == key_to_find:
                j = 1
                possibility_list = []
                while i - j > 0:
                    if isinstance(rules[i - j], list):
                        possibility_list.append(rules[i - j])
                    else:
                        j += 1
                        possibility_list.append(reverse_rule(rules[i - j]))
                    j += 1
                if len(possibility_list) == 0:
                    possibility_list.append(rules[0])
                possibilities += find_range_of_possibilities(key, possibility_list)
    return possibilities

workflow = read_input('test_input.txt')
create_rules(workflow)
result = find_all_accepted_parts()
print("RESULTED:", result)
print('EXPECTED:', 167409079868000)
print("LIMITEDD:", 256000000000000)