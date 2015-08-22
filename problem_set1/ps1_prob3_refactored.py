#MIT 6.00SC
#Problem Set 1 Problem 3 (bisection)

balance = float(raw_input("Enter your outstanding balance on your credit card: "))
annual_interest = float(raw_input("Enter your outstanding balance on your credit card: "))
monthly_interest = annual_interest / 12.0
lower_bound = balance / 12.0
upper_bound = (balance * ((1 + monthly_interest)**12)) / 12.0
mid_point = (lower_bound + upper_bound) / 2.0

def calculate_balance(amount, monthly_interest, monthly_payment):
  for i in range(1, 13):
    amount = amount * (1 + monthly_interest) - monthly_payment
  return amount

test = calculate_balance(balance, monthly_interest, mid_point)
while abs(test - 0) > .1:
  if test == 0.0:
    break
  elif test > 0.0:
    lower_bound = mid_point
  else:
    upper_bound = mid_point
  mid_point = (lower_bound + upper_bound) / 2.0
  test = calculate_balance(balance, monthly_interest, mid_point)

print mid_point
print test
