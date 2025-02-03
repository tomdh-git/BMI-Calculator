#name: dasan tom
#polish notation calculator

def main():
    #ask
    print('Enter input file name: ', end = '')

    #file stuff
    file = open(str(input()), 'r')
    content = file.readlines()
    file.close()

    line = 0
    #for every element in the set
    for equation in content:
        #goal:
        #solve element

        #steps:
        #-find the operation done
        #-run checks
        #if its +=*/ then you cant solve with one number
        #if its < then you can solve with one number

        #-find all numbers
        #-solve
        line += 1 #increment line num
        solving = equation.strip().split() #remove \n make it one word each
        nums = 0 #how many nums
        try:
            operation = solving[0] #find operatiion
            first = int(solving[1]) #find first number 
            for num in solving: #finding all nums (for all numbers in solving)
                nums += 1 #find all numbers, including op and first
            listsecabove = [] #reset list
            for i in range(2,nums): #range from second above
                listsecabove.append(int(solving[i])) #second and above
            match operation: #match op to things
                case '+': 
                    for n in listsecabove: #for second and above add all nums
                        first += n #add it to first num
                    print('Result of Line %d: %d' % (line,first)) #print stuff
                    res = first #make it res
                case '-':
                    for n in listsecabove:
                        first -= n
                    print('Result of Line %d: %d' % (line,first))
                    res = first
                case '*':
                    for n in listsecabove:
                        first *= n
                    print('Result of Line %d: %d' % (line,first))
                    res = first
                case '/':
                    for n in listsecabove:
                        first //= n
                    print('Result of Line %d: %d' % (line,first))
                    res = first
                case '<+':
                    #add to previous sums
                    res = res + first #prev + first + secnum
                    for n in listsecabove:
                        res += n
                    print('Result of Line %d: %d' % (line,res))
                case '<-':
                    #subtract from previous sums
                    res = res - first #3-10-3
                    for n in listsecabove:
                        res -= n
                    print('Result of Line %d: %d' % (line,res))
                case '<*':
                    #multiply from previous sums
                    res = res * first
                    for n in listsecabove:
                        res *= n
                    print('Result of Line %d: %d' % (line,res))
                case '</':
                    #divide from previous sums
                    res = res // first
                    for n in listsecabove:
                        res //= n
                    print('Result of Line %d: %d' % (line,res))
            
        except IndexError: #if there isnt a second number or something
            #check if operation is <
            #print('i got an index error')
            second = 0
            match operation: #these you can solve
                case '<+':
                    #add to previous sums
                    res = res + first #prev + first + secnum
                    for n in listsecabove:
                        res += n
                    print('Result of Line %d: %d' % (line,res))
                case '<-':
                    #subtract from previous sums
                    res = res - first #3-10-3
                    for n in listsecabove:
                        res -= n
                    print('Result of Line %d: %d' % (line,res))
                case '<*':
                    #multiply from previous sums
                    res = res * first
                    for n in listsecabove:
                        res *= n
                    print('Result of Line %d: %d' % (line,res))
                case '</':
                    #divide from previous sums
                    res = res // first
                    for n in listsecabove:
                        res //= n
                    print('Result of Line %d: %d' % (line,res))
            if (operation != '<+' and operation != '<-' and operation != '<*' and operation != '</'):
                print('error') #if it has one int and starts with < which means error
        except ValueError: #if first or second is a str or something
            if (operation != '+' and operation != '-' and operation != '*' and operation != '/'\
                and operation != '<+' and operation != '<-' and operation != '<*' and operation != '</'):
                print('Result of Line %d: No operator %s' % (line,equation), end = '')
            if (operation == '+' or operation == '-' or operation == '*' or operation == '/'\
                or operation == '<+' or operation == '<-' or operation == '<*' or operation == '</'):
                print('Result of Line %d: %s' % (line,'Non-integer input on this Line')) #meaning error
            res = 0
        except ZeroDivisionError: #divide by zero
            print('Result of Line %d: %s' % (line,'Error: / by zero'))
            res = 0
        except UnboundLocalError:
            print('error')
            res = 0
        except NameError:
            
            res = 0
            first = 0
            second = 0
          
if __name__ == "__main__":
    main()
