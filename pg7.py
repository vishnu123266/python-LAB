num1 =int(input("Enter the first integer:" ))
num2 = int(input("Enter the second integer:"))

addition=num1+num2
substraction =num1-num2
multiplication =num1*num2

if num2 !=0:
    division =num1/num2
    modulus=num1%num2
else:
    division ="Undefined(division by zero)"
    modulus="Undefined(division by zero)"
print(f" {num1} + {num2} = {addition}(addition)")
print(f" {num1} - {num2} = {substraction}(substraction)")
print(f" {num1} * {num2} = {multiplication}(multiplication)")
print(f" {num1} / {num2} = {division}(division)")
print(f" {num1} % {num2} = {modulus}(modulus)")