def filePreprocess():
    l = []
    with open("../data/day3.txt") as f:
        for x in f.readlines():
            l.append(x.strip())
    return l

def count_trees(matrix, right=3, down=1):
    rows = len(matrix)-1
    cols = len(matrix[0])
    i, j = 0, 0
    trees = 0
    while i < rows-down:
        if j >= cols - right:
            j = (j-cols)
        if matrix[i+down][j+right] == '#':
            trees += 1
        i += down
        j += right

    return trees


l = filePreprocess()
factor = count_trees(l, right=3, down=1)*count_trees(l, right=1, down=1)*count_trees(l, right=5, down=1)*count_trees(l, right=7, down=1)*count_trees(l, right=1, down=2)
print(factor)