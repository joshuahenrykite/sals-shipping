def ground_shipping(weight):
  if weight <= 2.0:
    cost = 20 + (weight * 1.5)
  elif weight <= 6.0:
    cost = 20 + (weight * 3.0)
  elif weight <= 10.0:
    cost = 20 + (weight * 4.0)
  elif weight > 10.0:
    cost = 20 + (weight * 4.75)
  return cost

premium_ground_shipping = 125.00

def drone_shipping(weight):
  if weight <= 2.0:
    cost = (weight * 4.5)
  elif weight <= 6.0:
    cost = (weight * 9.0)
  elif weight <= 10.0:
    cost = (weight * 12.0)
  elif weight > 10.0:
    cost = (weight * 14.25)
  return cost
