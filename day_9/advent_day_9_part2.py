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
            return channel_list[channel]

def slide_channel(broken_channel, channel_list):
    for channel in range(0, len(channel_list) - 1):
        the_answer = find_sum_list(broken_channel, channel_list[channel:])
        if the_answer:
            print(the_answer)
            break



def find_sum_list(broken_channel, channel_list):
    sum_list = []
    for channel in channel_list:
        sum_list.append(channel)

        if sum(sum_list) > broken_channel:
            sum_list = []
            continue
        if sum(sum_list) == broken_channel and len(sum_list) > 1:
            return min(sum_list) + max(sum_list)
    return None


channel_list = generate_input()
broken_channel = find_broken(channel_list)
slide_channel(broken_channel, channel_list)