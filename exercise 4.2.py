speed = int(input("What is the speed of vechicle in mph?\n")) 
print("")
hours = int(input("How many hours has it travelled?\n"))
print("")
print("Hour | Distance Travelled")
print("-----------------------")
for i in range(0+1,hours+1):
    print(f"{i:<4} | {i*speed}")