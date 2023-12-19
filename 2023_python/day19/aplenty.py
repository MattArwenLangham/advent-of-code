def read_input(file_path):
    with open(file_path, 'r') as file:
        workflow, part_ratings = file.read().split("\n\n")
        return workflow.split("\n"), part_ratings.split("\n")

rules_dict = {}

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

def rate_parts(part_ratings):
    parts_accepted = []
    for part_rating in part_ratings:
        part_rating_list = part_rating.replace("{", "").replace("}", "").split(",")
        rule = 'in'
        i = 0
        while rule != 'A' or rule != 'R':
            rule_to_compare = rules_dict[rule][i]
            part_to_compare = rule_to_compare[0]
            comparison = rule_to_compare[1]
            value_to_compare = rule_to_compare[2]

            if part_to_compare == 'x':
                part_rating = part_rating_list[0]
            elif part_to_compare == 'm':
                part_rating = part_rating_list[1]
            elif part_to_compare == 'a':
                part_rating = part_rating_list[2]
            elif part_to_compare == 's':
                part_rating = part_rating_list[3]
            value = int(part_rating[2:])

            if comparison == '<':
                if value < value_to_compare:
                    if isinstance(rules_dict[rule][i + 1], str):
                        rule = rules_dict[rule][i + 1]
                        i = 0
                    else:
                        i += 1
                else:
                    if isinstance(rules_dict[rule][i + 2], str):
                        rule = rules_dict[rule][i + 2]
                        i = 0
                    else:
                        i += 2
            else:
                if value > value_to_compare:
                    if isinstance(rules_dict[rule][i + 1], str):
                        rule = rules_dict[rule][i + 1]
                        i = 0
                    else:
                        i += 1
                else:
                    if isinstance(rules_dict[rule][i + 2], str):
                        rule = rules_dict[rule][i + 2]
                        i = 0
                    else:
                        i += 2

            if rule == 'A':
                parts_accepted.append(part_rating_list)
                break
            elif rule == 'R':
                break
    return parts_accepted

def sum_all_accepted_parts(accepted_parts):
    sum = 0
    for accepted_part in accepted_parts:
        for part in accepted_part:
            sum += int(part[2:])
    return sum


workflow, part_ratings = read_input('input.txt')
create_rules(workflow)
accepted_parts = rate_parts(part_ratings)
result = sum_all_accepted_parts(accepted_parts)
print(result)