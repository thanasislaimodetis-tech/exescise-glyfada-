#from tracer import trace
#@trace 
def base_10_convertor_rec(num_string, convert_from_base):
 
    if len(num_string) == 0:
        return 0


    last_digit = int(num_string[-1])
    
 
    remaining_string = num_string[:-1]


    previous_value = base_10_convertor_rec(remaining_string, convert_from_base)
    
    return last_digit + (convert_from_base * previous_value)


if __name__ == "__main__":
    print(base_10_convertor_rec("1011", 2))   # prints 11
    print(base_10_convertor_rec("00341", 5))  # prints 96
    print(base_10_convertor_rec("00341", 6))  # prints 133
    print(base_10_convertor_rec("00341", 10)) # prints 341