basic_pay= float(input("Enter basic pay of the employee: "))
hra=0.10*basic_pay
ta =0.05*basic_pay
total_salary=basic_pay+hra+ta
print(f"basic pay: {basic_pay}")
print(f"HRA(10% of basic):{ta}")
print(f"TA(5% of basic):{ta}")
print(f"Total salary: {total_salary}")