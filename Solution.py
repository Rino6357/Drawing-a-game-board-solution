def main():
    x = int(input('What is the size of your board? (size(x)size):'))
    y = x
    board(x, y)

def board(loop, const):
    i = 0
    while i < loop:
        print('---'*const)
        print('|  '*(const+1))
        loop-=1
    print('---'*const)
main()
