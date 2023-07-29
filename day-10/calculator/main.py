# from replit import clear
from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1/n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}


def calculator():
  print(logo)
  
  num1 = float(input("What's the first number? "))
  
  for operation in operations:
    print(operation)
  
  calculation_on = True
  
  while calculation_on:
    operation_choice = input("Pick an operation from the above list. ")
    num2 = float(input("What's the next number? "))
    
    answer = operations[operation_choice](num1, num2)
    
    print(f"{num1} {operation_choice} {num2} = {answer}")
    
    continue_operations = input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation.: ")
    
    num1 = answer
    
    if continue_operations == "n":
      calculation_on = False
    #   clear()
      calculator()

calculator()