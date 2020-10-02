while(True):
    n = int(input('Enter a number :\n'))

    if n == 18:
        print('Yes you got it !!! \n')
        break
    elif n > 30:
        print(f'Sorry, your entered number {n}  is greater than expected.')
        continue
    elif n < 15:
        print(f'Sorry, your entered number {n}  is smaller than expected.')
        continue
    elif n >= 15 < 18:
        print('Good ! Your are nearly close...')
        continue
    elif n < 30 >= 19:
        print('Good ! Your are nearly close...')
        continue
    else:
        print('Please try again !\n')
        continue

