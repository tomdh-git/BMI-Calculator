# @author Dasan Tom

def not_descending(a: int, b: int, c: int) -> bool:
    """Given 3 ints a, b, and c, return True 
        if they are in descending order. If there 
        are similar values, it should return False.

    Args:
        a (int): first input
        b (int): second input
        c (int): third input

    Returns:
        bool: returns true if they are in descending order
        or false if they are not or equal
    """
    if a > b and b > c and a > c:
        return True
    else:
        return False

def check_nums(n: int, start: int, end: int, check: bool) -> bool:
    """Given a number n, return True if n 
    is in the range of [start - end] and check is True,
    inclusive. If check is False, return True if the number
    is less than start, or greater than end.

    Args:
        n (int): number input
        start (int): starting number
        end (int): ending number
        check (bool): if true, return range, if false
        return less than start or greater than end

    Returns:
        bool: returns true if check is true and n is in start to end
        or if the check is false and the number is less than the start
        or greater than the end. returns false if otherwise
    """
    if check == True:
        for i in range(start,end+1):
            if i == n:
                return True
        return False
    else:
        if n > end or n<start:
            return True
        else:
            return False

def get_substring(inp: str, start: int, end: int, check: bool) -> str:
    """gets a substring from an input from start to end

    Args:
        inp (str): the input string that you want to get the substring for
        start (int): starting number
        end (int): ending number
        check (bool): check two options

    Returns:
        str: returns the substring of the range 
        from the two int values if the boolean value is true
        if the check is false then return the input
    """
    if check == True: return inp[start:end]
    else:
        return inp

def switch_xo(inp: str) -> str:
    """Given a String, switch the X to 
    O and vice versa, and return a new String.


    Args:
        inp (str): the string input that you want
        to switch the xs and os for 

    Returns:
        str: returns a new string with the xs and os switched
    """
    list = []
    if inp == '':
        return ''
    for i in inp:
        if i == 'X':
            list.append('O')
        else:
            list.append('X')
    return ''.join(list)

def next_div7(num: int) -> int:
    """Given a none-zero int, return the 
    first number that is divisible by 7 after 
    the given number

    Args:
        num (int): number input that you want
        to check the first number that is divisible by
        7 for

    Returns:
        int: returns the first number that is divisible by 7
        after the input number
    """
    success = False
    while success == False:
        num += 1
        if num % 7 == 0:
            success == True
            return num

def change_odd_chars(inp: str, odd: bool) -> str:
    """Given a String str and a boolean value odd, 
    create a new String and change all characters
located at odd indices to uppercase and characters 
located at even indices to lowercase. or all characters
located at odd indices should change to
lowercase and the rest to uppercase

    Args:
        inp (str): the inputted 
        odd (bool): _description_

    Returns:
        str: _description_
    """
    list = []
    if odd:
        for i in range(0,len(inp),2):
            list.insert(i,inp[i:i+1].lower())
        for i in range(1,len(inp),2):
            list.insert(i,inp[i:i+1].upper())
    return ''.join(list)

def what_missing(inp: str) -> str:
    """finds the missing letter in a string in alphabetical order

    Args:
        inp (str): the inputted string that has a missing letter

    Returns:
        str: returns the missing letter
    """
    list = ['a','b','c','d','e','f','g','h','i',\
        'j','k','l','m','n','o','p','q','r','s',\
            't','u','v','w','x','y','z']
    list = ''.join(list)
    if list[0:len(inp)] != inp:
        return (list[len(inp)-1])
    else:
        return ''

def get_similars(s1: str, s2: str, s3: str) -> str:
    """finds a letter or letters 
    in the string that all 
    three strings have in common

    Args:
        s1 (str): first string
        s2 (str): second string
        s3 (str): third string

    Returns:
        str: returns the letters that they have in common
    """
    list = []
    for i in s1:
        for j in s2:
            for k in s3:
                if i == j and j == k and i == k:
                    list.append(i)
    return ''.join(list)

def add_digits(inp: str) -> int:
    """finds the sum of all integers 
    in the string

    Args:
        inp (str): the inputted string

    Returns:
        int: returns the sum of all the integers
    """
    sum = 0
    if inp == '':
        return 0
    for i in inp:
        try:
            i = int(i)
            sum += i
        except ValueError:
            sum+=0
    return sum

def add_divisibles(num: int) -> int:
    """add all even divisible numbers of the int

    Args:
        num (int): the inputted integer 

    Returns:
        int: returns the sum of all the even divisible
        numbers of the int
    """
    sum = 0
    for i in range(1,num):
        if num % i == 0 and i % 2 == 0:
            sum += i
    return sum

def fix_sentence(inp: str) -> str:
    """capitilize the first character and before 
    the start of every word

    Args:
        inp (str): the inputted sentence

    Returns:
        str: returns the string with capitilized
        first letter of every word
    """
    list = []
    space = -1
    for i in range(0,len(inp)): #good
        if i == 0 or space > 0:
            list.append(inp[i].upper())
            space = 0
        else:
            if inp[i] == ' ':
                space = i
                
            list.append(inp[i])
    return ''.join(list)

def switch_signs(inp: str) -> str:
    """switches the signs from negative to 
    positive and vice versa

    Args:
        inp (str): the inputted string that you 
        want to switch the signs for

    Returns:
        str: returns the string but with switched
        signs
    """
    list = []
    if inp == '':
        return ''
    for i in inp.split():
        if int(i) > 0:
            list.append('-%d'%int(i))
        else:
            list.append(i.lstrip('-'))
    return ' '.join(list)

