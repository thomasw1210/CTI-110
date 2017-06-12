 
# Projected Profit from Sales Program
# 11 June 2017
# CTI-110 M2T1 - Sales Prediction
# William Thomas
#
# Get input for projected total sales.
total_sales = float (input('Enter the projected sales: '))

# Calculate profit as 23 percent of projected sales.
profit = total_sales * 0.23

# Display estimated profit.
print('The projected profit is $', format(profit, ',.2f'))
