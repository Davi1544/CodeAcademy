# variáveis
weight = 1.5
cost_ground = 0
cost_ground_premium = 0
cost_drone = 0

# nesta seção do curso, ainda não havia sido definido a sintaxe select ou a sintaxe function. Por isso, utilizou-se if, elif e else
# ground shipping
cost = 0
if weight <= 2:
  cost = 1.5 * weight + 20
  print("Ground Shipping: $" + str(cost))
elif weight > 2 and weight <= 6:
  cost = 3 * weight + 20
  print("Ground Shipping: $" + str(cost))
elif weight > 6 and weight <= 10:
  cost = 4 * weight + 20
  print("Ground Shipping: $" + str(cost))
elif weight > 10:
  cost = 4.75 * weight + 20
  print("Ground Shipping: $" + str(cost))

cost_ground = cost

# ground shipping premium
cost = 0
cost = 125.0
print("Ground Shipping Premium: $" + str(cost))
cost_ground_premium = cost

# drone shipping
cost = 0
if weight <= 2:
  cost = 4.5 * weight
  print("Drone Shipping: $" + str(cost))
elif weight > 2 and weight <= 6:
  cost = 9.0 * weight
  print("Drone Shipping: $" + str(cost))
elif weight > 6 and weight <= 10:
  cost = 12.0 * weight
  print("Drone Shipping: $" + str(cost))
elif weight > 10:
  cost = 14.25 * weight
  print("Drone Shipping: $" + str(cost))

cost_drone = cost