from art import logo
print(logo)

#calculator

#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2 

#Dictionary to store the key-value pairs for different operators
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

#intial inputs
num1 = int(input("What is the first number: "))
num2 = int(input("What is the first number: "))

#display operators
for operator in operations:
  print(operator)

#user selects operator
selected_operator = input("Pick an operator: ")

answer = operations[selected_operator](num1, num2)

print(f"{num1} {selected_operator} {num2} = {answer}")









# #functions with outputs
# f_name = input("What is your first name?")

# l_name = input("What is your last name?")



# def format_name(fname, lname):
#   """Takes the first and last name and 
#   formats it so that the first letter is capitalized."""
#   formated_f_name = fname.title()
#   formated_l_name = lname.title()
#   fullname = print(f"{formated_f_name} {formated_l_name}")
#   return fullname

# format_name(f_name, l_name)
# format_name()