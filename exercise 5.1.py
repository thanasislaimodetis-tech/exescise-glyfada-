def calc_retail_price(wholesale, markup):
    retail = wholesale + (wholesale * (markup / 100))
    return retail
def main():
    wholesale = float(input("Please enter a wholesale cost:\n"))
    markup = float(input("Please enter a markup percentage:\n"))
    price = calc_retail_price(wholesale, markup)
    print(f"The retail price is ${price:.2f}.")
if __name__ == "__main__":
    main()