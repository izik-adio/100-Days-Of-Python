def add(x, y):
    """It adds two num"""
    return x + y
def subtract(x, y):
    """It subtract two num"""
    return x - y
def multiply(x, y):
    """it multiply to num"""
    return x * y
def divide(x, y):
    """it divides two num"""
    return x / y

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}
def calculator():
    print("""

    :'######:::::'###::::'##::::::::'######::
    '##... ##:::'## ##::: ##:::::::'##... ##:
     ##:::..:::'##:. ##:: ##::::::: ##:::..::
     ##:::::::'##:::. ##: ##::::::: ##:::::::
     ##::::::: #########: ##::::::: ##:::::::
     ##::: ##: ##.... ##: ##::::::: ##::: ##:
    . ######:: ##:::: ##: ########:. ######::
    :......:::..:::::..::........:::......:::

    """)
    num = float(input("What is the first number: "))
        
    while True:       
        for operand in operations:
            print(operand,end="   ")
        operation_symbol = input("\nPick an operation from the line above: ").lower().strip()
        num2  = float(input("What is the next number: "))
        
        if operation_symbol not in operations:
            print("invalid operation specified")
            result = num2
        else:
            result = operations[operation_symbol](num,num2)
            print(f"\n{num} {operation_symbol} {num2} = {result}")
            
        opt = input(f"\nType 'yes' if you would like to continue calclation with {result}, or type 'no' to start a new calculation: ").lower().strip()
        if opt == 'yes':
            num = result
        else:
            calculator()
calculator()