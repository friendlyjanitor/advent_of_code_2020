import fileinput
import re


def generate_rules():
    final_rules = {}
    for line in fileinput.input():
        colors = re.findall(r'(\w* \w*) bag', line)
        parent = colors[0]
        secondary = list(colors[1:])
        final_rules[parent] = secondary
    return final_rules

def contains_shiny_gold(rules):
    contain_shiny_gold = []
    for parent_bag in rules.keys():
        if 'shiny gold' in rules[parent_bag]:
            contain_shiny_gold.append(parent_bag)
            del rules[parent_bag]
    return contain_shiny_gold, rules

def outside_check(contain_shiny_gold, rules, total):
    return_list = []

    for bag in contain_shiny_gold:
        for parent_bag in rules.keys():
            if bag in rules[parent_bag]:
                total += 1
                return_list.append(parent_bag)
                del rules[parent_bag]

    return return_list, total

def second_layer_check(contain_shiny_gold, rules):
    total = len(contain_shiny_gold)
    while contain_shiny_gold:
        contain_shiny_gold, total = outside_check(contain_shiny_gold, rules, total)
    print total




rules = generate_rules()
contain_shiny_gold, rules = contains_shiny_gold(rules)
second_layer_check(contain_shiny_gold, rules)
