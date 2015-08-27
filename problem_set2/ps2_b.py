poly = (-13.39, 0.0, 17.5, 3.0, 1.0)


def compute_deriv(poly):
  ans = []
  if len(poly) == 1:
    return (0.0,)
  else:
    for i in range(1, len(poly)):
      ans.append(poly[i] * i)
  return tuple(ans)


print compute_deriv(poly)

