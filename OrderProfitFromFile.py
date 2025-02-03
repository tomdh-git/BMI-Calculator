def read_file(inp: str) -> list:
    """reads the input file

    Args:
        inp (str): the inputted file name from the user

    Returns:
        list: returns list of lines
    """
    lines = []
    try:
        file = open(inp,'r')
        content = file.readlines()
        for line in content: lines.append(line.strip().split())
    except FileNotFoundError: return 'File not Found'
    file.close()
    return lines
def get_order_profits(x: list) -> list:
    """gets the order profits by multiplying\
        amount and price

    Args:
        x (list): inputted list of lines

    Returns:
        list: returns list of all the profits for each line
    """
    lines = []
    for line in x: lines.append(int(line[2]) * float(line[3]))
    return lines
def display(x: list) -> None:
    """displays the order profits by printing each\
        item in the inputted list

    Args:
        x (list): uses the inputted list of each\
            order profit for each line 
    """
    ordernum = 0
    for order in x:
        ordernum += 1
        print('Order #%d profit is $%.2f.' % (ordernum,order))
def get_average_profit(x:list) -> float:
    """get the average profit by dividing the sum\
        by the amount of orders

    Args:
        x (list): the inputted order list\
            from the list of profits from each line\
                of the file

    Returns:
        float: returns the profit as a float
    """
    sum = 0
    ordernum = 0
    for order in x:
        sum += order
        ordernum += 1
    return sum/ordernum
def get_total_profit(x: list) -> float:
    """gets the total profit by adding all the\
        profits together into a sum

    Args:
        x (list): the inputted list of all profits\
            from each line of the file

    Returns:
        float: returns the sum as a float
    """
    sum = 0
    for order in x:
        sum += order
    return sum
def main():
    """asks for the filename, saves the orderlist\
        as a variable, displays each profit \
            as well as the average and total
    """
    print('Enter a filename: ', end = '')
    orderlist = get_order_profits(read_file(str(input())))
    display(orderlist)
    print('The average profit is %.2f.' % (get_average_profit(orderlist)))
    print('The total profit is %.2f.' % (get_total_profit(orderlist)))
if __name__ == "__main__": main()
