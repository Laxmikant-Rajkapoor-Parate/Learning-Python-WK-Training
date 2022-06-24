def getVowels(inputstr, vowels):
    ans = []
    for char in inputstr:
        if char in vowels:
            ans.append(char)
    return ans

if __name__ == '__main__':
    vowels = 'aeiou'
    inputstr = input('Enter the string: ')
    inputstr = inputstr.casefold()
    ans = getVowels(inputstr, vowels)
    print(ans)
    print()
