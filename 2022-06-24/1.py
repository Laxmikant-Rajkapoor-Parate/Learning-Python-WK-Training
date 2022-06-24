def isPresent(inputstr):
    present = False
    for num in inputstr:
        if num % 2 == 0:
            present = True
            break
    return present

if __name__ == '__main__':
    inputstr = list(map(int, input('Enter numbers:\n').split()))
    if isPresent(inputstr):
        print('Even numbers present!')
    else:
        print('Even numbers not present')
