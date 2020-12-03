def slidePath(h,v,terrain): # accepts horizontal and vertical input and terrain
    x = 0
    y = 0
    w = len(terrain[0])
    trees = 0
    for step in range(0,len(terrain)-1,v):
        #find new y
        if y + h < w:
            y += h
        else:
            y = (y + h - w)
        #find new x
        x += v
        if terrain[x][y] == '#':
            trees += 1
    return trees



f = open('inputd03.txt', 'r+')
my_file_data = f.read()
f.close()

terrain = my_file_data.split('\n')
result = slidePath(1,1,terrain) * slidePath(3,1,terrain) * slidePath(5,1,terrain) * slidePath(7,1,terrain) * slidePath(1,2,terrain)
print(result)