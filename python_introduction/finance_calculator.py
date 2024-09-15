# Financial Details Calculator

# Get user input
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Calculate projected annual savings with interest
annual_interest_rate = 0.05
projected_annual_savings = monthly_savings * 12 + (monthly_savings * 12 * annual_interest_rate)

# Output results
print("Your monthly savings are: ${:.2f}".format(monthly_savings))
print("Projected savings after one year, with interest, is ${:.2f}".format(projected_annual_savings))