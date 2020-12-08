import fileinput
import re


def generate_rules():
    final_rules = {}
    for rule in fileinput.input():
        rule = rule.strip('.\n').split(' contain ')
        parent_bag, children_bags = rule[0], rule[1]
        parent_bag = parent_bag.rstrip('s')
        bags = []
        for bag in children_bags.split(', '):
            bag = re.sub(r"[0-9]{1}[\s]", "", bag)
            bags.append(bag.rstrip('s'))
        final_rules[parent_bag] = bags
    return final_rules

def contains_shiny_gold(rules):
    contain_shiny_gold = []
    for parent_bag in rules.keys():
        if 'shiny gold bag' in rules[parent_bag]:
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
