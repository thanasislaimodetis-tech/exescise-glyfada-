child_ticket = 5
adult_ticket = 10
senior_ticket = 8

child_tickets = int(input("How many child tickets would you like?\n"))
adult_tickets = int(input("How many adults tickets would you like?\n"))
senior_tickets = int(input("How many senior tickets would you like?\n"))

child_cost = child_tickets * child_ticket
adult_cost = adult_tickets * adult_ticket
senior_cost = senior_tickets * senior_ticket

cost = child_cost + adult_cost + senior_cost

print("Total price: $",cost)