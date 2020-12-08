import fileinput
import re



def generate_rules():
    final_rules = []
    for line in fileinput.input():
        action = re.findall(r'\w*', line)
        step = (action[0], integers(line)[0])

        final_rules.append(step)
    return final_rules


def integers(number): #had to do some researching online for assistance
    if re.search(r'[-]', number) is not None:
        return [(-1 *int(number))for number in re.findall(r'\d*', number) if number.isdigit()]
    return [int(number)for number in re.findall(r'\d+', number) if number.isdigit()]

def boot_code(rules):
    seen = set()
    position = 0
    acc = 0
    while True:
        if position in seen:
            print (acc)
            break
        seen.add(position)
        if rules[position][0] == 'acc':
            acc += rules[position][1]
            position += 1

        if rules[position][0] == 'nop':
            position += 1

        if rules[position][0] == 'jmp':
            position += rules[position][1]

final_rules = generate_rules()
boot_code(final_rules)
