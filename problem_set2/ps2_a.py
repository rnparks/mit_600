poly = (0.0, 0.0, 5.0, 9.3, 7.0)


def evaluate_poly(poly, x):
  ans = 0.0
  for i in range(len(poly)):
    ans += (poly[i] * x ** i)
  return ans


print evaluate_poly(poly, -13.0)


for index, item in enumerate(poly):
    print index, item
