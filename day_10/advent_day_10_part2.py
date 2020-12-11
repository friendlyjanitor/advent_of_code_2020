import fileinput
import itertools


def generate_input():
    return sorted([int(x) for x in fileinput.input()])

def find_differences(adapters, order):
    starting_volt = 0

    adapter_list = []

    while starting_volt != max(adapters):
        if starting_volt + order[0] in adapters:
            adapter_list.append(starting_volt + order[0])
            starting_volt += order[0]
            continue
        if starting_volt + order[1] in adapters:
            adapter_list.append(starting_volt + order[1])
            starting_volt += order[1]
            continue
        if starting_volt + order[2] in adapters:
            adapter_list.append(starting_volt + order[2])
            starting_volt += order[2]
            continue

    return adapter_list

def find_adapter_sets(adapters):
    counted_adapters = {0:1}
    for adapter in sorted(adapters):
        counted_adapters[adapter] = 0
        import pdb;pdb.set_trace()
        if adapter - 1 in counted_adapters:
            counted_adapters[adapter] += counted_adapters[adapter-1]
        if adapter - 2 in counted_adapters:
            counted_adapters[adapter] += counted_adapters[adapter-2]
        if adapter - 3 in counted_adapters:
            counted_adapters[adapter] += counted_adapters[adapter-3]
    print(counted_adapters[max(adapters)])

#def find_adapter_sets(adapters):


adapters = generate_input()
find_adapter_sets(adapters)