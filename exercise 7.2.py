def and_many(*args):
 
    for item in args:
        if item == False:
            return False
    return True

def or_many(*args):
   
    for item in args:
        if item == True:
            return True
    return False


if __name__ == "__main__":
    print("--- Testing and_many ---")
    print(and_many(True))    
    print(and_many(True, True))
    print(and_many(True, True, True))
    print(and_many(True, True, True, True))
    print(and_many(False, True))
    print(and_many(True, False, True))
    print(and_many(True, True, True, False))
    print("\n--- Testing or_many ---")
    print(or_many(True))
    print(or_many(False, True))
    print(or_many(True, False, True))
    print(or_many(True, True, True, False))
    print(or_many(False))
    print(or_many(False, False))
    print(or_many(False, False, False))
    print(or_many(False, False, False, False))