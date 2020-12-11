import fileinput

def generate_questionnaires_part_1(): # part 1
    questionnaires = []
    group = []
    for line in fileinput.input():
        if line == '\n':
            questionnaires.append(set(group))
            group = []
            continue
        line = line.strip('\n')
        for data in list(line):
            group.append(data)
    questionnaires.append(set(group)) # the last line wasn't getting added
    return questionnaires

def generate_questionnaires_part_2(): # part 2
    questionnaires = []
    group = []
    for line in fileinput.input():
        if line == '\n':
            group = common_elements(group)
            questionnaires.append(set(group))
            group = []
            continue
        group.append(line.strip('\n'))
    group = common_elements(group)
    questionnaires.append(set(group)) # the last line wasn't getting added
    return questionnaires


def total_yes_count(groups): #part 1
    total_count = 0
    for group in groups:
        total_count += len(group)
    print total_count

def common_elements(group):
    return set(group[0]).intersection(*group)



#questionnaires = generate_questionnaires_part_1() #part_1 answer
questionnaires = generate_questionnaires_part_2()
total_yes_count(questionnaires)