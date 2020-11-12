def salarycalculator(pay):
    deduction=18
    totaldeduction=(deduction/100)*pay
    totalpay=pay-totaldeduction
    print(totalpay)
salarycalculator(1000)
