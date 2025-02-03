# Practicing writing functions.

# TODO
# ADD get_letter() and get_word functions here

def get_letter(input: str):
    """gets a letter from a 8 digit long binary code

    Args:
        input (str): input as a string

    Returns:
        string: returns a string from the binary code
    """
    i = 7
    res = 0
    for char in input:
        if char == '1':
            res += 2**i
        i -= 1
    res = chr(res)
    return res
    
def get_word(input: str):
    """gets a word from a string input. splits \
        into splits of 8 and finds the letter for each\
        substring

    Args:
        input (str): input as a string(binary code)

    Returns:
        string: returns a joined list
    """
    temp = input
    count = 0
    res = []
    for i in temp:
        count += 1
    for i in range(1,int(count/8)+1):
        help1 = 8*(i-1)
        help2 = 8*i
        substring = temp[help1:help2] #0 then 8
        res.append(get_letter(substring))
    return ''.join(res)

def menu() -> None:
    """
    Prints a menu with options on the display.

    Args: 
        None
    
    Returns: 
        None
    """
    print('**Binary Code Translator v 1.0**')
    print('1. Translate a binary code into a letter')
    print('2. Translate binary codes into a word')
    print('3. Exit\nEnter a number [1-3]: ', end = '')

def main():
    option = -1

    while(option != 3):
        menu()
        try:
            option = int(input())
        except ValueError as e:
            option = 0
        
        match(option):
            case 1:
                print('Enter a single binary code: ', end = '')
                letter = get_letter(input())
                print('The letter is: %s\n' % (letter))
            case 2:
                print('Enter binary codes: ', end = '')
                word = get_word(input())
                print('The word is: %s\n' % (word))
            case 3:
                print('End!')
            case _:
                print('Invalid input!')

if __name__=="__main__":
    main()
    
