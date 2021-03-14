def lines_to_list(fname):
    with open(fname, 'r') as f:
        mylist = f.readlines()
        return mylist

print(lines_to_list('test.txt'))
