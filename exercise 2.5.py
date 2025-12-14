length = float(input("Please enter the length of the wall:\n"))
height = float(input("Please enter the height of the waall:\n"))
            
square_meters = length * height

neaded_cans = square_meters / 20 
neaded_cans = int(neaded_cans + 0.9999)


print(f"You require {neaded_cans} of paint.")