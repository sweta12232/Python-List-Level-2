home_prices_mexico = [
    22000000.0,
    1500000.0,
    3200000.0,
    5800000.0,
    7205000.34,
    6500000.21,
    500000.0,
]
#With simple list
increaseRate = []
for rate  in home_prices_mexico:
    increaseRate.append(rate*180)

print(increaseRate)

#With list comprehension
increaseRate = [price * 180 for price in home_prices_mexico]

print(increaseRate)
