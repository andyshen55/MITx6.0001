#program constants
portion_down_payment = 0.25
current_savings = 0.0
r = 0.04

#user input
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

#continues adding months until savings exceed down payment
months = 0
while (current_savings < total_cost * portion_down_payment):
    months += 1
    current_savings *= 1 + (r / 12)
    current_savings += annual_salary / 12 * portion_saved
     #increases salary semi-annually after every 6th month
    if not (months % 6):
        annual_salary *= 1 + semi_annual_raise
    
print("Number of months:", str(months))
