def evaluate_poly(poly, x):
  ans = 0.0
  for i in range(len(poly)):
    ans += (poly[i] * x ** i)
  return ans


def compute_deriv(poly):
  ans = []
  if len(poly) == 1:
    return (0.0,)
  else:
    for i in range(1, len(poly)):
      ans.append(poly[i] * i)
  return tuple(ans)

poly = (-13.39, 0.0, 17.5, 3.0, 1.0)
x_0 = 0.1
epsilon = .0001

def compute_root(poly, x_0, epsilon):
  interations = 1
  while abs(evaluate_poly(poly, x_0)) >= epsilon:
    x_0 -= (evaluate_poly(poly, x_0) / evaluate_poly(compute_deriv(poly), x_0))
    interations += 1
  return (x_0, interations)

print compute_root(poly, x_0, epsilon)





