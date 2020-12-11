import fileinput
import re


valid_criteria =[
'byr',
'iyr',
'eyr',
'hgt',
'hcl',
'ecl',
'pid'
]


def validate_fields(k, v, valid):
    if k == 'byr':
        valid = (len(v)==4 and (1920 <= int(v) <= 2002))
    if k == 'iyr':
        valid = (len(v)==4 and (2010 <= int(v) <= 2020))
    if k == 'eyr':
        valid = (len(v)==4 and (2020 <= int(v) <= 2030))
    if k == 'pid':
        valid = re.match(r"^\d{9}$", v) is not None
    if k == 'ecl':
        valid = v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if k == 'hcl':
        valid = re.match(r"^#[a-f0-9]{6}", v) is not None
    if k == 'hgt':
        valid = (re.match(r"^1[5-8][0-9]cm|19[0-3]cm", v) or re.match(r"^6[0-9]in|5[9]in|7[0-6]in", v)) is not None

    return valid

def generate_passports():
    passports = []
    passport = {}
    for line in fileinput.input():
        if line == '\n':
            passports.append(passport)
            passport = {}
            continue
        line = line.strip('\n').split()
        for pairs in line:
            key, value = pairs.split(':')
            passport[key] = value
    passports.append(passport) # the last line wasn't getting added
    return passports

def find_valid_passports(passports):
    valid_passports = []
    for passport in passports:
        passport.pop('cid', None)
        keys = passport.keys()
        if sorted(keys) == sorted(valid_criteria):
            valid_passports.append(passport)
    print len(valid_passports)
    return valid_passports

def passport_validation(valid_passports):
    final_count = 0
    for vp in valid_passports:
        valid = False
        for field, value in vp.iteritems():
            valid = validate_fields(field, value, valid)
            if not valid:
                break
        if valid:
            final_count +=1

    print final_count








passports = generate_passports()
valid_passport = find_valid_passports(passports)
passport_validation(valid_passport)
