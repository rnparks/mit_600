#MIT 6.00SC
#Problem Set 1 Problem 2


balance = float(raw_input("Enter your outstanding balance on your credit card: "))
annual_interest = float(raw_input("Enter your outstanding balance on your credit card: "))
monthly_interest = annual_interest / 12.0
monthly_minimum = 0.0
increment = 0.01
temp_balance = balance

while temp_balance > 0.0:
  temp_balance = balance
  monthly_minimum += increment
  for i in range(1, 13):
    temp_balance = round(temp_balance * (1 + monthly_interest) - monthly_minimum, 2)
    if temp_balance < 0.0:
      print "Number of Months to Pay off Debt:" + " " +str(i)
      print "Monthly amount needed: $%.2f" % (monthly_minimum)
      print "$%.2f" % (temp_balance)
      break




