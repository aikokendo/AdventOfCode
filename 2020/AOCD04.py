from classes.helper import Helper
from classes.idDocument import IdDocument

def parseFiletoIds(file_data,mandatory,optional,rules):
    ids = file_data.split('\n\n')
    return [IdDocument(id,mandatory,optional,rules) for id in ids]

def countValidPassports(ids):
    return sum([1 for id in ids if id.checkValid()])

def countValidPassportsSimple(ids):
    return sum([1 for id in ids if id.checkAllFieldsPresent()])

m = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
o = ['cid']
rules = [
            '^byr:((19[2-9][0-9])|200[0-2])$', #byr (Birth Year) - four digits; at least 1920 and at most 2002.
            '^iyr:((201[0-9])|2020)$', #(Issue Year) - four digits; at least 2010 and at most 2020.
            '^eyr:((202[0-9])|2030)$', # (Expiration Year) - four digits; at least 2020 and at most 2030.
            # (Height) - a number followed by either cm or in:
            '^hgt:(1[5-8][0-9]|19[0-3])cm$', # If cm, the number must be at least 150 and at most 193.
            '^hgt:(59|6[0-9]|7[0-6])in$', # If in, the number must be at least 59 and at most 76.
            '^hcl:#[0-9a-f]{6}$', # (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
            '^(ecl:)(amb|blu|brn|gry|grn|hzl|oth)$', #(Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
            '^pid:[0-9]{9}$', #pid (Passport ID) - a nine-digit number, including leading zeroes.
            '^cid:.*$' #cid (Country ID) - ignored, missing or not.
]
# Make a regex that matches if any of our regexes match.
rules = "(" + ")|(".join(rules) + ")"

file_name = 'input\inputd04.txt'
file = Helper.read_file(file_name)
passports = parseFiletoIds(file,m,o,rules)
print('Part 1 solution:', countValidPassportsSimple(passports))
print('Part 2 solution:', countValidPassports(passports))