def passwordCheckerSledRental(passAndPolicies):
    validPass = 0
    for p in passAndPolicies:
        elements = p.split()
        passRange = elements[0].split('-')
        charInstance =  elements[2].count(elements[1].replace(':',''))
        if charInstance >= int(passRange[0]) and charInstance <= int(passRange[1]):
            validPass += 1

    return validPass


def passwordChecker(passAndPolicies):
    validPass = 0
    for p in passAndPolicies:
        elements = p.split()
        passRange = elements[0].split('-')
        start = int(passRange[0])-1
        end = int(passRange[1])-1
        policy = elements[1].replace(':', '')
        pas = elements[2]
        if (len(pas) > start and pas[start] == policy) ^ (len(pas) > end and pas[end] == policy):
            validPass += 1

    return validPass

f = open('inputd02.txt', 'r+')
my_file_data = f.read()
f.close()

passAndPolicies = my_file_data.split('\n')

validPass = passwordChecker(passAndPolicies)
print(validPass)

