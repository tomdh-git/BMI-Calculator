import math
import sys

def draw_border(length,character,middle):#drawborder with the parameter length and character
    if middle == False: #basically top border test=f middle border test = t
        print(' ', end='')
    else:
        print('', end='')
    for i in range(length):
        print(str(character), end = '')
    if middle == True: #if middle make it end so you can add the |
        print('', end='')
    else:
        print('')

def main():
    #display
    print('Enter your first and last name: ', end ='')#names
    name = input()
    print('Enter your age: ' , end = '')#age
    age = input()
    print('Enter your weight(lb): ' , end = '')#weight
    weight = float(input())
    #weight = int(('%.3s' % (weight)))
    print('Enter your height(feet): ' , end = '') #height
    height_feet = float(input())
    #height_feet = int(('%.1s' % (height_feet)))

    #calculate everything
    height_inch = height_feet * 12
    inchsquared = height_inch * height_inch
    weight703 = weight * 703
    bmi = (round(weight703 / inchsquared,3))

    #display everything
    #draw 38 - with space in front
    draw_border(38,'-',False) #top border so middle = f
    print('|%-20s|%-8s|%-8s|' % ('Name','Age' ,'BMI'))
    print('|', end='')
    draw_border(38,'.',True) #middle = t
    print('|')
    print('|%-20s|%-8s|%-8.5s|' % (name, age, round(bmi,1)))
    draw_border(38,'-',False) #again

    #ask input
    print('Enter an input filename: ' , end = '')
    inputfile = input()

    #read files and such
    file = open(str(inputfile), 'r')
    name2 = file.readline().strip()
    age2 = file.readline().strip()
    weight2 = float(file.readline().strip())
    height2 = float(file.readline().strip())
    file.close()
    #calculate everything
    height_inch2 = height2 * 12
    inchsquared2 = height_inch2 * height_inch2
    weight703_2 = weight2 * 703
    bmi2 = (round(weight703_2 / inchsquared2,3))
    

    #display everything
    #draw 38 - with space in front
    draw_border(38,'-',False) #top border so middle = f
    print('|%-20s|%-8s|%-8s|' % ('Name','Age' ,'BMI'))
    print('|', end='')
    draw_border(38,'.',True) #middle = t
    print('|')
    print('|%-20s|%-8s|%-8.4s|' % (name2, age2, round(bmi2,1)))
    draw_border(38,'-',False) #again

    #output stuff
    print('Enter an output filename: ' , end = '')
    outputfile = input()
    file = open(str(outputfile), 'w')
    file.write(" " + "-" * 38) 
    file.write('\n|%-20s|%-8s|%-8s|' % ('Name','Age' ,'BMI'))
    file.write("\n|" + "." * 38 + "|") 
    file.write('\n|%-20s|%-8s|%-8.4s|' % (name, age, round(bmi,1)))
    file.write("\n|" + "." * 38 + "|")
    file.write('\n|%-20s|%-8s|%-8.3s|' % (name2, age2, round(bmi2,1)))
    file.write("\n " + "-" * 38)
    file.close()
    


if __name__ == "__main__":
    main()