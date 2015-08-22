#MIT 6.00SC
#Problem Set 1 Problem 3 (bisection)

import math



balance = float(raw_input("Enter your outstanding balance on your credit card: "))
annual_interest = float(raw_input("Enter your outstanding balance on your credit card: "))
monthly_interest = annual_interest / 12.0
lower_bound = balance / 12.0
upper_bound = (balance * ((1 + monthly_interest)**12)) / 12.0
mid_point = (lower_bound + upper_bound) / 2.0
print upper_bound
print lower_bound

def calculate_balance(amount, monthly_interest, monthly_payment):
  for i in range(1, 13):
    amount = amount * (1 + monthly_interest) - monthly_payment
  return amount



# print "Midpoint 1: %.2f" % (mid_point)

# while calculate_balance(balance, monthly_interest, mid_point) > 0.0:
#   lower_bound = mid_point
#   upper_bound = upper_bound
#   mid_point = (lower_bound + upper_bound) / 2.0

# print "Midpoint 2: %.2f" % (mid_point)

n = 0
while n < 30:
  print "going through time" + " " + str(n)
  if calculate_balance(balance, monthly_interest, mid_point) == 0.0:
    break
  elif calculate_balance(balance, monthly_interest, mid_point) > 0.0:
    lower_bound = mid_point
    upper_bound = upper_bound
    mid_point = (lower_bound + upper_bound) / 2.0
  else:
    lower_bound = lower_bound
    upper_bound = mid_point
    mid_point = (upper_bound + lower_bound) / 2.0
  n += 1

print mid_point
print calculate_balance(balance, monthly_interest, mid_point)





