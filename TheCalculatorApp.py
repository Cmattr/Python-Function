print ("welcome to the calculator")

a = int(input("Input your first number: "))
b = int(input("input your second number: "))

def add (a, b):
    return a + b

def subtract (a, b):
    return a - b

def multiply (a, b):
    return a * b

def divide (a, b):
    try:
        a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
  


operator = input (''' please select an option by number
1. add
2. subtract
3. multiply
4. divide
5. exit
:  ''')

    
if operator == '1' :
    result = add(a, b)
    print(f"the result is: {result}")
elif  operator == '2' :
    result = subtract(a, b)
    print (f"the result is {result}")
elif operator == '3' :
    result = multiply(a, b)
    print(f"the result is {result}")
elif operator ==  '4' :
     result = divide(a, b)
     print(f"the result is {result}")
   
else :
    print ("you have not selected a viable option")
