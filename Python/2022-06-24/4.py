def countVowels(inputstr, vowels):
    ans = {}
    for char in vowels:
        ans[char] = 0

    for char in inputstr:
        if char in vowels:
            ans[char] += 1

    return ans

if __name__ == '__main__':
    vowels = 'aeiou'
    inputstr = input('Enter the string: ')
    inputstr = inputstr.casefold()

    ans = countVowels(inputstr, vowels)
    print(ans)
    print()
