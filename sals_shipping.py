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

def print_best_shipping_method(weight):
  ground = ground_shipping(weight)
  premium = premium_ground_shipping
  drone = drone_shipping(weight)
  
  if ground < premium and ground < drone:
    method = "standard ground"
    cost = ground
  
  elif premium < ground and premium < drone:
    method =  "premium ground"
    cost = premium
  
  elif drone < ground and drone < premium:
    method = "drone"
    cost = drone

    print( "The cheapest available method is "+str(method)+" shipping and will cost $"+str(cost))
        
print_best_shipping_method(4.8)
print_best_shipping_method(100)

