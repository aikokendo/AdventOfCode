def slidePath(h,v,terrain): # accepts horizontal and vertical input and terrain
    x = 0
    y = 0
    w = len(terrain[0])
    trees = 0
    for x in range(v,len(terrain),v):
        #find new y
        y = (y+h)%w
        if terrain[x][y] == '#':
            trees += 1
    return trees



f = open('inputd03.txt', 'r+')
my_file_data = f.read()
f.close()

terrain = my_file_data.split('\n')
print('Part 1 solution:', slidePath(3,1,terrain))
result = slidePath(1,1,terrain) * slidePath(3,1,terrain) * slidePath(5,1,terrain) * slidePath(7,1,terrain) * slidePath(1,2,terrain)
print('Part 2 solution: ', result)

