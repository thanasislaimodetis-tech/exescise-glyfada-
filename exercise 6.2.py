import random

def rand_num_list_gen(num=100, lower=1, upper=50):

    rand_num_list = [random.randint(lower, upper) for _ in range(num)]
    return rand_num_list

def main():

    random_numbers = rand_num_list_gen()
    

    counts = [0, 0, 0, 0, 0]
 
    for n in random_numbers:
        if 1 <= n <= 10:
            counts[0] += 1
        elif 11 <= n <= 20:
            counts[1] += 1
        elif 21 <= n <= 30:
            counts[2] += 1
        elif 31 <= n <= 40:
            counts[3] += 1
        elif 41 <= n <= 50:
            counts[4] += 1

    print("I have generated 100 random numbers between 1 and 50.")
    print("The count in the following ranges is:")
    print(f"1..10: {counts[0]}")
    print(f"11..20: {counts[1]}")
    print(f"21..30: {counts[2]}")
    print(f"31..40: {counts[3]}")
    print(f"41..50: {counts[4]}")

def advanced_main():
    num_to_gen = int(input("Please enter the number of integers to generate between 1 and 50.:\n"))
    
 
    ranges_input = input("Please enter the ranges in the following format:\ne.g. 1..5,6..10,11..20,21..30,31..40,41..50\n")

    random_numbers = rand_num_list_gen(num=num_to_gen)

    raw_ranges = ranges_input.split(',')
    
    parsed_ranges = []
    for item in raw_ranges:

        parts = item.strip().split('..')
        lower = int(parts[0])
        upper = int(parts[1])

        parsed_ranges.append([lower, upper, 0])

    for num in random_numbers:
        for i in range(len(parsed_ranges)):
            lower = parsed_ranges[i][0]
            upper = parsed_ranges[i][1]

            if lower <= num <= upper:
                parsed_ranges[i][2] += 1

    print("The count in the given ranges is:")
    for r in parsed_ranges:
        print(f"{r[0]}..{r[1]}: {r[2]}")

if __name__ == "__main__":
   
    advanced_main()   

