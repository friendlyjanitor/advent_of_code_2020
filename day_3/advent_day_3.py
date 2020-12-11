import fileinput

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
def __move_sleigh(right, down, dr, dd):

    return right + dr, down + dd

def find_trees():
    combined_trees = 1
    g =[]

    for lines in fileinput.input():
        g.append(list(lines.strip()))
    for dr, dd in slopes:
        right = 0
        down = 0
        trees = 0
        while down + 1 < len(g):
            #import pdb;pdb.set_trace()
            if g[down][right%len(g[down])] == '#':
                trees += 1
            right, down =__move_sleigh(right, down, dr, dd)
        #print trees
        combined_trees *= trees
    print (combined_trees)


find_trees()