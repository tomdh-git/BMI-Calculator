def power(x: int, n: int) -> int:
    if n == 0:
        return 1
    else:
        return x * power(x,n-1)

def sum_digits(n: int) -> int:
    if n == 0:
        return 0
    return n%10 + sum_digits(n//10)

def num_vowels(word: str) -> int:
    if word == '':
        return 0
    if word[0:1] == 'a' or word[0:1] == 'e' or word[0:1] == 'i' \
        or word[0:1] == 'o' or word[0:1] == 'u' or word[0:1] == 'y':
        return 1 + num_vowels(word[1:])
    else:
        return num_vowels(word[1:])

def print_backwards(word: str) -> None:
    count = 0
    for i in word:
        count += 1
    if word == '':
        return
    else:
        print(word[count-1:count],end = '') #last letter
        print_backwards(word[0:count-1])

def max_digit(n: int) -> int:
    count = 0
    if n == 0:
        return 0
    for i in str(n):
        count += 1
    mod = 10**(count-1)
    first = n//mod
    if first > max_digit(n%mod):
        return first
    else:
        return max_digit(n%mod)

def menu() -> None:
    print('Enter a choice for one of the following problems: ')
    print('1. Power')
    print('2. Sum digits')
    print('3. Count vowels')
    print('4. Print backwards')
    print('5. Max digit of an integer')
    print('6. Exit the program')

def main():
    choice = -1
    while(choice != 6):
        menu()
        choice = int(input())

        match(choice):
            case 1:
                print('Enter the base: ', end = '')
                base = int(input())
                print('Enter the power: ', end = '')
                pow = int(input())
                print('The result of taking the power of %d of base %d is %d.' \
                      % (pow, base, power(base, pow)))
            case 2:
                print('Enter the integer to sum the digits of: ', end = '')
                num = int(input())
                print('The result of summing the digits of the integer %d is %d.' \
                      % (num, sum_digits(num)))
            case 3:
                print('Enter the String of characters you want ' \
                      + 'to count the vowels of: ', end = '')
                word = input()
                print('The number of vowels in the String %s is %d.' \
                      % (word, num_vowels(word)))
            case 4:
                print('Enter the String of characters you ' \
                      + 'want to print backwards: ', end = '')
                word = input()
                print('The String %s printed backwards is: ' % (word), end = '')
                print_backwards(word)
                print('')
            case 5:
                print('Enter a positive integer to find the max digit of: ', end ='')
                num = int(input())
                print('The max digit of the integer %d is %d.' % (num, max_digit(num)))
            case 6: 
                print('End!')
            case _:
                print('Invalid choice!')
        print('')

if __name__=="__main__":
    main()
