def password_checker_sled_rental(pass_policies):
    valid_pass = 0
    for p in pass_policies:
        elements = p.split()
        pass_range = elements[0].split('-')
        char_instance = elements[2].count(elements[1].replace(':',''))
        if int(pass_range[0]) <= char_instance <= int(pass_range[1]):
            valid_pass += 1

    return valid_pass


def password_checker(pass_policies):
    valid_pass = 0
    for p in pass_policies:
        elements = p.split()
        pass_range = elements[0].split('-')
        start = int(pass_range[0])-1
        end = int(pass_range[1])-1
        policy = elements[1].replace(':', '')
        pas = elements[2]
        if (len(pas) > start and pas[start] == policy) ^ (len(pas) > end and pas[end] == policy):
            valid_pass += 1
    return valid_pass


f = open('input\inputd02.txt', 'r')
my_file_data = f.read()
f.close()

pass_policies = my_file_data.split('\n')
print('Part 1 solution: ', password_checker_sled_rental(pass_policies))
print('Part 2 solution: ', password_checker(pass_policies))


