import itertools
import numpy
import fileinput

def generate_list():
    expense_report = []
    for line in fileinput.input():
        expense_report.append(int(line.strip('\n')))
    return expense_report

def sum_2020(expense_report, r):
    combinations = itertools.combinations(expense_report, r)
    for comb in combinations:
        if sum(comb) == 2020:
            print numpy.prod(comb)


expense_report = generate_list()
sum_2020(expense_report, 3)