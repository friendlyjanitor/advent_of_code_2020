import fileinput
import re


def generate_rules():
    final_rules = {}
    for line in fileinput.input():
        colors = re.findall(r'(\w* \w*) bag', line)
        parent = colors[0]
        secondary = list(zip(colors[1:], integers(line)))
        final_rules[parent] = dict(secondary)
    return final_rules

def integers(s): #had to do some researching online for assistance
    return [int(s)for s in re.findall(r'\d', s) if s.isdigit()]

def bag_count(color, rules):
    bags = rules

    def stack(bag):
        total = 1
        if bags[bag]:
            for inside in bags[bag]:
                total += bags[bag][inside] * stack(inside)
            return total
        return total

    print stack(color) - 1


rules = generate_rules()
bag_count('shiny gold', rules)