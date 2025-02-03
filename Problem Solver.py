import math

def main():
    #print intro
    print('Welcome to the problem solver!')
    print('Please choose one of the 4 available options and follow all given prompts.')
    print("1. Determining a Student's Final Grade")
    print("2. Trigonometry Circle Quadrants")
    print("3. Getting Candy for Math")
    print("4. Solving a Summation Problem")

    #ask for input
    choice = int(input())
    match choice:
        case 1:
            finalgrade()
        case 2:
            trig()
        case 3:
            candy()
        case 4:
            summation()

def finalgrade():
    print('Enter the final grade value: ', end = '')
    gradval = float(input())
    if(gradval >= 0 and gradval <= 59): #make all intervals
        final = 'F'
    elif(gradval >= 60 and gradval <= 69):
        final = 'D'
    elif(gradval >= 70 and gradval <= 79):
        final = 'C'
    elif(gradval >= 80 and gradval <= 89):
        final = 'B'
    elif(gradval >= 90 and gradval <= 100):
        final = 'A'
    else:
        print('you gave me a number i couldnt handle')
    print('The final grade is an %s.' % (final)) #print final

def trig():
    print('Enter the degree of the circle: ', end = '')
    degree = float(input())
    if(degree >= 1 and degree <= 89):
        quadrant = 1
    elif(degree >= 91 and degree <= 179):
        quadrant = 2
    elif(degree >= 181 and degree <= 269):
        quadrant = 3
    elif(degree >= 271 and degree <= 359):
        quadrant = 4
    else:
        quadrant = 0
    if(quadrant != 0):
        print('The degree %.2f is in Quadrant %d.' % (degree, quadrant))
    else: #if angle is 0, 90, 180, 270, or 360
        print('This angle has no Quadrant')
    
def candy():
    print("Enter the number to see if it's a perfect square: ", end = '')
    userinput = int(input())
    squareroot = math.sqrt(userinput)
    square = math.pow(squareroot, 2)
    print(userinput == square) #if x == z

def summation():
    print('Enter the summation starting point: ', end = '')
    starting = int(input())
    print('Enter the summation ending point: ', end = '')
    ending = int(input())
    length = ending - starting
    sumres = 0
    for i in range(0,length + 1): #one more length
        sumres = sumres + starting + i #4 5
        i+=1
    print("The result of the summation is: %d" % sumres)

if __name__ == "__main__":
    main()
