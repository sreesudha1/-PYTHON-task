def salarycalculator(pay):
    deduction=18
    totaldeduction=(deduction/100)*pay
    totalpay=pay-totaldeduction
    return total_pay

check_salary=salarycalculator(10000)
if check_salary<900:
    print("your salary is too low")
