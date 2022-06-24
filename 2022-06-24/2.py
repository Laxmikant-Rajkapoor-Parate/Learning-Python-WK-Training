def seperateOddEven(nums):
    oddNumbers = []
    evenNumbers = []
    for num in nums:
        if num % 2 == 0:
            evenNumbers.append(num)
        else:
            oddNumbers.append(num)

    print(f'Odd Numbers: {oddNumbers}')
    print(f'Even Numbers: {evenNumbers}')

if __name__ == '__main__':
    nums = list(map(int, input('Enter elements:\n').split()))
    seperateOddEven(nums)
    print()
