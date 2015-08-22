#MIT Problem Set 1


#Test Case 1

outstanding_balance = float(raw_input("Enter your outstanding_balance: "))
annual_interest = float(raw_input("Enter the annual credit card interest rate as a decimal: "))
minimum_payment = float(raw_input("Enter the minimum monthly payment rate as a decimal: "))
total_paid = 0.0

for i in range(1, 13):
  monthly_interest_paid = round(outstanding_balance * annual_interest / 12.0, 2)
  minimum_payment_paid = round(outstanding_balance * minimum_payment, 2)
  principle_paid = minimum_payment_paid - monthly_interest_paid
  total_paid += (principle_paid + monthly_interest_paid)
  outstanding_balance -= principle_paid
  print "Month" + " " + str(i)
  print "Minimum Monthly payment: $%.2f" % (minimum_payment_paid)
  print "Principle Paid: $%.2f" % (principle_paid)
  print "Remaining Balance: $%.2f" % (outstanding_balance)


print "total paid: $%.2f" % (total_paid)
print "outstanding_balance: $%.2f" % (outstanding_balance)