def double_hi(inp: str) -> bool:
    """finds how many times the word
    hi is said in the string

    Args:
        inp (str): the string that you want
        to find how many his there are in it

    Returns:
        bool: returns true if there are two his
        in the string and false if there are not
    """
    hcount = 0
    icount = 0
    if inp == '':
        return False
    for i in inp:
        if i.upper() == 'H':
            hcount += 1
        if i.upper() == 'I':
            icount += 1
    if icount == 2 and hcount == 2:
        return True
    else:
        return False

def put_together(inp: str) -> str:
    """sorts a string by the characters in it

    Args:
        inp (str): inputted string that you want
        to sort

    Returns:
        str: returns the sorted string
    """
    if inp == '':
        return ''
    char_count = {}
    for char in inp: #for each letter in inp
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    res = []
    for char in inp: #acda
        if char in char_count: #if a in charcount
            res.append(char * char_count[char])
            del char_count[char] #delete from dictionary

    # Join the list into a string
    return ''.join(res)

def get_sec_max(inp: str) -> float:
    """get the second maximum from a string

    Args:
        inp (str): the inputted string that you
        want to get the second max from

    Returns:
        float: returns the second max from the string
    """
    count = 0
    if inp == '':
        return 0.0
    inp = inp.split()
    for i in inp:
        count += 1
    for i in range(0,count):
        greatest = inp[i-1] #1.3 1.3
        if float(inp[i]) > float(greatest): #4.1>1.3 5>1.3
            second = float(greatest) #1.3
            greatest = float(inp[i]) #4.1
        else:
            second = inp[i]
    return second

def main():
    print('***Testing not_descending***')
    print('False == ' + str(not_descending(1, 2, 3)))
    print('True == ' + str(not_descending(3, 2, 1)))
    print('True == ' + str(not_descending(-2, -3, -4)))
    print('')

    print('***Testing check_nums***')
    print('True == ' + str(check_nums(2, 1, 10, True)))
    print('False == ' + str(check_nums(0, 1, 10, True)))
    print('True == ' + str(check_nums(10, 9, 10, True)))
    print('')

    print('***Testing get_substring***')
    print('a == ' + str(get_substring('abc', 0, 1, True)))
    print('000111222 == ' + str(get_substring('000111222', 0, 3, False)))
    print('Hell == ' + str(get_substring('Hello', 0, 4, True)))
    print('')

    print('***Testing switch_xo***')
    print('O == ' + str(switch_xo('X')))
    print(' == ' + str(switch_xo('')))
    print('XO == ' + str(switch_xo('OX')))
    print('')

    print('***Testing next_div7***')
    print('7 == ' + str(next_div7(1)))
    print('14 == ' + str(next_div7(8)))
    print('14 == ' + str(next_div7(9)))
    print('')

    print('***Testing change_odd_chars***')
    print('aB == ' + str(change_odd_chars('ab', True)))
    print('aAaAa == ' + str(change_odd_chars('aaaaa', True)))
    print('aBcSdE == ' + str(change_odd_chars('ABcsde', True)))
    print('')

    print('***Testing what_missing***')
    print('b == ' + str(what_missing('ac')))
    print(' == ' + str(what_missing('ab')))
    print('f == ' + str(what_missing('abcdeg')))
    print('')

    print('***Testing get_similars***')
    print('ab == ' + str(get_similars('ab', 'ab', 'ab')))
    print('a == ' + str(get_similars('ab', 'ac', 'ad')))
    print('a == ' + str(get_similars('a', 'ab', 'abc')))
    print('')

    print('***Testing add_digits***')
    print('0 == ' + str(add_digits('')))
    print('0 == ' + str(add_digits('a0')))
    print('3 == ' + str(add_digits('1fr2')))
    print('')

    print('***Testing add_divisibles***')
    print('12 == ' + str(add_divisibles(12)))
    print('0 == ' + str(add_divisibles(1)))
    print('0 == ' + str(add_divisibles(5)))
    print('')

    print('***Testing fix_sentence***')
    print('Hi == ' + str(fix_sentence('hi')))
    print('Good Morning == ' + str(fix_sentence('Good morning')))
    print('Nice Job! == ' + str(fix_sentence('nice job!')))
    print('')

    print('***Testing switch_signs***')
    print(' == ' + str(switch_signs('')))
    print('-1 == ' + str(switch_signs('1')))
    print('2 -3 == ' + str(switch_signs('-2 3')))
    print('')

    print('***Testing double_hi***')
    print('True == ' + str(double_hi('HiHi')))
    print('False == ' + str(double_hi('')))
    print('True == ' + str(double_hi('Hkji3Hi')))
    print('')

    print('***Testing put_together***')
    print(' == ' + str(put_together('')))
    print('aacd == ' + str(put_together('acda')))
    print('11ww222gddm == ' + str(put_together('1w2g1dw2md2')))
    print('')

    print('***Testing get_sec_max***')
    print('1.2 == ' + str(get_sec_max('2 1.2')))
    print('4.1 == ' + str(get_sec_max('1.3 4.1 5')))
    print('0.0 == ' + str(get_sec_max('')))

if __name__=="__main__":
    main()
