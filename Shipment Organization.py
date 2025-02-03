#Name: Dasan Tom
#Project 4: Remote Pharmacy Medicine Shipment

def menu():
    """prints menu choices
    """
    print('1. Load from a file')
    print('2. Print from the loaded list')
    print('3. Sort the list based on shipment IDs')
    print('4. Sort the list based on the tracking numbers')
    print('5. Print the sorted list')
    print('6. Exit')
def sort1(x:list)->None:#[x,shipmentid,y,tracking]
    """sorts the input list based on shipmentid
    using selection sort

    Args:
        x (list): the inputted list
    """
    n = len(x) #3
    for i in range(n): #0 1 2 3
        min = i #0
        for j in range(i+1,n):#1 2
            if x[j][1]<x[min][1]: #4<5 3<4
                min = j #1 2
        x[i],x[min] = x[min],x[i] #5 and 3 become 3 and 5
def sort2(x:list)->None:
    """sorts the input list based on tracking number
    using selection sort

    Args:
        x (list): the inputted list
    """
    n = len(x) #3
    for i in range(n): #0 1 2 3
        min = i #0
        for j in range(i+1,n):#1 2
            if x[j][3]<x[min][3]: #4<5 3<4
                min = j #1 2
        x[i],x[min] = x[min],x[i] #5 and 3 become 3 and 5
if __name__ == "__main__":
    success = False
    fileloaded = False
    sort = False
    while not success:
        menu()
        print('Enter a number[1-6]: ',end = ''); choice = input()
        match choice:
            case '1':
                fileloaded = True 
                print('Enter the name of the file: ', end = '')
                content = []
                with open(input(),'r') as file:
                    for line in file: content.append(line.strip().split())
                print('Loading from the file is done!')
                print('',end = '')
            case '2': 
                success = False
                done = False
                page = 0
                while not done and fileloaded:
                    if page == 0: print('**** Printing the list ****')
                    if len(content)<10:
                        for i in range(0,len(content)+1): print(content[i])
                    else:
                        for i in range(10*page,10*page +10): print(content[i]); highest = i
                        print('Enter something to continue/enter s to stop: ', end= '')
                        if input() == 's': done = True
                        elif highest + 1 >= len(content): done = True
                        else: done = False; page += 11
            case '3': 
                if fileloaded:
                    success = False
                    #sort by shipid
                    shipid = []
                    for i in content: shipid.append(i)
                    sort1(shipid)
                    res = shipid
                    print('Sorting is done!')
                    sort = True
            case '4': 
                if fileloaded:
                    success = False
                    #sort by tracknum
                    tracknum = []
                    for i in content: tracknum.append(i)
                    sort2(tracknum)
                    res = tracknum
                    print('Sorting is done!')
                    sort = True
            case '5':
                success = False
                if not sort and fileloaded: print('Nothing sorted yet!')
                elif sort:
                    done = False
                    page = 0
                    while not done:
                        if page == 0: print('**** Printing the list ****')
                        if len(res)<10:
                            for i in range(0,len(res)+1): print(res[i])
                        else:
                            for i in range(10*page,10*page +10): print(res[i]); highest = i
                            print('Enter something to continue/enter s to stop: ', end= '')
                            if input() == 's': done = True
                            elif highest + 1 >= len(res): done = True
                            else: done = False; page += 1
            case '6': success = False; print('End!'); break
            case _: success = False; print('not a valid input')
        if 2<=int(choice)<=5 and not fileloaded: print('No data has been loaded yet!'); print('')
        elif fileloaded: print('')
        
        

    
        
