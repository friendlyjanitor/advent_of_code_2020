import fileinput
import itertools


def generate_input():
    return [int(x) for x in fileinput.input()]

def generate_preamble(channel_list):
    sums = []
    for number in itertools.combinations(channel_list, 2):
        sums.append(sum(number))
    return sums

def find_broken(channel_list):

    for channel in range(25, len(channel_list) - 1):
        preamble = generate_preamble(channel_list[(channel - 25):channel])
        if channel_list[channel] not in preamble:
            return (channel_list[channel],  channel_list[(channel -25):channel])

channel_list = generate_input()
broken = find_broken(channel_list)
print (broken)