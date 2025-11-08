monthly_income = float(input('Enter your monthly income: '))
monthly_expenses = float(input('Enter your monthly expenses: '))

monthlySavings = monthly_income - monthly_expenses
projectedSavings = monthlySavings * 12 + (monthlySavings * 12 * 0.05)
print(f'Your monthly savings are: ${monthlySavings}')
print(f'Projected savings after one year with interest is: ${projectedSavings}')