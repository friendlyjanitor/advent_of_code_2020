import fileinput


def generate_input():
    return [int(x) for x in fileinput.input()]

def find_differences(adapters):
    starting_volt = 0
    ending_volt = max(adapters) + 3
    volt_1 = []
    volt_3 = []
    while starting_volt != max(adapters):
        if starting_volt + 1 in adapters:
            volt_1.append(starting_volt + 1)
            starting_volt += 1
            continue
        if starting_volt + 3 in adapters:
            volt_3.append(starting_volt + 3)
            starting_volt += 3
            continue

    print (len(volt_1) * (len(volt_3) +1))



adapters = generate_input()
find_differences(adapters)