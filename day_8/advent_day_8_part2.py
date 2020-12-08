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
    accumulator = 0
    pointer = 0

    def execute(instruction):
        arg = instruction[1]
        op = instruction[0]
        if op == "acc":
            return int(arg), 1

        elif op == "jmp":
            return 0, int(arg)

        else:
            return 0, 1

    seen = set()  # Set of pointers we've seen so far
    accumulator = 0
    pointer = 0
    while pointer not in seen and pointer < len(rules):
        seen.add(pointer)
        acc, jmp = execute(rules[pointer])
        accumulator += acc
        pointer += jmp

    if pointer >= len(rules):
        return accumulator

    return None


def code_repair(rules):
    for i in range(len(rules)):
        if final_rules[i][0] == "acc":
            continue

        if final_rules[i][0] == "nop":
            copy = rules.copy()
            copy[i] = ["jmp", rules[i][1]]

        else:
            copy = rules.copy()
            copy[i] = ["nop", rules[i][1]]

        x = boot_code(copy)
        if x:
            print(x)
            break




final_rules = generate_rules()
#boot_code(final_rules, 0, 0)
code_repair(final_rules)

