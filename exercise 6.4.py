def calculate_change_coins(change_amount):


    coin_values = [50, 20, 10, 5, 2, 1]
    coins_count = [] 

    remaining_change = change_amount

    for coin in coin_values:

        count = remaining_change // coin
        

        coins_count.append(count)
        

        remaining_change = remaining_change % coin
        
    return coins_count

def main():

    try:
        print("Please enter the amount inserted (1 to 100):")
        amount_inserted = int(input())
    except ValueError:
        return 


    if amount_inserted > 100 or amount_inserted < 1:
        print("Invalid amount")
        return


    try:
        print("Please enter the cost of the item:")
        item_cost = int(input())
    except ValueError:
        return


    if item_cost > amount_inserted:
        print("Item costs more than amount inserted")
        return


    total_change = amount_inserted - item_cost
    

    change_list = calculate_change_coins(total_change)

    coin_labels = [50, 20, 10, 5, 2, 1]
    
    for i in range(len(coin_labels)):

        print(f"Number of {coin_labels[i]}p coins is {change_list[i]}")

if __name__ == "__main__":
    main()