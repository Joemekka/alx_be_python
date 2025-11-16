outer_count = int(input('Enter the size of the pattern: '))
row = 0
while row < outer_count:
        for _ in range(outer_count):
                print('*', end='')
        print()
        row += 1