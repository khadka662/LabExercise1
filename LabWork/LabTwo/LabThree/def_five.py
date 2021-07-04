'''
Q.No.5 Write a function called show_stars(rows).If rows is 5, it should print the following:
***************
'''

def show_starts(rows):
    for i in range(0,rows):
        for j in range(0,i+1):
            print('*',end='')
        print("\r")
rows = 5
show_starts(rows)

